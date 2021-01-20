from common.file_handler import FileHandler
from common.module_data_handler import ModuleDataHandler


class InputHandler(FileHandler, ModuleDataHandler):
    def register_parameter(self, parameter, values, module_name, function_name):
        try:
            param_json = self.create_json_from_list(parameter, values)

            if param_json:
                test_case = {function_name: {"input": param_json}}
                self.save_file(f"test_{module_name}", test_case)

        except Exception as e:
            print(f"error in register_parameter(): {str(e)}",
                  parameter, values, module_name, function_name)

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

    def register_test_case(self, parameter, values, module_name, function_name, function: object):
        try:
            param_json = self.create_json_from_list(parameter, values)

            if param_json:
                file_name = f"test_{module_name}"
                function_data = dict()

                if json_data := self.read_json(file_name):
                    if function_name in json_data:
                        function_data = json_data[function_name]

                else:
                    json_data = dict()

                if input_case := self.build_input_case(param_json, function_data):
                    parameter_as_string = ''

                    for each_param in values:
                        if isinstance(each_param, int):
                            parameter_as_string += str(each_param) + ","

                        else:
                            parameter_as_string += f"'{each_param}'" + ","

                    parameter_as_string = parameter_as_string.lstrip(",")

                    result = eval(f"function({parameter_as_string})")
                    # result = function(values)

                    if "output" in function_data:
                        function_result = function_data["output"]

                    else:
                        function_result = []

                    function_result.append(result)

                    print("New values found", input_case)
                    data = {"input": input_case, "output": function_result}
                    json_data[function_name] = data
                    self.save_file(file_name,json_data)

                else:
                    print("values already exist")

        except Exception as e:
            print(f"error in register_test_case(): {str(e)}", parameter, values, module_name, function_name)