emp = pd.read_csv("../data/emp.csv")
emp = emp.groupby("job", as_index=False)["empno"].count()
emp = emp.rename(columns={"empno": "count"})
emp = emp[emp["count"] >= 3]
print(emp)