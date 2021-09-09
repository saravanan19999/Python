import requests
from bs4 import BeautifulSoup
#getting url
page=requests.get('https://www.cricbuzz.com/live-cricket-scorecard/32058/4th-test-india-tour-of-england-2021')
#convert into html Structure
soup=BeautifulSoup(page.text, "html.parser")
#get Entire Table
k=0
for j in range(0,7):
    if j==2 or j==6:
        tbl=soup.find_all("div",class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[j]
        #get particula data eg names:
        names=[x.get_text() for x in tbl.find_all("div",class_="cb-col cb-col-27")]
        #remove spaces in names
        header=[]
        for i in names:
            header.append(i.upper().strip())
        print(header)
        #get runs of the player
        runs=[x.get_text()for x in tbl.find_all("div",class_="cb-col cb-col-8 text-right text-bold")]
        #this will remove R
        player_runs=runs[1:]
        # print(player_runs)
        val=input("Enter The Player Name:\n")
        val=val.upper()

        for i in range(0,len(names)):
            if val == header[i]:
                print(f"\nName of the Player:{names[i]}\n")
                print(f"Runs scored in {k+1} innings :{player_runs[i]}\n")
                k=k+1