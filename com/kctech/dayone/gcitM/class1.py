import pymongo

class Pet:

    # expects to be instantiated using a dictionary like ...
    # pet = Pet({'name':'Kirby', 'type':'Dog', 'age':'really old'})
    def __init__(self, options):
        self._name = options['name']
        self._animal_type = options['type'] # e.g. 'Dog', 'Cat' and 'Bird'
        self._age = options['age']

    def get_name(self):
        return self._name

    def get_animal_type(self):
        return self._animal_type

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        self._name = new_name

    def set_animal_type(self, new_type):
        self._animal_type = new_type

    def set_age(self, new_age):
        self._age = new_age

# Once you have written the class, write a program that creates an object of the class and prompts the user to enter the name, type and age of his or her pet.  This data should be stored as the object's attributes.
# Use the object's accessor methods to retrieve the pet's name, type, and age and display this data on the screen.

print("----------------")
print("PETS APPLICATION")
print("-----------------")

animal_type = input("Please input the type of pet (e.g. 'Dog'): ")
name = input("Please input the pet's name (e.g. 'Ruffles'): ")
age = input("Please input the pet's age in years (e.g. '11'): ")

pet = Pet({'name': name, 'type': animal_type, 'age': age})

# d={'name': pet._animal_type, 'type': pet._name, 'age': pet._age}






client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['Pets']
information2=mydb.employeeinformation2
# record2={
#     'firstname':'hi',
#     'lastname':'welcome',
#
# }
d={'name': pet._name, 'type': pet._animal_type, 'age': int(pet._age)}
information2.insert_one(d)







