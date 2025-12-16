import sys
import json
import pandas as pd

from calc_bioreactor import calculate
from multiplot_ferm import multiplot_ferm
from Util.base_io_adapter import IOAdapter
from OutputAdapter.chart_js_adapter import ChartJSAdapter
from InputAdapter.file_input_adapter import FileInputAdapter
from typing import Tuple


def main() -> Tuple[pd.DataFrame, IOAdapter]:
    """
    TODO: Add selection logic (cli-parameters) to select InputAdapter if required.
    Default is STDINAdapter
    """
    input_adapter = FileInputAdapter()

    if len(sys.argv) < 2:
        print('Usage: python script.py \'{"key": "value"}\'')
        sys.exit(1)

    arg = sys.argv[1]
    input_df = input_adapter.transform_data(arg)
    print(input_df)
    """
    TODO: Selection logic (cli-parameters) to select OutputAdapter if required.
    Default is ChartJSAdapter
    """
    output_adapter = ChartJSAdapter()

    return input_df, output_adapter


if __name__ == "__main__":
    [input_df, output_adapter] = main()
    result_df = calculate(input_df)

    output = output_adapter.transform_data(result_df)

    sys.stdout.write(json.dumps(output))
    multiplot_ferm(result_df)    
    sys.exit(0)
