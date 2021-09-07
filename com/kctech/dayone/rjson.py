f=open("D://saravanan//python//com//kctech//dayone//book.txt","r")
s=f.read()
import json
book=json.loads(s)

d={}
c=""
for id in book:

    for k in book[id]:
        c = ""
        for i in (book[id][k]):

            for s in i:
                if s == '\'' or "\"":
                    c= c + s
                else:
                    c = c + s
            d[k]=c

    print(d)




