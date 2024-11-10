import pandas as pd

# print ename first letter and second letter
# emp = pd.read_csv("data/emp.csv")
# emp["ename"] = emp["ename"].str.slice(start=0, stop=2)
# print(emp["ename"])

# print ename, age if first letter is 김
# emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")
# result = emp20[["ename", "age"]][emp20["ename"].apply(lambda x: x[0] == "김")]
# print(result)
# result = emp20[["ename", "age"]
#                ][emp20["ename"].str.slice(start=0, stop=1) == "김"]
# print(result)

# print address,ename,age not living in seoul and age ascending order

emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")
# result = emp20[["ename", "age", "address"]
#                ][emp20["address"].apply(lambda x: x[0:2] != "서울")]
result = emp20[["ename", "age", "address"]
               ][emp20["address"].str.slice(start=0, stop=2) != "서울"]
print(result.sort_values(by="age", ascending=True))
