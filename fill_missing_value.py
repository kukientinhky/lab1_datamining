import argparse
import pandas as pd
## command line
parser = argparse.ArgumentParser(description="Fill missing values in CSV file")
parser.add_argument("input_file", help="Input CSV file")
parser.add_argument("--method", choices=["mean", "median"], default="mean", help="Imputation method: mean or median")
parser.add_argument("--columns", nargs="+", help="Columns to impute")
parser.add_argument("--out", dest="output_file", default="result.csv", help="Output CSV file")
args = parser.parse_args()
data = pd.read_csv(args.input_file)
## tạo một dic Modes chứa mode của từng cột trong data
modes = {col: 0 for col in data.columns}
for col in data.columns:
     if data[col].dtype == 'object':
        mode_count = 0
        mode_value = None
        value_counts = {}
        for value in data[col]:
            if value == value:
                if value in value_counts:
                    value_counts[value] += 1
                else:
                    value_counts[value] = 1
                if value_counts[value] > mode_count:
                    mode_count = value_counts[value]
                    mode_value = value
        modes[col] = mode_value
## tạo một dic Modes chứa mean của từng cột trong data
means = {col: 0 for col in data.columns}
for col in data.columns:
    if data[col].dtype != 'object':
        sum = 0
        sl = 0
        for value in data[col]:
            if value == value:
                sl += 1
                sum += value
        if (sl ==0):
            means[col] = 0
        else:
            means[col] = sum/sl
## tạo một dic Modes chứa median của từng cột trong data
medians = {col: 0 for col in data.columns}
for col in data.columns:
    if data[col].dtype != 'object':
        sorted_col = sorted(data[col])
        if len(data) % 2 == 1:
            medians[col]  = sorted_col[len(data) // 2]
        else:
            medians[col]  = (sorted_col[len(data) // 2 - 1] + sorted_col[len(data) // 2])/2
## Thực thi chương trình
for column in args.columns:
    if column in data.columns:
        if data[column].dtype == 'object':
            index = 0
            for value in data[column]:
                if value != value:
                    data.at[index, column] = modes[column]
                index += 1
        else:
            if args.method == 'mean':
                index = 0
                for value in data[column]:
                    if value != value:
                        data.at[index, column] = means[column]
                    index += 1
            elif args.method == 'median':
                index = 0
                for value in data[column]:
                    if value != value:
                        data.at[index, column] = medians[column]
                    index += 1
data.to_csv(args.output_file)
