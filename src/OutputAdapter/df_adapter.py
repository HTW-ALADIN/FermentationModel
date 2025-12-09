from .base_output_adapter import OutputAdapter
import pandas as pd


class DFAdapter(OutputAdapter):
    def transform_data(self, df: pd.DataFrame) -> pd.DataFrame:
        return df