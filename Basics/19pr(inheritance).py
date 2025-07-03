class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, species, breed):
        # Call the base class constructor
        super().__init__(name, species)
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks loudly!")

# Create an instance of Dog
my_dog = Dog(name="Buddy", species="Canine", breed="Golden Retriever")

# Access properties and methods
print(f"Name: {my_dog.name}")
print(f"Species: {my_dog.species}")
print(f"Breed: {my_dog.breed}")

my_dog.speak()  # Calls the base class method
my_dog.bark()   # Calls the subclass method
