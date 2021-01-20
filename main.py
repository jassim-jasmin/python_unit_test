import inspect
from common.file_handler import FileHandler
from py_unit_test import decorator_function

"""
    file(__module__)
    {
        function_name(__name__):
        {
            input: 
                {
                    arg1:value,
                    ...
                }
        }
    }
        
"""
@decorator_function
def function_test(test_argument: str, arg2=None, arg3='constant value'):
    print("test_argument: str, arg2=None, arg3", test_argument, arg2, arg3)

    return "pass1", "pass2"

@decorator_function
def sum_it(a: int, b: int):
    return a+b

print("starting")
# param = inspect.getfullargspec(function_test)
# print(param.args)
# FileHandler.save_file(FileHandler, 'test_json_file', {"test":"test"}, "test_file/inner_file")
function_test('ha', 'haha', 'hahaha')
sum_it(1,2)
# print('module', function_test.__module__)
# print('name', function_test.__name__)