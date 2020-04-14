import unittest


class TestFindVersion(unittest.TestCase):
    def test_versionSystem(self):
        pythonVersion_system = 3
        pythonVersion_web = 3.2

        if self.assertEqual(pythonVersion_system, pythonVersion_web):
            return True
        else:
            return False
