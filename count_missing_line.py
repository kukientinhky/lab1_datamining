import sys
import pandas as pd
fileName = sys.argv[1]
data = pd.read_csv(fileName)
count = 0
for row in range(len(data)):
    for value in data.iloc[row]:
        if value != value:
            print(value)
            count += 1
            break
print(count)