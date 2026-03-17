from models import Animal, Dog, Cat

animal = Animal("Generic Animal", 5, "brown")
dog = Dog("Buddy", 3, "golden", "Labrador")
cat = Cat("Whiskers", 4, "white", True)

animals = [animal, dog, cat]

print("=== All Animals ===")
for a in animals:
    print(a)

print()

print("=== Sounds (Polymorphism) ===")
for a in animals:
    a.speak()

print()

print("=== Unique Actions ===")
dog.fetch()
cat.purr()

print()

print("=== Common Actions ===")
dog.eat()
cat.sleep()