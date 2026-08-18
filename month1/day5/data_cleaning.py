import pandas as pd

data = pd.read_csv("employees.csv")

# print(data.info())

print(data.isnull().sum())

# data = data.drop_duplicates()

# average_salary = data["salary"].mean()
# data["salary"] = data["salary"].fillna(average_salary)
# data["department"] = data["department"].fillna("Unknown")
# data = data.sort_values(by="salary", ascending=False)

# engineering = data[data["department"] == "Engineering"]

# print(engineering)