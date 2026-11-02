"""隔离验证检查入口的成功与拒绝路径 / Isolated checker acceptance tests."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

CHECKER = Path(__file__).resolve().parents[1] / 'scripts/check-safeguards.py'
SUITES = ('test_install_security.py', 'test_install_updates.py')
PASSING = '''import unittest
class Sample(unittest.TestCase):
    def test_one(self):
        self.assertTrue(True)
'''


class SafeguardsRunnerTests(unittest.TestCase):
    def run_checker(self, overrides=None):
        # Fixtures only: never execute an installer or write real client data.
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'scripts').mkdir()
            (root / 'tests').mkdir()
            shutil.copyfile(CHECKER, root / 'scripts/check-safeguards.py')
            for name in SUITES:
                content = (overrides or {}).get(name, PASSING)
                if content is not None:
                    (root / 'tests' / name).write_text(content, encoding='utf-8')
            return subprocess.run(
                [sys.executable, str(root / 'scripts/check-safeguards.py')],
                cwd=root, capture_output=True, text=True, encoding='utf-8',
                env={**os.environ, 'PYTHONUTF8': '1'},
                timeout=30, check=False,
            )

    def assert_rejected(self, content, diagnostic):
        for name in SUITES:
            with self.subTest(suite=name):
                result = self.run_checker({name: content})
                self.assertNotEqual(result.returncode, 0, result.stderr)
                self.assertIn(diagnostic, result.stderr)
                self.assertIn(f'Summary: {SUITES[1 - SUITES.index(name)]}', result.stderr)

    def test_success_uses_actual_counts_without_a_fixed_total(self):
        two_tests = PASSING + '    def test_two(self):\n        self.assertEqual(1, 1)\n'
        result = self.run_checker({SUITES[1]: two_tests})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f'{SUITES[0]}: discovered=1, executed=1, skipped=0', result.stderr)
        self.assertIn(f'{SUITES[1]}: discovered=2, executed=2, skipped=0', result.stderr)

    def test_missing_either_file_fails(self):
        self.assert_rejected(None, 'Missing required test file')

    def test_empty_either_file_fails(self):
        self.assert_rejected('import unittest\n', 'No executed tests')

    def test_all_cases_skipped_in_either_group_fails(self):
        skipped = PASSING.replace('    def test_one',
                                 "    @unittest.skip('fixture skip')\n    def test_one")
        self.assert_rejected(skipped, 'No executed tests')

    def test_class_skip_in_either_group_fails(self):
        skipped = PASSING.replace('class Sample',
                                 "@unittest.skip('fixture class skip')\nclass Sample")
        self.assert_rejected(skipped, 'No executed tests')

    def test_assertion_failure_in_either_group_fails(self):
        self.assert_rejected(PASSING.replace('assertTrue(True)', 'assertTrue(False)'),
                             'AssertionError')

    def test_import_failure_in_either_group_fails(self):
        self.assert_rejected('raise RuntimeError("fixture import failure")\n',
                             'fixture import failure')

    def test_partial_skips_are_visible_and_allow_executed_cases(self):
        partial = PASSING + '''    @unittest.skip('fixture partial skip')
    def test_skipped(self):
        self.fail('must be skipped')
'''
        for name in SUITES:
            with self.subTest(suite=name):
                result = self.run_checker({name: partial})
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn('fixture partial skip', result.stderr)
                self.assertIn(f'{name}: discovered=2, executed=1, skipped=1', result.stderr)

    def test_skipped_subtest_does_not_hide_executed_parent(self):
        subtest = '''import unittest
class Sample(unittest.TestCase):
    def test_subtests(self):
        with self.subTest(case='skip'):
            self.skipTest('fixture subtest skip')
        with self.subTest(case='execute'):
            self.assertTrue(True)
'''
        result = self.run_checker({SUITES[0]: subtest})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('fixture subtest skip', result.stderr)
        self.assertIn(f'{SUITES[0]}: discovered=1, executed=1, skipped=1', result.stderr)

    def test_all_subtests_skipped_in_either_group_fails(self):
        subtests = '''import unittest
class Sample(unittest.TestCase):
    def test_variants(self):
        for n in (1, 2):
            with self.subTest(n=n):
                self.skipTest('no variant ran')
'''
        self.assert_rejected(subtests, 'No executed tests')
        for name in SUITES:
            with self.subTest(suite=name):
                result = self.run_checker({name: subtests})
                self.assertIn(f'{name}: discovered=1, executed=0, skipped=2', result.stderr)


if __name__ == '__main__':
    unittest.main()
