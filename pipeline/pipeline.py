import sys
import pandas as pd


print('Hello')
print('arguments', sys.argv[0])

month = sys.argv[1]

print(f'month = {month} \nmon = {month}')

data = pd.DataFrame({"day":[1,2], "year":[2026,2026]})
data["month"] = month
print(data)

data.to_parquet(f'output_{month}.parquet')

readp = pd.read_parquet(f'output_{month}.parquet')
print(readp)
