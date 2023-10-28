import argparse
import pandas as pd
import math
## command line
parser = argparse.ArgumentParser(description="Fill missing values in CSV file")
parser.add_argument("input_file", help="Input CSV file")
parser.add_argument("--method", choices=["min_max", "z_score"], default="min_max", help="Imputation method: min_max or z_score")
parser.add_argument("--columns", nargs="+", help="Columns to impute")
parser.add_argument("--out", dest="output_file", default="result.csv", help="Output CSV file")
args = parser.parse_args()
data = pd.read_csv(args.input_file)
if args.method == "min_max":
    a = input("Nhap giá trị đầu trong đoạn muốn chuẩn hóa:")
    b = input("Nhap giá trị cuối trong đoạn muốn chuẩn hóa:")
    a = int(a)
    b = int(b)
    for column in args.columns:
        if column in data.columns:
            if data[column].dtype != 'object':
                mi = min(data[column])
                ma = max(data[column])
                index = 0
                for value in data[column]:
                    if value == value:
                        data.at[index, column] = round((((value - mi)/(ma - mi)) * (b - a) + a), 4)
                        index += 1
            else: 
                print("Not numeric")
else:
    for column in args.columns:
        if column in data.columns:
            if data[column].dtype != 'object':
                sum = 0
                sl = 0
                sum_squared = 0
                for value in data[column]:
                    if value == value:
                        sl += 1
                        sum += value
                mean = sum/sl
                for value in data[column]:
                    if value == value:
                        sum_squared += (value - mean) ** 2
                standard_deviation = math.sqrt(sum_squared / sl)
                index = 0
                for value in data[column]:
                    if value == value:
                        data.at[index, column] = round(((value - mean)/standard_deviation), 4)
                        index += 1
            else: 
                print("Not numeric")
data.to_csv(args.output_file)