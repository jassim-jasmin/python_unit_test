from .input_handler import FileHandler
from ..common.module_data_handler import ModuleDataHandler


class TestCaseHandler(FileHandler, ModuleDataHandler):
    def __init__(self, test_case_file_name, dir_name):
        FileHandler.__init__(self, "mismatch_" + test_case_file_name, dir_name)

    def apply_test_case(self, function: object, test_case: dir, function_name):
        try:
            if function and test_case:
                input = test_case["input"]
                output = test_case["output"]
                missmatch = []

                for each_input, each_output in zip(input, output):
                    result = self.evaluate_function_from_input(function, each_input)
                    print(result)

                    if isinstance(each_output, tuple):
                        each_output = list(each_output)

                    if isinstance(result, tuple):
                        list_result = list(result)

                    if list_result != each_output:
                        missmatch.append({
                            "input": each_input,
                            "output": each_output,
                            "result": result
                        })

                self.save_file({function_name: missmatch})


        except Exception as e:
            print(f"error in apply_test_case(): {str(e)}")
