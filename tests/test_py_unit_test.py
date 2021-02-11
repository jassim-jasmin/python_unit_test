from unittest import TestCase
import shutil

from py_unit_test import Unit


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
