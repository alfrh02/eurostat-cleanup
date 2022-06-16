#!/usr/bin/env python3
import pandas as pd
import argparse
import json

parser = argparse.ArgumentParser(description="Convert Eurostat country code values to country names for Tableau usage. Must be converted to CSV through MS Excel, Google Sheets, or otherwise.")

parser.add_argument("file", type=str, help="CSV file name.")
parser.add_argument("column", type=str, help="Column to convert to country names.")
parser.add_argument("exception", type=str, help="If this string is not encountered, the cell will be skipped & will not be replaced with the country name.")
args = parser.parse_args()

jsonfile = open("codes.json")
codes = json.load(jsonfile)

datafile = args.file
df = pd.read_csv(datafile)

column_name = rf"{args.column}" 
print(column_name)

exception =  rf"{args.exception}"

counter = 0
for i in df[column_name]:   
    x = str(i)
    if exception not in x:
        print(x)
        df = df.drop(counter)
        df.to_csv(datafile, index=False)
        print(f"{counter} DROPPED!")
        counter += 1
        continue
    x = x[-2] + x[-1] 
    try:
        i = codes[x]
        df.loc[counter, column_name] = i
        df.to_csv(datafile, index=False)
        counter += 1
    except:
        counter += 1
        continue
