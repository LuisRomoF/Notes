# Object-Oriented Programming in Python
Classes are templates for objects.
<br> The ***self*** parameter used in Class methods is a stand-in for a particular object used in class definition. It is equivalent to passing the specific object as an argument for the general Class method.
Class anatomy:
* Attributes: characteristics of the Class created.
* Methods: functions definitions within a class.

**Class attributes**: Global constants related to the class. Data shared among all instances of a class
<br>**Class methods**: This methods can't use instance-level data.
One of the main usecases for class methods is alternative constructors.
```python
class MyClass:

    @classmethod  # Use classmethod decorator to declare a class method
    def from_file(cls, filename): # cls argument refers to the class
    with open(filename, "r") as f:
        name = f.readline()
    return cls(name) # cls will call __init__()

```

## Constructor
The Constructor is a special method ( \_\_init\_\_() ) called every time an object is created. The name is to be exactly: \_\_init\_\_() for python to recognize it.
<br> The best practice is to defined all the class attributes in the Constructor.
<br> Naming best practices for classes uses CamelCase format.

### Example:
```python
import numpy as np

class Point:
    def __init__(self,x = 0.0,y = 0.0):
        self.x = x
        self.y = y
    
    def distance_to_origin(self):
        return np.sqrt(self.x**2 + self.y**2)
    
    def reflect(self,axis):
        if axis == "x":
            self.y = -self.y
        elif axis == "y":
            self.x = -self.x
        else:
            print("error")
```

## Core principles of OOP
* **Inheritance:** Extending functionality of existing code.
* **Polymorphism:** Creating a unified interface.
* **Encapsulation:** Bundling of data and methods.