import json
import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


person = Person("Alice", 30)

# 序列化
with open('person.pkl', 'wb') as f:
    pickle.dump(person, f)

# 反序列化
with open('person.pkl', 'rb') as f:
    person_new = pickle.load(f)

person_new.display()  # 输出: Name: Alice, Age: 30
