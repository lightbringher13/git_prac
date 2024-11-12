import pandas as pd
# select instances with certain condition
# emp = pd.read_csv("data/emp.csv")
# print(emp[["ename", "sal"]][emp["sal"] == 3000])

# select ename,sal and job if job is salesman
# emp = pd.read_csv("data/emp.csv")
# print(emp[["ename", "sal", "job"]][emp["job"] == "SALESMAN"])

# select ename,sal and job if SAL >= 1200
# emp = pd.read_csv("data/emp.csv")
# print(emp[["ename", "sal"]][emp["sal"] >= 1200])

# select ename and sal if deptno is 20
emp = pd.read_csv("data/emp.csv")
print(emp[["ename", "sal", "deptno"]][emp["deptno"] == 20])
