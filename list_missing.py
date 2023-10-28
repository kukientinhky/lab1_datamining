import sys
import pandas as pd
fileName = sys.argv[1]
data = pd.read_csv(fileName)
columns_with_missing_values = []
columns = data.columns
for column in columns:
    for row in data[column]:
        if row != row: ##check NaN
            columns_with_missing_values.append(column)
            break
print(columns_with_missing_values) 