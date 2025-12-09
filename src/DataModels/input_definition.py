from enum import Enum

class InputKeys(str, Enum):
    model = "Modell",
    phase = "Phase",
    q_air = "Q_Air_vvm",
    bolus_c = "Bolus_C",
    feed_c = "Feed_C",
    bolus_n = "Bolus_N",
    rotation_speed = "Drehzahl",
    pressure = "Druck",
    duration = "Dauer",
    v_l = "V_L",
    t = "T",
    ph = "pH",
    do = "DO",
    density = "Dichte",
    c_x = "c_x0",
    q_in = "Q_in" 
    q_out = "Q_Out",