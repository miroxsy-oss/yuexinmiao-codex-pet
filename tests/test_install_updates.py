import contextlib,importlib.util,io,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
spec=importlib.util.spec_from_file_location('installer',Path(__file__).resolve().parents[1]/'scripts/install.py');installer=importlib.util.module_from_spec(spec);spec.loader.exec_module(installer)

class UpdateTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.home=Path(self.tmp.name);self.old=self.home/'pets/yuexinmiao-selected'
 def tearDown(self):self.tmp.cleanup()
 def old_version(self):
  self.old.mkdir(parents=True);(self.old/'pet.json').write_text('{"id":"yuexinmiao-selected"}');(self.old/'spritesheet.webp').write_bytes(b'previous-version')
 def test_fresh_and_repeat_do_not_duplicate(self):
  installer.install(self.home);installer.install(self.home);self.assertEqual(len(list((self.home/'pets').iterdir())),1);self.assertFalse((self.home/'pet-backups').exists())
 def test_noninteractive_requires_choice_without_writes(self):
  self.old_version()
  with patch.object(installer.sys.stdin,'isatty',return_value=False),self.assertRaises(ValueError):installer.install(self.home)
  self.assertEqual((self.old/'spritesheet.webp').read_bytes(),b'previous-version');self.assertFalse((self.home/'pet-backups').exists())
 def test_replace_retains_backup_and_single_entry(self):
  self.old_version();installer.install(self.home,'replace');backups=list((self.home/'pet-backups').iterdir());self.assertEqual(len(backups),1);self.assertEqual((backups[0]/'spritesheet.webp').read_bytes(),b'previous-version');self.assertEqual(len(list((self.home/'pets').iterdir())),1)
 def test_keep_both_and_repeat_are_idempotent(self):
  self.old_version();new=installer.install(self.home,'keep-both');self.assertNotEqual(new,self.old);self.assertEqual((self.old/'spritesheet.webp').read_bytes(),b'previous-version');self.assertEqual(json.loads((new/'pet.json').read_text())['id'],new.name);installer.install(self.home,'keep-both');self.assertEqual(len(list((self.home/'pets').iterdir())),2)
 def test_cancel_keeps_old(self):
  self.old_version()
  with patch.object(installer.sys.stdin,'isatty',return_value=True),patch('builtins.input',return_value='cancel'):self.assertIsNone(installer.install(self.home))
  self.assertEqual((self.old/'spritesheet.webp').read_bytes(),b'previous-version')
 def test_failed_commit_rolls_back(self):
  self.old_version();original=Path.rename
  def fail_staged(p,d):
   if p.name.startswith('.yuexinmiao-'):raise OSError('simulated commit failure')
   return original(p,d)
  with patch.object(Path,'rename',fail_staged),self.assertRaises(OSError):installer.install(self.home,'replace')
  self.assertEqual((self.old/'spritesheet.webp').read_bytes(),b'previous-version');self.assertEqual(len(list((self.home/'pets').iterdir())),1)

if __name__=='__main__':
 with contextlib.redirect_stdout(io.StringIO()):unittest.main()
