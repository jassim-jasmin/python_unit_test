from py_unit_test.common.file_handler import FileHandler
from py_unit_test.common.module_data_handler import ModuleDataHandler


class InputHandler(FileHandler, ModuleDataHandler):
    def __init__(self, dir_name: str, module_name: str, function_name: str,
                 test_case_file_name: str):
        self.module_name = module_name
        self.function_name=function_name
        FileHandler.__init__(self, test_case_file_name, dir_name)

    def register_parameter(self, parameter, values):
        try:
            param_json = self.create_json_from_list(parameter, values)

            if param_json:
                test_case = {self.function_name: {"input": param_json}}
                self.save_file(test_case)

        except Exception as e:
            print(f"error in register_parameter(): {str(e)}",
                  parameter, values, self.module_name, self.function_name)

    def build_input_case(self, param_json, function: dict):
        try:
            function_data = function.copy()

            if "input" in function_data:
                input_list = function_data["input"]

            else:
                input_list = []

            if param_json not in input_list:
                input_list.append(param_json)

                return input_list

        except Exception as e:
            print(f"Exception in build_input_case(): {str(e)}", param_json, function)

    def create_and_save_test_case(self, function, values, function_data, input_case):
        result = self.evaluate_function_from_input(function, values)

        if "output" in function_data:
            function_result = function_data["output"]

        else:
            function_result = []

        function_result.append(result)

        json_data = {"input": input_case, "output": function_result}
        self.save_file(json_data)

    def register_test_case(self, parameter, values, function):
        try:
            param_json = self.create_json_from_list(parameter, values)

            if param_json and function:
                function_data = dict()

                if json_data := self.read_json():
                    function_data = json_data

                if input_case := self.build_input_case(param_json, function_data):
                    self.create_and_save_test_case(function, values, function_data, input_case)

                else:
                    print("values already exist")

                return json_data

        except Exception as e:
            print(f"error in register_test_case(): {str(e)}", parameter, values, self.module_name, self.function_name)