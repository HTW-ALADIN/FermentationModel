from .base_output_adapter import OutputAdapter
import pandas as pd

from typing import Generic, List, Optional, TypeVar

# Type variables representing the generic TS parameters
TType = TypeVar("TType")   # corresponds to ChartType
TData = TypeVar("TData")   # corresponds to DefaultDataPoint<TType>
TLabel = TypeVar("TLabel") # corresponds to unknown

# Stub for ChartDataset<TType, TData>
class ChartDataset(Generic[TType, TData]):
    # The real class could include many Chart.js fields.
    # This is just a placeholder to satisfy typing.
    pass


class ChartJSAdapter(OutputAdapter):
    def transform_data(self, df: pd.DataFrame) -> str:
        diagramData = {
            "type": 'bar',
            "diagram1": {
                "datasets": [{
                    "label": "cₓ",
                    "data": [1,2],
                    "borderColor": "#66c2a5",
                    "backgroundColor": "#66c2a5",
                    "tension": 0.1
                }],
                "labels": ['a', 'b']
            },
            "diagram2": {
                "datasets": [{
                    "label": "cₓ",
                    "data": [20, 10],
                    "borderColor": "#66c2a5",
                    "backgroundColor": "#66c2a5",
                    "tension": 0.1
                }],
                "labels": ['a', 'b']
            },
            "diagram3": {
                "datasets": [{
                    "label": "cₓ",
                    "data": [20, 10],
                    "borderColor": "#66c2a5",
                    "backgroundColor": "#66c2a5",
                    "tension": 0.1
                }],
                "labels": ['a', 'b']
            },
            "diagram4": {
                "datasets": [{
                    "label": "cₓ",
                    "data": [20, 10],
                    "borderColor": "#66c2a5",
                    "backgroundColor": "#66c2a5",
                    "tension": 0.1
                }],
                "labels": ['a', 'b']
            }
        }
        return diagramData