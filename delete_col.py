import argparse
import pandas as pd
parser = argparse.ArgumentParser(description="Fill missing values in CSV file")
parser.add_argument("input_file", help="Input CSV file")
parser.add_argument("--rate",  default= "50", help="if number missing row > rate then delete row")
parser.add_argument("--out", dest="output_file", default="result.csv", help="Output CSV file")
args = parser.parse_args()

data = pd.read_csv(args.input_file)
rate = float(args.rate)
numbers_row = len(data)
cols_delete = []
for col in data.columns:
    count = 0
    for value in data[col]:
        if value != value:
            count += 1
    if float((count/numbers_row)*100) >= rate:
        cols_delete.append(col)
for col in cols_delete:
    del data[col]
data.to_csv(args.output_file)