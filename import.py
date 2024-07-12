import pandas as pd

# Load the Excel file
xls = pd.ExcelFile('FAQs.xlsx')

# Choose a specific sheet (if needed, typically the first one)
sheet_name = xls.sheet_names[0]

# Read only the first row (which contains column headers)
df_columns = pd.read_excel(xls, sheet_name=sheet_name, nrows=1)

# Display column names
print(df_columns.columns.tolist())


# Read the entire sheet into a DataFrame
df = pd.read_excel(xls, sheet_name=sheet_name)

# Replace 'Column_Name' with the actual column name you want to list entries from
column_name = df_columns.columns[2]
print(column_name)

# # List all entries (values) of the specified column
column_entries = df[column_name].tolist()

# # Display the entries
print(column_entries)

