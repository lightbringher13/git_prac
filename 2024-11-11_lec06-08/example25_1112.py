import pandas as pd

# print shift lead shift lag
# emp = pd.read_csv("../data/emp.csv")
# emp["sal_lead"] = emp["sal"].shift(-1).fillna(0).astype(int)
# emp["sal_lag"] = emp["sal"].shift(1).fillna(0).astype(int)
# print(emp[["sal_lead", "sal", "sal_lag"]])

# print shift lead hire date
# emp = pd.read_csv("../data/emp.csv")
# emp["hiredate_lead"] = emp["hiredate"].shift(1).fillna(0)
# print(emp[["ename", "hiredate", "hiredate_lead"]])
