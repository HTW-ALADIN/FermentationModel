from .base_output_adapter import OutputAdapter
import pandas as pd

from typing import Generic, List, Optional, TypeVar

# Type variables representing the generic TS parameters
TType = TypeVar("TType")   # corresponds to ChartType
TData = TypeVar("TData")   # corresponds to DefaultDataPoint<TType>
TLabel = TypeVar("TLabel") # corresponds to unknown

# Stub for ChartDataset<TType, TData>
class ChartDataset(Generic[TType, TData]):
    pass


class ChartJSAdapter(OutputAdapter):
    def transform_data(self, df: pd.DataFrame) -> ChartDataset:
        # TODO: transform the df into the appropriate diagrams (e.g. see example-data below)
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
                "type": 'bar',
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
                "type": 'bar',
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
                "type": 'bar',
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