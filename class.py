class person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def fullname (self):
            return f"{self.name} {self.age}"

my_person = person("ram", 20)
print(my_person.name)
print(my_person.age) 
print(my_person.fullname())
print(my_person)    

class asianperson(person):
    def __init__(self, name, age, country, hobby):
        super().__init__(name, age)
        self.country = country
        self.hobby = hobby

    def fullname (self):
            return f"{self.name} {self.age} {self.country} {self.hobby}"

My_asian_person = asianperson("nina", 25, "korea", "dancing")
print(My_asian_person.name)   
print(My_asian_person.age) 
print(My_asian_person.country)
print(My_asian_person.hobby)
print(My_asian_person.fullname())






    