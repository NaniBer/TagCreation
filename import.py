import pandas as pd
from processing import process_error_title  # Assuming this imports your function correctly

# Load the Excel file
xls = pd.ExcelFile('FAQs.xlsx')

# Choose a specific sheet (if needed, typically the first one)
sheet_name = xls.sheet_names[0]

# Read the entire sheet into a DataFrame
df = pd.read_excel(xls, sheet_name=sheet_name)

# Assuming df has columns 0, 1, 2, ... based on your description
column_1_name = df.columns[1]  # Get the name of column 1
column_2_name = df.columns[2]  # Get the name of column 2

# List all entries (values) of column 1 and column 2
column_1_entries = df[column_1_name].tolist()
column_2_entries = df[column_2_name].tolist()

# Print column 2 entries
# print("Column 2 (Error Messages or Details):")
# print(column_2_entries)

# Initialize an empty list to store results
questions_list = []

# Iterate through each pair of entries from column 1 and column 2
for question, error_message in zip(column_1_entries, column_2_entries):
    # Process error message and title
    print(error_message)
    ranked_words = process_error_title(error_message, question)
    
    # Store results in a dictionary format (optional)
    result = {
        'Question': question,
        'Error_Message': error_message,
        'Ranked_Words': ranked_words
    }
    
    # Append result to questions_list
    questions_list.append(result)

# Print or use the results
# for result in questions_list:
#     print(f"\nQuestion: {result['Question']}")
#     print(f"Error Message: {result['Error_Message']}")
#     print("Ranked Words based on Occurrence:")
#     for word, count in result['Ranked_Words']:
#         print(f"{word}: {count}")
