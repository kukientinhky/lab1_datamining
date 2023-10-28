import argparse
import pandas as pd
## command line
parser = argparse.ArgumentParser(description="Fill missing values in CSV file")
parser.add_argument("input_file", help="Input CSV file")
parser.add_argument("--method", choices=["add", "sub", "mul", "div"], default="add", help="Imputation method: add, sub, mul or div")
parser.add_argument("--columns", nargs="+", help="Columns to impute")
parser.add_argument("--out", dest="output_file", default="result.csv", help="Output CSV file")
args = parser.parse_args()
data = pd.read_csv(args.input_file)
news_value = []
if args.method == "add":
    attri_1 = args.columns[0]
    attri_2 = args.columns[1]
    if data[attri_1].dtype == 'object' or data[attri_2].dtype == 'object':
        print("Not numeric")
    else:
        for index in range((len(data))):
            news_value.append(float(data.loc[index, attri_1] +  data.loc[index, attri_2]))
        data[args.method] = news_value
elif args.method == "sub":
    attri_1 = args.columns[0]
    attri_2 = args.columns[1]
    if data[attri_1].dtype == 'object' or data[attri_2].dtype == 'object':
        print("Not numeric")
    else:
        for index in range((len(data))):
            news_value.append(float(data.loc[index, attri_1] - data.loc[index, attri_2]))
        data[args.method] = news_value
elif args.method == "mul":
    attri_1 = args.columns[0]
    attri_2 = args.columns[1]
    if data[attri_1].dtype == 'object' or data[attri_2].dtype == 'object':
        print("Not numeric")
    else:
        for index in range((len(data))):
            news_value.append(float(data.loc[index, attri_1] * data.loc[index, attri_2]))
        data[args.method] = news_value
else:
    attri_1 = args.columns[0]
    attri_2 = args.columns[1]
    if data[attri_1].dtype == 'object' or data[attri_2].dtype == 'object':
        print("Not numeric")
    else:
        for index in range((len(data))):
            news_value.append(float(data.loc[index, attri_1] / data.loc[index, attri_2]))
        data[args.method] = news_value
data.to_csv(args.output_file)