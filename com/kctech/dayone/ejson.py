book ={}
book['tom']={
    'name':'saravana',
    'address':'1 red street',
    'phone':98989898
}
book['bob']={
    'name':'bob',
    'address':'1 green street',
    'phone':23424234
}

import json
s=json.dumps(book)
print(s)

with open("D://saravanan//python//com//kctech//dayone//book.txt","w") as f:
    f.write(s)