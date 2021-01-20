from .input_handler import FileHandler


class TestCaseHandler(FileHandler):
    def get_test_case(self, module_name: str, function_name, path: str = "test"):
        try:
            file_name = f"test_{module_name}"
            data = self.read_json(file_name, path)

            if function_name in data:
                test_case = data[function_name]

                return test_case

        except Exception as e:
            print(f"error in get_test_case(): {str(e)}", module_name, function_name)

    def apply_test_case(self, module_name: str, function_name: str, function: object):
        try:
            if test_case := self.get_test_case(module_name, function_name):
                print(test_case)
                input_param = tuple(test_case['input'])
                # function(input_param)
                print(input_param)

        except Exception as e:
            print(f"error in apply_test_case(): {str(e)}", module_name, function_name)
