class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def __iter__(self):  # свой итератор
        return iter(vars(self).values())
    
    def keys(self):
        return iter(vars(self).keys())
    
    def items(self):
        return iter(vars(self).items())


p = Person("Alice", 30, "Moscow")

for value in p:  # Перебор значений
    print(value)  # Alice, 30, Moscow

for key in p.keys():  # Перебор ключей
    print(key)  # name, age, city

for key, value in p.items():  # Перебор пар
    print(f"{key}: {value}")
