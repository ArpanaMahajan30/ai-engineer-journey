import pandas as pd

data = {
    "name": ["Arpana", "John", "Sarah"],
    "age": [26, 30, 25],
    "skill": ["Python", "Java", "SQL"]
}

df = pd.DataFrame(data)

# print(df)

# print(df.head(2))

# print(df.columns)

# print(df.shape)

# print(df.describe())

# print(df["name"])  # Accessing a single column

# print(df[["name", "skill"]])  # Accessing multiple columns

# print(type(df["age"]))  # Accessing a single column returns a Series

# print(df[df["age"] > 20])  # Filtering rows based on a condition

# print(df[df["skill"] == "Python"]) # Filtering rows based on a condition

