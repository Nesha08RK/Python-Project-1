import pandas as pd
import datetime

filename = input("Enter the CSV filename to read (eg: data.csv): ")
file_obj = None
try:
    file_obj = open(filename, 'r')
    df = pd.DataFrame(file_obj)
    print(df)

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")


