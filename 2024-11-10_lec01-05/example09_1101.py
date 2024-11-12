import pandas as pd

# print ename and sal with ename lower
# emp = pd.read_csv("data/emp.csv")
# result = pd.concat([emp["ename"].str.lower(), emp["sal"]], axis=1)
# print(result)
# emp["ename"] = emp["ename"].str.lower()
# print(emp[["ename", "sal"]])

# print name and sal if search name is lower
emp = pd.read_csv("data/emp.csv")
print(emp[["ename", "sal"]][emp["ename"].str.lower() == "scott"])
