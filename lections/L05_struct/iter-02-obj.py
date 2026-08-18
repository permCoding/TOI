class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)

# Способ 1: dir() — все атрибуты (включая служебные)
for attr in dir(p):
    if not attr.startswith('_'):  # фильтруем служебные
        print(f"{attr} = {getattr(p, attr)}")
# name = Alice
# age = 30

# Способ 2: vars() — только атрибуты, определённые в __dict__
for key, value in vars(p).items():
    print(f"{key} = {value}")
# name = Alice
# age = 30

# Способ 3: __dict__ напрямую (не у всех объектов!)
for key in p.__dict__:
    print(f"{key} = {p.__dict__[key]}")
