import pandas as pd
# print sal between 1000 and 3000
# emp = pd.read_csv("data/emp.csv")
# print(emp[["ename", "sal"]][emp["sal"].between(1000, 3000)])

# in pandas not -> "~"
# [~ emp["sal"].between(1000, 3000)]

# print id,price if price between and 10 and 30
# boston = pd.read_csv("data/boston.csv")
# print(boston[["id", "price"]][boston["price"].between(10, 30)])

# print all if price between 10 and 30
# print(boston[:][boston["price"].between(10, 30)])

# print all if not price between 10 and 30
# print(boston[:][~boston["price"].between(10, 30)])

# print emp20 with korean MUST include "euckr"
# emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")

# print name and age if age is 20s
# emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")
# print(emp20[["ename", "age"]][emp20["age"].between(20, 29)])

# print name and job if job is salesman and analyst
# emp = pd.read_csv("data/emp.csv")
# print(emp[["ename", "job"]][emp["job"].isin(["SALESMAN", "ANALYST"])])

# print name and telecom if telecom is kt or lg
# emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")
# print(emp20[["ename", "telecom"]][emp20["telecom"].isin(["kt", "lg"])])

# print name and telecom if not telecom is kt or lg
# emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")
# print(emp20[["ename", "telecom"]][~emp20["telecom"].isin(["kt", "lg"])])

# print ename and commition if commition is null
# emp = pd.read_csv("data/emp.csv")
# print(emp[["ename", "comm"]][emp["comm"].isnull()])

# print ename and commition if commition is not null
# emp = pd.read_csv("data/emp.csv")
# print(emp[["ename", "comm"]][~emp["comm"].isnull()])

# print ename if ename's second letter is 'M'
# emp = pd.read_csv("data/emp.csv")
# print(emp[['ename']][emp["ename"].apply(lambda x: x[1] == 'M')])

# print ename and salary if enmae's last letter is "T"
# emp = pd.read_csv("data/emp.csv")
# print(emp[['ename', 'sal']][emp["ename"].apply(lambda x: x[-1] == 'T')])

# print ename and age if ename starts with letter "김"
# emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")
# print(emp20[["ename", "age"]][emp20["ename"].apply(lambda x: x[0] == "김")])

# print ename and age if not ename starts with letter "김"
# emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")
# print(emp20[["ename", "age"]][~emp20["ename"].apply(lambda x: x[0] == "김")])
