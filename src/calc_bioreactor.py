import pandas as pd
import json
import numpy as np
from scipy.integrate import solve_ivp #solve odes
from DataModels.input_definition import InputKeys
from DataModels.model_definition import ModelKeys
from Nebenrechnungen import Nebenrechnungen
from Fx_ODE_Bioreaktor import Bioreaktor_ODE #hier wird das Differentialgleichungssystem definiert

MODEL_PATH = "./src/DataModels/model_db.json"


def calculate(ferm_param_in_df: pd.DataFrame) -> pd.DataFrame:
    try:
        model_number = int(ferm_param_in_df[InputKeys.model][0]-1) #"-1" as indices start with 0 and model numbers start with 1
        print("Genutztes Model hat die Nummer: ", model_number+1)
        with open(MODEL_PATH) as f:
            model = json.load(f)
            model_param_in= model[model_number] #dictionary
            #print (model_param_in[ModelKeys.YPS1])

    except json.JSONDecodeError:
        print("Invalid JSON input.")
        pass

    # Nebenberechnung
    [model_param,ferm_param_df]=Nebenrechnungen(model_param_in,ferm_param_in_df)
    
    #global constants
    data_rate=60 #data rate per hour
    Vm_norm=22.41396954 #molares Volumen in NL/mol bei Normbedingungen (0°C und 101,325 kPa) 
    c_O2_Luft = 0.2095      #Sauerstoffgehalt Luft in mol(O2)/mol(Luft)
    c_CO2_Luft =0.0004147    #CO2 Gehalt der Luft in mol(CO2)/mol(Luft)
    
    
    # nachfolgend Hauptberechnung
    for index, row in ferm_param_df.iterrows():
        # result_df hier befüllen
        print("Phase:", row[InputKeys.phase])
        
        if index==0:
            c_x_0=row[InputKeys.c_x0]
            c_S1_0=row[InputKeys.bolus_c]
            c_S2_0=row[InputKeys.bolus_n]
            c_P_0=0
            c_DO_0=row[InputKeys.c_o2_sat]*row[InputKeys.do]/100
        
            y0=[c_x_0,c_S1_0,c_S2_0, c_P_0, c_DO_0, c_O2_Luft, c_CO2_Luft] #Startparameter in Vektor
            t_start=0
            t_ende=row[InputKeys.duration] 
       
        else:
            c_x_0=y[-1,0] #"-1" means the last element of the array
            c_S1_0=y[-1,1]+row[InputKeys.bolus_c]
            c_S2_0=y[-1,2]+row[InputKeys.bolus_n]
            c_P_0=y[-1,3]
            #print("c_P0",c_P_0)
            c_DO_0=y[-1,4]
            O2_Out=y[-1,5]      #Konz. O2 in Abluft
            CO2_Out=y[-1,6]     #Konz. CO2 in Abluft
            y0=[c_x_0,c_S1_0,c_S2_0, c_P_0, c_DO_0, O2_Out, CO2_Out] #Startparameter in Vektor
            t_start=result.t[-1]
            t_ende=t_start+row[InputKeys.duration]
            #print("Calc Phase: ",i," from ",t_start," - ",t_ende,"h")

        if row[InputKeys.duration]!=0:
            print("Calc Phase: ",index," from ",t_start," - ",t_ende,"h")
            datapoints=row[InputKeys.duration]*data_rate
            t_span=np.linspace(t_start,t_ende,datapoints)
            if datapoints < 50:datapoints=50 #this is needed in case a Phase is really short so the minimal number of datapoint per phase=50
            Fpar_d=row.to_dict() #extract Fermentation parameters for current phase and convert to dictionary as this is faster in solve_ivp
            
        
        result=solve_ivp(Bioreaktor_ODE,(t_start,t_ende),y0,args=(model_param,Fpar_d), t_eval=t_span, max_step=0.0005, atol=1e-6, rtol=1e-7)
        #solve_IVP Explanations
            #args are passed as a tupel - a single element in a tupel is single_element_tuple = (5,)
            #via small atol and rtol practical "non-negative" is achieved
            # #Results of Solve_ivp stores y values in result.y which is an array of one row per parameter
            #and n-datapoints in n columns
        if index==0:
            y=result.y.T
            y_ges=y #transform array
            #print("dim y_ges", y_ges.shape)
            t_ges=np.atleast_2d(result.t).T
            #print("dim t_ges", t_ges.shape)
            # sum_feeding = t_span*Fpar["Feed_C"][0]
            # len_t_span=len(t_span)
            # Drehzahl = np.zeros(len_t_span)+Fpar["Drehzahl"][0]
            # Begasungsrate = np.zeros(len_t_span)+Fpar["Q_Air"][0]
            # Druck = np.zeros(len_t_span)+Fpar["Druck"][0]
        else:
            y=result.y.T #transform array
            y_ges=np.vstack((y_ges, y))
            t=np.atleast_2d(result.t).T
            t_ges=np.vstack((t_ges, t))
            # already_fed=sum_feeding[-1]
            # t_span_temp=np.subtract(t_span,t_span[0])
            # temp_feed=already_fed+t_span_temp*Fpar["Feed_C"][i-1]
            # sum_feeding = np.hstack((sum_feeding, temp_feed))
            # len_t_span=len(t_span)
            # Drehzahl = np.hstack((Drehzahl, np.zeros(len_t_span)+Fpar["Drehzahl"][i-1]))
            # Begasungsrate = np.hstack((Begasungsrate, np.zeros(len_t_span)+Fpar["Q_Air"][i-1]))
            # Druck = np.hstack((Druck,np.zeros(len_t_span)+Fpar["Druck"][i-1]))
    result_df=pd.DataFrame([0,0])
    return result_df
