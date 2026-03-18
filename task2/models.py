class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        return f"{self.name} makes a generic animal sound."

    def describe(self):
        return f"{self.name} is a {self.age}-year-old {self.species}."

    def __str__(self):
        return f"Animal(name={self.name}, age={self.age}, species={self.species})"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")
        self.breed = breed

    def speak(self):
        return f"{self.name} says: Woof! Woof!"

    def fetch(self, item):
        return f"{self.name} fetches the {item} and brings it back!"

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age, "Cat")
        self.indoor = indoor

    def speak(self):
        return f"{self.name} says: Meow!"

    def purr(self):
        return f"{self.name} purrs... Purrr..."

    def __str__(self):
        return f"Cat(name={self.name}, age={self.age}, indoor={self.indoor})"

