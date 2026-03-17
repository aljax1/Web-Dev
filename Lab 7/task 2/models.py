class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def speak(self):
        print(f"{self.name} makes a sound.")

    def __str__(self):
        return f"Animal: {self.name}, Age: {self.age}, Color: {self.color}"


class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed

    def speak(self):
        print(f"{self.name} says: Woof!")

    def fetch(self):
        print(f"{self.name} fetches the ball!")

    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}, Breed: {self.breed}"


class Cat(Animal):
    def __init__(self, name, age, color, indoor):
        super().__init__(name, age, color)
        self.indoor = indoor

    def speak(self):
        print(f"{self.name} says: Meow!")

    def purr(self):
        print(f"{self.name} is purring...")

    def __str__(self):
        indoor_str = "indoor" if self.indoor else "outdoor"
        return f"Cat: {self.name}, Age: {self.age}, {indoor_str}"