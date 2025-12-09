import sys
import json
import pandas as pd
from calculation import calculate
from Util.base_io_adapter import IOAdapter
from OutputAdapter.chart_js_adapter import ChartJSAdapter
from InputAdapter.std_in_adapter import STDINAdapter
from typing import Tuple

def main() -> Tuple[pd.DataFrame, IOAdapter]:
    """
    TODO: Add selection logic (cli-parameters) to select InputAdapter if required.
    Default is STDINAdapter
    """
    input_adapter = STDINAdapter()

    if len(sys.argv) < 2:
        print("Usage: python script.py '{\"key\": \"value\"}'")
        sys.exit(1)

    arg = json.loads(sys.argv[1])
    input_df = input_adapter.transform_data(arg)

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
    sys.exit(0)