import contextlib
import hashlib
import importlib.util
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('secure_installer', Path(__file__).resolve().parents[1] / 'scripts/install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerSecurityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.home = self.root / 'home'
        self.home.mkdir()
        self.outside = self.root / 'outside'
        self.outside.mkdir()

    def link(self, target, path):
        try:
            path.symlink_to(target, target_is_directory=True)
        except OSError as error:
            self.skipTest(f'OS does not permit test symlinks: {error}')

    def test_parent_link_cannot_redirect_installation(self):
        self.link(self.outside, self.home / 'pets')
        with self.assertRaises(ValueError):
            installer.install(self.home)
        self.assertEqual(list(self.outside.iterdir()), [])

    def test_backup_link_does_not_move_existing_files(self):
        old = self.home / 'pets/yuexinmiao-selected'
        old.mkdir(parents=True)
        (old / 'sentinel.txt').write_text('keep this file')
        self.link(self.outside, self.home / 'pet-backups')
        with self.assertRaises(ValueError):
            installer.install(self.home, 'replace')
        self.assertEqual((old / 'sentinel.txt').read_text(), 'keep this file')
        self.assertEqual(list(self.outside.iterdir()), [])
        self.assertEqual(list(old.parent.iterdir()), [old])

    def test_existing_target_link_is_rejected(self):
        (self.home / 'pets').mkdir()
        self.link(self.outside, self.home / 'pets/yuexinmiao-selected')
        with self.assertRaises(ValueError):
            installer.install(self.home, 'replace')
        self.assertEqual(list(self.outside.iterdir()), [])

    def package_copy(self):
        root = self.root / 'package'
        shutil.copytree(installer.ROOT / 'dist', root / 'dist')
        shutil.copy2(installer.ROOT / 'CHECKSUMS.sha256', root / 'CHECKSUMS.sha256')
        return root

    def test_changed_payload_is_rejected_before_any_install_write(self):
        package = self.package_copy()
        (package / 'dist/yuexinmiao-selected/spritesheet.webp').write_bytes(b'corrupted image')
        with patch.object(installer, 'ROOT', package), self.assertRaises(ValueError):
            installer.install(self.home)
        self.assertEqual(list(self.home.iterdir()), [])

    def test_manifest_cannot_choose_a_traversal_destination(self):
        package = self.package_copy()
        path = package / 'dist/yuexinmiao-selected/pet.json'
        manifest = json.loads(path.read_text(encoding='utf-8'))
        manifest['id'] = '../../outside'
        path.write_text(json.dumps(manifest), encoding='utf-8')
        checksum = package / 'CHECKSUMS.sha256'
        lines = checksum.read_text().splitlines()
        lines = [hashlib.sha256(path.read_bytes()).hexdigest() + '  dist/yuexinmiao-selected/pet.json'
                 if line.endswith('dist/yuexinmiao-selected/pet.json') else line for line in lines]
        checksum.write_text('\n'.join(lines) + '\n')
        with patch.object(installer, 'ROOT', package), self.assertRaises(ValueError):
            installer.install(self.home)
        self.assertEqual(list(self.home.iterdir()), [])
        self.assertEqual(list(self.outside.iterdir()), [])


if __name__ == '__main__':
    with contextlib.redirect_stdout(io.StringIO()):
        unittest.main()
