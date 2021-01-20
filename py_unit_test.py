import inspect
# from common.file_handler import FileHandler
from helper.input_handler import InputHandler
from helper.test_case_handler import TestCaseHandler


def decorator_function(func):
    function_name = func.__name__
    module_name = func.__module__
    # FileHandler.save_file(FileHandler, f"test_{module_name}", {function_name: {}}, "test")

    def inner(*arg):
        try:
            input_handler = InputHandler()
            test_case_handler = TestCaseHandler()
            p = inspect.getfullargspec(func)
            input_handler.register_test_case(p.args, arg, module_name, function_name, func)
            # from_data = test_case_handler.get_test_case(module_name, function_name)
            test_case_handler.apply_test_case(module_name, function_name, func)

            # func(arg)

        except Exception as e:
            print(f"error in inner(): {str(e)}")
            return func

    return inner
