import pandas as pd

data = pd.read_csv('employees.csv')

data = data.drop_duplicates()

average_salary = data['salary'].mean()
data['salary'] = data['salary'].fillna(average_salary)
data['department'] = data['department'].fillna('Unknown')
average_age = data['age'].mean()
data['age'] = data['age'].fillna(average_age)
highest_salary = data['salary'].max()
lowest_salary = data['salary'].min()
engineering_employees = data[data["department"] == "Engineering"]
sales_employees = data[data["department"] == "Sales"]
total_employees = len(data)  

print(f"""===== EMPLOYEE REPORT =====

- Total Employees: {total_employees}
- Average Salary: {average_salary}
- Highest Salary: {highest_salary}
- Lowest Salary: {lowest_salary}
- Engineering Employees: {len(engineering_employees)}
- Sales Employees: {len(sales_employees)}""")