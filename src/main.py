import sys
import json
import pandas as pd

from calc_bioreactor import calculate
from multiplot_ferm import multiplot_ferm
from Util.base_io_adapter import IOAdapter
from OutputAdapter.output_adapter_strategy import output_adapter_strategy
from InputAdapter.input_adapter_strategy import input_adapter_strategy
from typing import Tuple
from Util.arg_parser import parser


def main() -> Tuple[pd.DataFrame, IOAdapter]:
    """
    TODO: Add selection logic (cli-parameters) to select InputAdapter if required.
    Default is STDINAdapter
    """
    args = parser.parse_args()
    print(args)

    input_adapter = input_adapter_strategy.select_strategy(args.input_type)

    input_df = input_adapter.transform_data(args.parameters)
    """
    TODO: Selection logic (cli-parameters) to select OutputAdapter if required.
    Default is ChartJSAdapter
    """
    output_adapter = output_adapter_strategy.select_strategy(args.output_type)

    return input_df, output_adapter


if __name__ == "__main__":
    [input_df, output_adapter] = main()
    result_df = calculate(input_df)

    output = output_adapter.transform_data(result_df)
    # print(output)
    # sys.stdout.write(json.dumps(output))
    with open("output.json", "w") as f:
        json.dump(output, f)
    multiplot_ferm(result_df)
    sys.exit(0)
