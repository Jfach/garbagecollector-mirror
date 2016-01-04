import os
import pep8
from .unittest import TestFixture, REPO_DIR


class TestPep8(TestFixture):
    def setUp(self):
        TestFixture.setUp(self)
        
    def test_conformance(self):
        """
        Run PEP8 tests.
        """
        checker = pep8.StyleGuide(paths=[REPO_DIR], reporter=pep8.StandardReport)
        report = checker.check_files()
        result = report.total_errors
        output = "\n".join(report.get_statistics())
        if result != 0:
            self.fail("Found PEP8 errors:\n%s" % output)
   
