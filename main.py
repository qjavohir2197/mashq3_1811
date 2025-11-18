#3-misol
class Animal:
    def speak(self):
        raise NotImplementedError("Bu metod subclasslarda qayta aniqlanishi kerak!")



class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class Cow(Animal):
    def speak(self):
        return "Moo"



animals = [Dog(), Cat(), Cow(), Dog(), Cow()]


for animal in animals:
    print(f"{type(animal).__name__}: {animal.speak()}")
