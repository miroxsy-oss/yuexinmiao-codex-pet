#!/usr/bin/env python3
"""离线运行安装防护测试 / Run offline installer safeguard tests."""
from pathlib import Path
import sys
import unittest

PROJECT = Path(__file__).resolve().parents[1]
REQUIRED_SUITES = ('test_install_security.py', 'test_install_updates.py')


class SafeguardResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.executed_ids = set()

    def addSuccess(self, test):
        self.executed_ids.add(test.id())
        super().addSuccess(test)

    def addSubTest(self, test, subtest, err):
        # Skipped subtests call addSkip instead. At least one real subtest
        # result is needed; merely entering its parent test is not enough.
        self.executed_ids.add(test.id())
        super().addSubTest(test, subtest, err)


def test_ids(suite):
    """Collect case IDs before unittest consumes the suite."""
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from test_ids(item)
        else:
            yield item.id()


def main():
    passed = True
    directory = PROJECT / 'tests'
    for name in REQUIRED_SUITES:
        print(f'安装防护测试组 / Safeguard suite: {name}', file=sys.stderr, flush=True)
        if not (directory / name).is_file():
            print(f'缺少必需测试文件 / Missing required test file: {name}', file=sys.stderr)
            passed = False
            continue
        suite = unittest.TestLoader().discover(str(directory), pattern=name)
        ids = set(test_ids(suite))
        discovered = suite.countTestCases()
        result = unittest.TextTestRunner(verbosity=2, resultclass=SafeguardResult).run(suite)
        executed_ids = result.executed_ids
        for test, _ in result.failures + result.errors + result.expectedFailures:
            executed_ids.add(test.id())
        executed_ids.update(test.id() for test in result.unexpectedSuccesses)
        executed = len(ids & executed_ids)
        print(f'汇总 / Summary: {name}: discovered={discovered}, '
              f'executed={executed}, skipped={len(result.skipped)}', file=sys.stderr)
        if not discovered or executed <= 0:
            print(f'没有实际执行的测试 / No executed tests: {name}', file=sys.stderr)
            passed = False
        if not result.wasSuccessful():
            passed = False
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
