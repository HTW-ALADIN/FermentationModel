from .base_input_adapter import InputAdapter
import pandas as pd
import json

class FileInputAdapter(InputAdapter):
    def transform_data(self, file_path: str) -> pd.DataFrame:
        input_df = None
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
            input_df = pd.DataFrame(data)
        except json.JSONDecodeError as error:
            print("Invalid JSON input.")
            print(error)
            raise
        except FileNotFoundError as error:
            print("Invalid file path.")
            print(error)
            raise
        return input_df