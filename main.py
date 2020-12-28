import inspect

def function_test(test_argument: str, arg2=None, arg3='constant value'):
    pass

param = inspect.getfullargspec(function_test)
print(param.args)
