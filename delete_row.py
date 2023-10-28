import argparse
import pandas as pd
# command line
parser = argparse.ArgumentParser(description="Fill missing values in CSV file")
parser.add_argument("input_file", help="Input CSV file")
parser.add_argument("--rate",  default= "50", help="if number missing row > rate then delete row")
parser.add_argument("--out", dest="output_file", default="result.csv", help="Output CSV file")
args = parser.parse_args()

data = pd.read_csv(args.input_file)
rate = float(args.rate)
numbers_col = len(data.columns)
indexs = []
for index in range(len(data)):
    count = 0
    for value in data.iloc[index]:
        if value != value:
            count += 1
    if float((count/numbers_col)*100) >= rate:
        indexs.append(index)
for index in indexs:
    data = data[data.index != index]
data.to_csv(args.output_file)