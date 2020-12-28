class ModuleDataHandler:
    def create_json_from_list(self, key: list, value: list):
        parameters = dict()

        if len(key) == len(value):
            for each_param, each_value in zip(key, value):
                parameters[each_param] = each_value

        return parameters