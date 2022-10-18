import pandas as pd
import time

url=input("Type URL:\n")
# csv-file-url = "https://raw.githubusercontent.com/arungautam071/csvfile071/main/myFile0.csv"

#file read using pandas
csvfileread = pd.read_csv(url)

#print file data using file url
print(csvfileread.to_string())

time.sleep(20)
