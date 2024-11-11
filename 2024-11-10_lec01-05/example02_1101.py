import pandas as pd
# select ename,empno,jon and sal from emp
emp = pd.read_csv("data/emp.csv")
print(emp[["empno", "ename", "job", "sal"]])
