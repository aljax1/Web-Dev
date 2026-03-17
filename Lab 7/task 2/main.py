from models import Animal, Dog, Cat

# Create objects
animal = Animal("Generic Animal", 5, "brown")
dog = Dog("Buddy", 3, "golden", "Labrador")
cat = Cat("Whiskers", 4, "white", True)

# Store in a list
animals = [animal, dog, cat]

# Iterate and print each object
print("=== All Animals ===")
for a in animals:
    print(a)

print()

# Call methods on each object
print("=== Sounds (Polymorphism) ===")
for a in animals:
    a.speak()

print()

# Call unique methods
print("=== Unique Actions ===")
dog.fetch()
cat.purr()

print()

# Call common methods
print("=== Common Actions ===")
dog.eat()
cat.sleep()