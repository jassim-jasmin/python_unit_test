import json
from pathlib import Path


class FileHandler:
    def __init__(self):
        self.path_complete = None

    @staticmethod
    def save_json(path, data):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def create_dir(path: str):
        Path(path).mkdir(parents=True, exist_ok=True)

    def save_file(self, file_name: str, data, path: str="test"):
        try:
            if path:
                t_path = "/".join([path, file_name])

            else:
                t_path = file_name

            self.path_complete = f"{t_path}.json"

            self.save_json(self.path_complete, data)

        except FileNotFoundError:
            print("dir handling")
            if path and self.path_complete:
                self.create_dir(path)
                self.save_json(self.path_complete, data)

        except Exception as e:
            print(f"error in FileHandler.save_file(): {str(e)}")

    def read_json(self, file_name: str, path: str = "test"):
        try:
            if path:
                t_path = "/".join([path, file_name])

            else:
                t_path = file_name

            self.path_complete = f"{t_path}.json"

            with open(self.path_complete) as f:
                data = json.load(f)

                return data

        except Exception as e:
            print(f"error in read_json(): {str(e)}")
