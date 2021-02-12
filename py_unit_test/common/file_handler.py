import json
from pathlib import Path


class FileHandler:
    def __init__(self, test_case_file_name, dir_name):
        self.test_case_file_name = test_case_file_name
        self.dir_name = dir_name
        self.path_complete = "/".join([self.dir_name, self.test_case_file_name])

    @staticmethod
    def save_json(path, data):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def create_dir(path: str):
        Path(path).mkdir(parents=True, exist_ok=True)

    def save_file(self, data):
        try:
            self.save_json(self.path_complete, data)

        except FileNotFoundError:
            print("dir handling")

            if self.path_complete:
                self.create_dir(self.dir_name)
                self.save_json(self.path_complete, data)

        except Exception as e:
            print(f"error in FileHandler.save_file(): {str(e)}")

    def read_json(self):
        try:
            with open(self.path_complete) as f:
                data = json.load(f)

                return data

        except Exception as e:
            print(f"error in read_json(): {str(e)}")
