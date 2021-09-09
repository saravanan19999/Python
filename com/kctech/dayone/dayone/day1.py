from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.nfl.com/standings/league/2020/reg'
page=requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')


table=soup.find('table', class_ ="d3-o-table d3-o-table--row-striping d3-o-table--detailed d3-o-standings--detailed d3-o-table--sortable {sortlist: [[4,1]], sortinitialorder: 'desc'}")
headers = []
for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)


df = pd.DataFrame(columns = headers)

for row in table.find_all('tr')[1:]:
    data=row.find_all('td')
    row_data=[td.text.strip() for td in data]
    length=len(df)
    df.loc[length]=row_data

col=df.columns

print(col)
for i in col:
    for j in df[i]:
        print("orginal : {0} , Data_type : {1}" .format(j,type(j)))