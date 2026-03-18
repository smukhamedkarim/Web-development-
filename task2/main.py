from models import Animal, Dog, Cat


def main():
    generic_animal = Animal("Generic", 5, "Unknown")
    dog1 = Dog("Buddy", 3, "Golden Retriever")
    cat1 = Cat("Whiskers", 4, True)

    animals = [generic_animal, dog1, cat1]

    print("Objects:")
    for animal in animals:
        print(animal)

    print("\nDescriptions:")
    for animal in animals:
        print(animal.describe())

    print("\nPolymorphism:")
    for animal in animals:
        print(animal.speak())

    print("\nUnique methods:")
    print(dog1.fetch("ball"))
    print(cat1.purr())


if __name__ == "__main__":
    main()