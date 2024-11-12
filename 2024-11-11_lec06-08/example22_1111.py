import pandas as pd

# print name, rank and rank by sal
# emp = pd.read_csv("../data/emp.csv", encoding="euckr")
# emp["rank"] = emp["sal"].rank(ascending=False).astype(int)
# print(emp[["ename", "rank"]].sort_values(by="rank", ascending=True))

# print age, name, rank by age
# emp20 = pd.read_csv("../data/emp20.csv", encoding="euckr")
# emp20["rank"] = emp20["age"].rank(method="dense", ascending=False).astype(int)
# result = emp20[["ename", "age", "rank"]].sort_values(
#     by="rank", ascending=True)
# print(result)

# print rank and name and sal ranked by sal saleman only
# emp = pd.read_csv("../data/emp.csv")
# emp = emp[emp["job"] == "SALESMAN"]
# emp["rank"] = emp["sal"].rank(method="dense", ascending=False).astype(int)
# result = emp[["ename", "sal", "job", "rank"]
#              ].sort_values(by="rank", ascending=True)
# print(result)

# print deptno,ename,sal,rank by sal
# emp = pd.read_csv("../data/emp.csv")
# emp["rank"] = emp.groupby("deptno", as_index=False)["sal"].rank(
#     method="dense", ascending=False)
# result = emp[["deptno", "rank", "sal", "ename"]].sort_values(
#     by=["deptno", "rank"], ascending=[True, True])
# print(result)

# print telecom,ename,age rank and ranked by age per telecom
emp20 = pd.read_csv("../data/emp20.csv", encoding="euckr")
emp20["rank"] = emp20.groupby("telecom", as_index=False)[
    "age"].rank(method="dense", ascending=False).astype(int)
result = emp20[["telecom", "rank", "age", "ename"]].sort_values(
    by=["telecom", "rank"], ascending=[True, True])
print(result)
