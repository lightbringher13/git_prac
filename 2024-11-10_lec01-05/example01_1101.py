import pandas as pd
# use relatvie paht
emp = pd.read_csv("data/emp.csv")
# use absolute path
emp1 = pd.read_csv(
    "/Users/jeonjaehwan/Desktop/python/BigData_Analysis/data/emp.csv")
print(emp1)
