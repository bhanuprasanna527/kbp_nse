import pandas as pd
import re
import os
import csv

def specific_company(symbol = "RELIANCE"):
    # Get Directory path and list contents
    directory = os.getcwd()
    dir_list = os.listdir(directory)

    # Use of Regular expressions
    r = re.compile("^bhav")
    filtered_list = list(filter(r.match, dir_list))

    # Get Company Data
    with open(symbol, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        header = []
        data = []
        flag = 1
        
        for i in filtered_list:
            data = []
            df = pd.read_csv(i)
            if flag == 1:
                header = df.columns
                writer.writerow(header)
                flag = 0
            data = df.loc[df['SYMBOL'] == 'RELIANCE'].values.tolist()
            writer.writerow(data[0])