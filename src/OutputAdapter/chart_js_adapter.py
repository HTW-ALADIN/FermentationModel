from .base_output_adapter import OutputAdapter
import pandas as pd

from typing import Generic, TypeVar, ClassVar

# Type variables representing the generic TS parameters
TType = TypeVar("TType")  # corresponds to ChartType
TData = TypeVar("TData")  # corresponds to DefaultDataPoint<TType>
TLabel = TypeVar("TLabel")  # corresponds to unknown


# Stub for ChartDataset<TType, TData>
class ChartDataset(Generic[TType, TData]):
    pass


class ChartJSAdapter(OutputAdapter):
    __qualname__: ClassVar[str] = "chart"

    def transform_data(self, df: pd.DataFrame) -> ChartDataset:
        # TODO: transform the df into the appropriate diagrams (e.g. see example-data below)
        # Dataframe structure:
        # results_columns=["t","c_x","c_S1","c_S2","c_P","c_DO","c_O2_Out","c_CO2_Out","Sum_Feed","Begasungsrate","Drehzahl","Druck","OUR","CER","RQ","c_DO_proz","V_L"]
        # print(df.iloc[0])

        diagramData = {
            "type": "line",
            "diagram1": {
                "datasets": [
                    {
                        "label": "Substratkonzentration",
                        "data": df["c_S1"].to_list(),
                        "borderColor": "#66c2a5",
                        "backgroundColor": "#66c2a5",
                        "tension": 0.1,
                    }
                ],
                "labels": ["a", "b"],
            },
            "diagram2": {
                "type": "line",
                "datasets": [
                    {
                        "label": "Produkte und Volumen",
                        "data": [20, 10],
                        "borderColor": "#66c2a5",
                        "backgroundColor": "#66c2a5",
                        "tension": 0.1,
                    }
                ],
                "labels": ["a", "b"],
            },
            "diagram3": {
                "type": "line",
                "datasets": [
                    {
                        "label": "Belüftungsbezogene Größen",
                        "data": [20, 10],
                        "borderColor": "#66c2a5",
                        "backgroundColor": "#66c2a5",
                        "tension": 0.1,
                    }
                ],
                "labels": ["a", "b"],
            },
            "diagram4": {
                "type": "line",
                "datasets": [
                    {
                        "label": "Abgasanalyse",
                        "data": [20, 10],
                        "borderColor": "#66c2a5",
                        "backgroundColor": "#66c2a5",
                        "tension": 0.1,
                    }
                ],
                "labels": ["a", "b"],
            },
        }
        return diagramData
