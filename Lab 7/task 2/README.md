# Object-Oriented Programming in Python

## Files
- `models.py` - contains the Animal, Dog, and Cat classes
- `main.py` - demonstrates usage of the classes

## Class Structure

### Animal (Base Class)
- Attributes: `name`, `age`, `color`
- Methods: `eat()`, `sleep()`, `speak()`, `__str__()`

### Dog (Child Class)
- Inherits from Animal
- Extra attribute: `breed`
- Extra method: `fetch()`
- Overrides: `speak()` → prints "Woof!"

### Cat (Child Class)
- Inherits from Animal
- Extra attribute: `indoor`
- Extra method: `purr()`
- Overrides: `speak()` → prints "Meow!"

## Concepts Demonstrated
- Inheritance
- Polymorphism
- Encapsulation
- Modules and imports
