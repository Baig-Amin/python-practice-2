class person:
    def __init__(self, person_name, db, ht):
        self.name = person_name
        self.date_of_birth = db
        self.hight = ht

    def update(self, new_name):
        self.name = new_name

    def get_summary(self):
        return f"Name: {self.name}, Date_of_birth: {self.date_of_birth}, Hight: {self.hight}"

person_list = [person("Kai",1994,5.10),
person("Amin",1996,5.9), person("goku",1980,6.8)]

for eachone in person_list:
    if eachone.date_of_birth >= 1990:
        print(eachone.get_summary())

#a_person.update("Kai Amin")
#print(a_person.get_summary())


