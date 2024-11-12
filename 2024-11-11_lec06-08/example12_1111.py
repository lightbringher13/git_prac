import pandas as pd

# add length of ename series
# emp = pd.read_csv("data/emp.csv")
# emp["ename_len"] = emp["ename"].str.len()
# print(emp[["ename"]].sort_values(by="ename_len", ascending=False))

# add length of ename series
tit = pd.read_csv("data/train.csv")

tit["Name_len"] = tit["Name"].str.len()
print(tit[["Name", "Name_len"]].sort_values(by="Name_len", ascending=False))
