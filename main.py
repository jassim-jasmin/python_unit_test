from py_unit_test.py_unit_test import UnitTest

unit_test = UnitTest("unit_test")


@unit_test.test
def function_test(test_argument: str, arg2=None, arg3='constant value'):
    print("test_argument: str, arg2=None, arg3", test_argument, arg2, arg3)

    return "pass1", "pass2"

function_test('ha', 'haha', 'hahaha')
function_test('first', 'second', 'third')
# sum_it(1,2)