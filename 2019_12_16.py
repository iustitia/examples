d = {'anna': 5, 'jan': 4, 'iga':3 }
d['marek'] = 5

def f(name, grade):
    d[name] = grade

f('zbyszek', 3)

# biology grades

school = {
    '123234': {
        'name': "Justyna",
        'surname': "Kub",
        'subject': 'Biology',
        'grades': [4, 5, 3, 2]
    },
    '123456': {
        'name': "Anna",
        'surname': "Kowalska",
        'subject': 'Biology',
        'grades': [4, 5, 3, 2]
    },
}

school["2348723"] = {"name": "Zbyszek", "surname": "Azdsd"}

# update a grade
school["123234"]["grades"].append(5)

school["123234"]["subject"] = "Language"


def add_student(index_number, name, surname, subject):
    pass
    #todo


#average:
grades = [12, 3, 5]
sum(grades)/len(grades)


class Student:
    def __init__(self, index_number, name, surname):
        self.index_number = index_number
        self.name = name
        self.surname = surname

    def __str__(self):
        return "Student: " + self.name + " " + self.surname


s = Student('34234', 'Jan', 'Nowak')
print(s)
