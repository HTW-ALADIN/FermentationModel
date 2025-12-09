from .base_input_adapter import InputAdapter
import sys
import pandas as pd
import json

class STDINAdapter(InputAdapter):
    def transform_data(self, data: str) -> pd.DataFrame:
        try:
            input_df = pd.DataFrame(data)
        except json.JSONDecodeError as error:
            print("Invalid JSON input.")
            print(error)
            sys.exit(1)
        return input_df