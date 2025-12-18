import pandas as pd
import numpy as np
    
#CONVERT EXCEL DATA into JSON Files
Excel_file="./Bioreaktor_forPy.xlsx"
#read Experiment parameters (exp_par) from Excel file
exp_par = pd.read_excel(Excel_file, sheet_name="Input_Array", skiprows=2, nrows=4,header=0, usecols="A:Q")
model_db=pd.read_excel(Excel_file, sheet_name="Input_Array", skiprows=37, nrows=4,header=0, usecols="A:AA")
# Save input data and models as Json file
orientation="records"
exp_par.to_json('./test/test_data/user_input.json', orient=orientation)
model_db.to_json('./src/DataModels/model_db.json', orient=orientation)