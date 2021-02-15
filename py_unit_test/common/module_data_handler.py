class ModuleDataHandler:
    @staticmethod
    def create_json_from_list(key: list, value: list):
        parameters = dict()

        if len(key) == len(value):
            for each_param, each_value in zip(key, value):
                parameters[each_param] = each_value

        return parameters

    @staticmethod
    def build_parameter_for_function(parameter: list) -> str:
        parameter_as_string = ''

        for each_param in parameter:
            if isinstance(each_param, int):
                parameter_as_string += str(each_param) + ","

            else:
                parameter_as_string += f"'{each_param}'" + ","

        parameter_as_string = parameter_as_string.lstrip(",")

        return parameter_as_string

    def evaluate_function_from_input(self, function: str, parameter: list):
        if function:
            if parameter_as_string := self.build_parameter_for_function(parameter):
                return eval(f"function({parameter_as_string})")
