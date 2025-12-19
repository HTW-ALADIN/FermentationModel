from .base_output_adapter import OutputAdapter
from typing import ClassVar
import pandas as pd


class DFAdapter(OutputAdapter):
    __qualname__: ClassVar[str] = "df"

    def transform_data(self, df: pd.DataFrame) -> pd.DataFrame:
        return df
