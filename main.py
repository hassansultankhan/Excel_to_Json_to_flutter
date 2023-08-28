import pandas as pd

# Provide the full path to the Excel file
excel_file = r'C:\Users\pakih\projects\python_1\test.xlsx'

# Read the Excel file
data = pd.read_excel(excel_file)

# Convert to JSON
json_data = data.to_json(orient='records')

print(json_data)

# Save JSON data to a file
with open('output.json', 'w') as json_file:
    json_file.write(json_data)
