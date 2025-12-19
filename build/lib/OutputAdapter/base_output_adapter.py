from Util.base_io_adapter import IOAdapter, unknown
from abc import abstractmethod
import pandas as pd

class OutputAdapter(IOAdapter):
    @abstractmethod
    def transform_data(self, data: pd.DataFrame) -> unknown:
        return