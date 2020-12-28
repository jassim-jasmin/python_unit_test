import inspect
# from common.file_handler import FileHandler
from helper.input_handler import InputHandler


def decorator_function(func):
    function_name = func.__name__
    module_name = func.__module__
    # FileHandler.save_file(FileHandler, f"test_{module_name}", {function_name: {}}, "test")

    def inner(*arg):
        input_handler = InputHandler()
        p = inspect.getfullargspec(func)
        input_handler.register_parameter(p.args, arg, module_name, function_name)

        return func

    return inner
