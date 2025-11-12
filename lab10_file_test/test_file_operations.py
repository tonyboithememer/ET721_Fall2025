"""
Antonios Takos
Oct 15, 2025
lab 10, unittest for file operations
"""

import unittest
import os
from file_operations import read_file, write_file, append_file


class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # set up temporary test file name before each test.
        self.filename = "test_file.txt"
        self.msg = "Antonios Takos"

    def tearDown(self):
        # remove the test file after each test
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_write_file(self):
        # test writing text to a file
        msg = "Antonios Takos"
        with open(self.filename, "w") as f:
            f.write(msg)

        # verify file exists and content matches
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, "r") as f:
            result = f.read()

        self.assertEqual(result, msg)

    def test_read_file(self):
        # test reading text from a file
        expected_content = "Read me!"
        with open(self.filename, "w") as f:
            f.write(expected_content)

            with open(self.filename, "r") as f:
                data = f.read()

            self.assertEqual(data, expected_content)

        def test_append_file(self):
            # test appending test to an existing file
            inital_content = "Line one"
            append_content = "\nLine two"

            with open(self.filename, "w") as f:
                f.write(inital_content)

            with open(self.filename, "a") as f:
                f.write(append_content)

            with open(self.filename, "r") as f:
                final_data = f.read()

            self.assertEqual(final_data, inital_content + append_content)

    # LAB EXERCISE
    def test_email_read(self):
        expected_content = "Nick Carter, ncarter@yahoo.com\nVanessa Singh, vsingh@gmail.com\nAnn Parker, aparker@gmail.com\nPhil Chen, pchen@hotmail.com\nFiona Smith, fsmith@gmail.com\nJoshue Candela, jcandela@yahoo.com\nCarl Peterson, cpeterson@hotmail.com\nKevin Brook, kbrook@gmail.com \nTheresa Ng, tng@hotmail.com\nJoe Hunter, jhunter@yahoo.com\nPatricia Franco, pfranco@gmail.com\nMarie Mansion, mmansion@gmail.com\nCarla Lee, clee@hotmail.com"
        with open(self.filename, "w") as f:
            f.write(expected_content)

        with open(self.filename, "r") as f:
            data = f.read()

        self.assertEqual(data, expected_content)


# run the unit tests automatically when the file is run
if __name__ == "__main__":
    unittest.main()
