import argparse
import pandas as pd
parser = argparse.ArgumentParser(description="Fill missing values in CSV file")
parser.add_argument("input_file", help="Input CSV file")
parser.add_argument("--out", dest="output_file", default="result.csv", help="Output CSV file")
args = parser.parse_args()


data = pd.read_csv(args.input_file)
seen_rows = set()
unique_rows = []
for index, row in data.iterrows():
    row_tuple = tuple(row)
    if row_tuple not in seen_rows:
        seen_rows.add(row_tuple)
        unique_rows.append(row)
new_data = pd.DataFrame(unique_rows, columns=data.columns)
new_data.to_csv(args.output_file)