class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def __str__(self):
        return f"{self.name}, {self.__age} лет"

class Student(Person):  # наследование
    def __init__(self, name, age, group):
        super().__init__(name, age)
        self.group = group
        self.courses = []
    def add_course(self, course):
        self.courses.append(course)

class Professor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
        self.courses = []
    def teach(self, course):
        self.courses.append(course)
    def __str__(self):
        return f"Профессор {self.name}"


ivanov = Student("Иванов", 20, "ИСУ-01")
smirov = Professor("Смирнов", 45, "МО")
ivanov.add_course("Базы данных")
smirov.teach("Математический анализ")

persons = [ivanov, smirov]
for person in persons: print(person)
    # Иванов, 20 лет
    # Профессор Смирнов

persons = [
        { 
            "name": person.name, 
            "age": person._Person__age, 
            "type": type(person).__name__
        } for person in persons
    ]
print(persons)

dct = {
    "university": "hse",
    "persons": [
        { 
            "name": person.name, 
            "age": person._Person__age, 
            "type": type(person).__name__
        } for person in persons
    ]
}
dct = {
    "university": "hse",
    "students": [
        {
            "name": "Иванов",
            "age": 20,
            "courses": ["БД", "Программирование"]
        },
        { "name": "Петров", "age": 21 }
    ]
}