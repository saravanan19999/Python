import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['Pets']
information2=mydb.employeeinformation2
# record2={
#     'firstname':'hi',
#     'lastname':'welcome',
#
# }
print("For Search Press 1:")
print("For Update Press 2:")
print("For Delete Press 3:")
num=int(input("Enter the choice"))
if num==1:
    age=int(input("Enter the age"))
    for record in information2.find({"age" :{'$lt':age}}):
    # for record in information2.find().sort("name",1):
        print(record)
if num==2:
    name=input("Enter the Name")
    age=int(input("Enter The age"))
    information2.update_one({"name":name},{"$set":{"age":age}})
if num==3:
    name=input("Enter The Name")
    information2.delete_one({"name":name})