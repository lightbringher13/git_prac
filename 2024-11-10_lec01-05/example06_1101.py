import pandas as pd

# object to date
# emp = pd.read_csv("data/emp.csv")
# emp["hiredate"] = pd.to_datetime(emp["hiredate"])


# date time 1981-11-17
# emp = pd.read_csv("data/emp.csv")
# emp["hiredate"] = pd.to_datetime(emp["hiredate"])
# result = emp[["ename", "hiredate"]][emp["hiredate"] == "1981-11-17"]
# print(result)

# ename and hiredate for 1981
# emp = pd.read_csv("data/emp.csv")
# emp.info()
# emp["hiredate"] = pd.to_datetime(emp["hiredate"])
# emp.info()
# result = emp[["ename", "hiredate"]
#              ][emp["hiredate"].between("1981-1-1", "1981-12-31")]
# print(result)


# pirnt ename, job, hiredate if job is salesman and 1981 hiredate

# very important multiple conditions using "&"
# emp = pd.read_csv("data/emp.csv")
# emp["hiredate"] = pd.to_datetime(emp["hiredate"])
# result = emp[["ename", "job", "hiredate"]
#              ][(emp["hiredate"].between("1981-1-1", "1981-12-31")) & (emp["job"] == "SALESMAN")]
# print(result)

# very important multiple conditions using "|"
# emp = pd.read_csv("data/emp.csv")
# emp["hiredate"] = pd.to_datetime(emp["hiredate"])
# result = emp[["ename", "job", "hiredate"]
#              ][(emp["hiredate"].between("1981-1-1", "1981-12-31")) | (emp["job"] == "SALESMAN")]
# print(result)

# not using "&" and "|"
emp = pd.read_csv("data/emp.csv")
emp.info()
emp["hiredate"] = pd.to_datetime(emp["hiredate"])
result = emp[["ename", "job", "hiredate"]
             ][emp["hiredate"].between("1981-1-1", "1981-12-31")]
result = result[result["job"] == "SALESMAN"]
print(result)
