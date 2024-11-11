import pandas as pd

# print capitalized telecom and ename
emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")
# emp20["telecom"] = emp20["telecom"].str.capitalize()
# print(emp20[["ename", "telecom"]])
result = pd.concat([emp20["ename"], emp20["telecom"].str.capitalize()], axis=1)
print(result)
