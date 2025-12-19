from .base_output_adapter import OutputAdapter
import pandas as pd

from typing import Any, ClassVar


class KatzbergAdapter(OutputAdapter):
    __qualname__: ClassVar[str] = "katzberg"

    def transform_data(self, df: pd.DataFrame) -> Any:
        # TODO: transform the df into the appropriate diagrams (e.g. see example-data below)
        # Dataframe structure:
        # results_columns=["t","c_x","c_S1","c_S2","c_P","c_DO","c_O2_Out","c_CO2_Out","Sum_Feed","Begasungsrate","Drehzahl","Druck","OUR","CER","RQ","c_DO_proz","V_L"]
        # print(df.iloc[0])
        Drehzahl = df["Drehzahl"] / 10
        diagramData = {
            "t": df["t"].to_list(),
            "c_x": df["c_x"].to_list(),
            "c_S1": df["c_S1"].to_list(),
            "c_S2": df["c_S2"].to_list(),
            "c_P": df["c_P"].to_list(),
            "c_DO": df["c_S1"].to_list(),
            "Sum_Feed": df["Sum_Feed"].to_list(),
            "Q_Air": df["Begasungsrate"].to_list(),
            "Drehzahl": Drehzahl.to_list(),
            "Druck": df["Druck"].to_list(),
            "OUR": df["OUR"].to_list(),
            "RQ": df["RQ"].to_list(),
            "V": df["V_L"].to_list(),
        }
        return diagramData
