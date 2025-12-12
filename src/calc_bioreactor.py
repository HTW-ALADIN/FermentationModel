import pandas as pd
import json
from .DataModels.input_definition import InputKeys

MODEL_PATH = "./src/Model/model_db.json"

def calculate(df: pd.DataFrame) -> pd.DataFrame:
    try:
        model_name = df[InputKeys.model][0]
        with open(MODEL_PATH) as f:
            model = json.load(f)
            model = model[model_name]
        
    except json.JSONDecodeError:
        print("Invalid JSON input.")
        pass

    result_df = pd.DataFrame([])

    # nebenberechnung
    # vorberechnung

    # nachfolgend Hauptberechnung
    for index, row in df.iterrows():
        # result_df hier befüllen
        pass

    return result_df