# Import libraries
import pandas as pd

# Create sample dataset
data = {
    "Name": ["John", "Alice", "Bob", "Emma", "David"],
    "Department": ["IT", "HR", "IT", "Finance", "IT"],
    "Salary": [60000, 50000, 70000, 65000, 80000]
}

df = pd.DataFrame(data)

# Display data
print("Dataset:\n", df)

# Basic analysis
print("\nAverage Salary:", df["Salary"].mean())

# Filter high salary
high_salary = df[df["Salary"] > 60000]
print("\nHigh Salary Employees:\n", high_salary)

# Group by department
dept_avg = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:\n", dept_avg)

# Sorting
sorted_df = df.sort_values(by="Salary", ascending=False)
print("\nSorted by Salary:\n", sorted_df)
