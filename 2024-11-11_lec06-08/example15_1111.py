import pandas as pd

# insert a row
emp = pd.read_csv("data/emp.csv")
emp.loc[len(emp)] = {"ename": "     JACK     "}
print(emp)

# to save the changes
emp.to_csv("data/emp.csv", index=False)

print(emp[["ename", "sal"]][emp["ename"].str.strip().str.lower() == "jack"])
