import pytest

class TestCollector:
    def __init__(self):
        self.passed = []
        self.failed = []

    def pytest_runtest_logreport(self, report):
        if report.when == 'call' and report.passed:
            self.passed.append(report.node)
        elif report.when == 'teardown' and report.failed:
            self.failed.append(report.node)

