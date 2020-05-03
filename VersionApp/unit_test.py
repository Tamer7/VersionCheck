import unittest
from program import FindVersion
from Validator import Validator


class TestFindVersion(unittest.TestCase):
    def test_versionSystem_same_value(self):
        pythonVersion_system = 3
        pythonVersion_web = 3
        self.assertEqual(pythonVersion_system, pythonVersion_web)

    # def test_versionSystem_wrong_value(self):
    #     pythonVersion_system = 3
    #     pythonVersion_web = "test"
    #     with self.assertRaises(TypeError) as err:
    #         self.assertEqual(pythonVersion_system, pythonVersion_web)

    def test_display_version(self):
        with self.assertRaises(TypeError):
            self.assertEqual(FindVersion.display_version(), True)
        with self.assertRaises(TypeError):
            self.assertEqual(FindVersion.display_version(""), True)

    def test_subscribe_wrong_input(self):
        input_test = "tamerjar"
        validator = Validator(input_test)
        is_valid = validator.check_for_symbol()

        self.assertEqual(is_valid, False)

    def test_subscribe_correct_input(self):
        input_test = "tamerjar@hotmail.com"
        validator = Validator(input_test)
        is_valid = validator.check_for_symbol()

        self.assertEqual(is_valid, True)

    def test_unsubscribe_wrong_input(self):
        input_test = "test"
        validator = Validator(input_test)
        is_valid = validator.check_for_symbol()

        self.assertEqual(is_valid, False)

    def test_unsubscribe_correct_input(self):
        input_test = "test@hotmail.com"
        validator = Validator(input_test)
        is_valid = validator.check_for_symbol()

        self.assertEqual(is_valid, True)

    def test_email_incorrect(self):
        with self.assertRaises(TypeError):
            res = FindVersion.email(42, 10)

    def test_email_correct(self):
        with self.assertRaises(TypeError):
            res = FindVersion.email("string", "string")


if __name__ == "__main__":
    unittest.main()
