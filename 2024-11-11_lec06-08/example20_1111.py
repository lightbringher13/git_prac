import pandas as pd

# print job and man count per job
# emp = pd.read_csv("../data/emp.csv")
# emp = emp.groupby("job", as_index=False)["empno"].count()
# print(emp)

# print job and man count per job if man count >= 3
# emp = pd.read_csv("../data/emp.csv")
# emp = emp.groupby("job", as_index=False)["empno"].count()
# emp = emp.rename(columns={"empno": "count"})
# emp = emp[emp["count"] >= 3]
# print(emp)
