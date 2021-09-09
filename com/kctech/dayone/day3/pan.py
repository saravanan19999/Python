import pandas as pd

data = pd.read_csv("employees.csv")

data.drop_duplicates(subset="FIRST_NAME",keep='first',inplace = True)

df=data
df.to_csv('nice4.csv')