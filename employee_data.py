import pandas as pd

# Create a DataFrame with sample employee data
employees_data = {
    'employee_id': [1001, 1002, 1003, 1004, 1005],
    'name': ['Alice Johnson', 'Bob Smith', 'Carol Williams', 'David Brown', 'Eve Davis'],
    'department': ['Sales', 'Engineering', 'HR', 'Engineering', 'Finance'],
    'salary': [65000, 85000, 55000, 90000, 72000],
    'hire_date': ['2021-03-15', '2020-07-22', '2022-01-10', '2019-11-05', '2021-06-18'],
    'email': ['alice@company.com', 'bob@company.com', 'carol@company.com', 'david@company.com', 'eve@company.com']
}

df = pd.DataFrame(employees_data)

# Display the DataFrame
print("Employee Data:")
print(df)
print("\nDataFrame Info:")
print(df.info())
print("\nBasic Statistics:")
print(df.describe())
