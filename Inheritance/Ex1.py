class Animal:

    def __init__(self, val):
        self.val = val;

    def dis(self):
        print(self.val)

class Dog(Animal):
    def bark(self):
        print("dog barking")

an = Animal(2);
an.dis()