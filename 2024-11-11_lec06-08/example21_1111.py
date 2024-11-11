import pandas as pd

# groupby two columns
# emp = pd.read_csv("../data/emp.csv")
# emp = emp.groupby(["deptno", "job"], as_index=False)["sal"].sum()
# print(emp)

# print address with from 3 letters from front
# emp20 = pd.read_csv("../data/emp20.csv", encoding="euckr")
# result = emp20["address"].str.slice(start=0, stop=3)

# make address2 and man count per address2
# emp20 = pd.read_csv("../data/emp20.csv", encoding="euckr")
# emp20["address2"] = emp20["address"].apply(lambda x: x[0:3])
# emp20 = emp20.groupby("address2", as_index=False)["empno"].count()
# print(emp20)

# make address2 and man count per address2,telecom
emp20 = pd.read_csv("../data/emp20.csv", encoding="euckr")
emp20["address2"] = emp20["address"].str.slice(start=0, stop=3)
result = emp20.groupby(["telecom", "address2"], as_index=False)[
    "empno"].count()
print(result)
