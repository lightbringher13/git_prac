import pandas as pd

# upper emp20
emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")
# result = pd.concat([emp20["ename"], emp20["telecom"].str.upper()], axis=1)
# print(result)
# emp20["telecom"] = emp20["telecom"].str.upper()
# print(emp20[["ename", "telecom"]])
