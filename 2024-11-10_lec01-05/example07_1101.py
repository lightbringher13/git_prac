import pandas as pd

# no duplicate data
# emp = pd.read_csv("data/emp.csv")
# print(emp["deptno"].unique())


# make tit from train.csv
# tit = pd.read_csv("data/train.csv")
# print(tit["Pclass"].unique())

# print no duplicate if deptno is 20
# emp = pd.read_csv("data/emp.csv")
# result = emp[["deptno", "job"]][emp["deptno"] == 20]
# print(result["job"].unique())

# print age no duplicate if telecom is sk and kt
emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")
print(emp20["age"][emp20["telecom"].isin(["sk", "kt"])].unique())
