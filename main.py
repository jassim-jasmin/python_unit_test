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
    pass


# param = inspect.getfullargspec(function_test)
# print(param.args)
# FileHandler.save_file(FileHandler, 'test_json_file', {"test":"test"}, "test_file/inner_file")
function_test('ha', 'haha', 'hahaha')
# print('module', function_test.__module__)
# print('name', function_test.__name__)