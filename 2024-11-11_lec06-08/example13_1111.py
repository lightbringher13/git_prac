import pandas as pd

# print ename,sal if "M" is in the ename
# emp = pd.read_csv("../data/emp.csv")
# print(emp[["ename", "sal"]][emp["ename"].str.find("M") >= 0])

# print ename,sal if "M" is not in the ename not include reuturn -1
# emp = pd.read_csv("data/emp.csv")
# print(emp[["ename", "sal"]][emp["ename"].str.find("M") == -1])

emp = pd.read_csv("../data/emp.csv")
emp["find"] = emp["ename"].str.find("M")
print(emp[["find", "ename"]])
