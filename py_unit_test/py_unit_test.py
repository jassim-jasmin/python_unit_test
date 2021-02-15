import inspect
import ntpath
import sys
import argparse

from py_unit_test.helper.input_handler import InputHandler
from py_unit_test.helper.test_case_handler import TestCaseHandler


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def get_current_executing_file_name() -> str:
    current_executing_file_path = sys.argv[0]
    file_name = path_leaf(current_executing_file_path).split(".")[0]

    return file_name


class UnitTest:
    unit_test = False

    @classmethod
    def arg_handler(cls, arg: list = None):
        """
        For parsing command line argument
        :param arg: Unit test uses this variable for argparse value
        :return:
        """
        test_message = """
        Record evey input and store as json, results for every input will be saved.
        Later evaluate each input and record not matching output
        """
        # Create the parser
        my_parser = argparse.ArgumentParser(description='Unit test handler module')

        # Add the arguments
        my_parser.add_argument('-test', '--unit_test', action='store_true', help=test_message)

        if arg:
            args = my_parser.parse_args(arg)

        else:
            args = my_parser.parse_args()

        if args.unit_test:
            cls.unit_test = True

    def __init__(self, dir_name: str = "test"):
        self.dir_name = dir_name
        self.arg_handler()

    def test(self, func):
        if self.unit_test:
            function_name = func.__name__
            module_name = func.__module__
            test_case_file_name = f"test_{module_name}_{function_name}.json"
            input_handler = InputHandler(dir_name=self.dir_name, module_name=module_name, function_name=function_name,
                                         test_case_file_name=test_case_file_name)
            test_case_handler = TestCaseHandler(test_case_file_name, self.dir_name)

            def inner(*arg):
                try:
                    p = inspect.getfullargspec(func)
                    argument_variables = p.args
                    argument_values = arg

                    if result := input_handler.register_test_case(argument_variables, argument_values, func):
                        test_case_handler.apply_test_case(func, result, function_name)

                except Exception as e:
                    print(f"error in inner(): {str(e)}")
                    return func

            return inner

        else:
            return func
