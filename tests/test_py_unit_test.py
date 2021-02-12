"""
1. Test directory will be for_unit_test as name
2. Test case saved in the directory for_unit_test
3. Check the result with unit test result
4. Delete the test directory in tearDown method function
"""

from unittest import TestCase
import shutil

from py_unit_test import Unit
from common.file_handler import FileHandler


class Test(TestCase):
    test_dir_name = "for_unit_test"

    def tearDown(self) -> None:
        shutil.rmtree(self.test_dir_name)

    def test_py_unit_test_handler(self):
        unit_test = Unit(self.test_dir_name)

        @unit_test.test
        def sample_function(param):
            return None

        sample_function('test values')
        expected_result = {
                    "input": [
                        {
                            "param": "test values"
                        }
                    ],
                    "output": [
                        None
                    ]
                }
        file_handler = FileHandler(test_case_file_name="test_test_py_unit_test_sample_function.json",
                                   dir_name=self.test_dir_name)
        result = file_handler.read_json()

        if result:
            self.assertDictEqual(expected_result, dict(result))

        else:
            self.assertFalse("no data generated")