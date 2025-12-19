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
import logging
import os

logging.basicConfig(level=os.environ.get("LOG_LEVEL") or logging.INFO)


def main() -> Tuple[pd.DataFrame, IOAdapter]:
    args = parser.parse_args()

    input_adapter = input_adapter_strategy.select_strategy(args.input_type)

    input_df = input_adapter.transform_data(args.parameters)
    output_adapter = output_adapter_strategy.select_strategy(args.output_type)

    return input_df, output_adapter


if __name__ == "__main__":
    [input_df, output_adapter] = main()
    result_df = calculate(input_df)

    output = output_adapter.transform_data(result_df)

    # TODO: explizite Dateiausgabe zurückbauen
    with open("output.json", "w") as f:
        json.dump(output, f)
    multiplot_ferm(result_df)
    sys.exit(0)
