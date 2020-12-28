from common.file_handler import FileHandler
from common.module_data_handler import ModuleDataHandler


class InputHandler(FileHandler, ModuleDataHandler):
    def register_parameter(self, parameter, values, module_name, function_name):
        param_json = self.create_json_from_list(parameter, values)

        if param_json:
            self.save_file(f"test_{module_name}", {function_name: {"input": param_json}})