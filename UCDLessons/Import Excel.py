import pandas as pd
file='urbanpop.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names)
df1 = data.parse('1960-1966')  # sheet name as a string
df2 = data.parse(0)  # sheet index as a float

print(df1.head())  # print first few rows of the sheet

# Parse the first sheet and rename the columns. Skip first row and rename the columns
df3 = data.parse(0, skiprows=[1], names=['Country','AAM due to War (2002)'])

# Print the head of the DataFrame df3
print(df3.head())

# Parse the first column of the second sheet and rename the column. Only use first column
df4 = data.parse(0, usecols=[0], skiprows=[1], names=['Country'])

# Print the head of the DataFrame df2
print(df4.head())