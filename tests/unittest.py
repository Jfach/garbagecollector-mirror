import os
import unittest
import pep8


class TestPep8(unittest.TestCase):
    def test_conformance(self):
        paths = [os.curdir]
        checker = pep8.StyleGuide(paths=paths, reporter=pep8.StandardReport)
        report = checker.check_files()
        result = report.total_errors
        output = "\n".join(report.get_statistics())
        if result != 0:
            self.fail("Found PEP8 errors:\n%s" % output)
    
