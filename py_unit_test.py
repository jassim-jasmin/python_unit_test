import inspect
# from common.file_handler import FileHandler
from helper.input_handler import InputHandler
from helper.test_case_handler import TestCaseHandler
import os
import ntpath
import sys


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def get_current_executing_file_name() -> str:
    current_executing_file_path = sys.argv[0]
    file_name = path_leaf(current_executing_file_path).split(".")[0]

    return file_name


class Unit:
    def __init__(self, dir_name: str = "test"):
        self.dir_name = dir_name

    def test(self, func):
        function_name = func.__name__
        module_name = func.__module__
        file_name = get_current_executing_file_name()
        test_case_file_name = f"test_{file_name}_{function_name}.json"
        input_handler = InputHandler(file_name=file_name, dir_name=self.dir_name, module_name=module_name,
                                     function_name=function_name, test_case_file_name=test_case_file_name)
        test_case_handler = TestCaseHandler(test_case_file_name, self.dir_name)

        def inner(*arg):
            try:
                p = inspect.getfullargspec(func)
                argument_variables = p.args
                argument_values = arg
                input_handler.register_test_case(argument_variables, argument_values, func)
                # from_data = test_case_handler.get_test_case(module_name, function_name)
                test_case_handler.apply_test_case(module_name, function_name, func)

                # func(arg)

            except Exception as e:
                print(f"error in inner(): {str(e)}")
                return func

        return inner
