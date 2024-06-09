class Point :
    def draw(self) :
        print("drawing")
    
    def erase(self) :
        print("erasing")

point = Point();
point.draw()
point.erase()


class PointTwo :
    # constructor
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    # method
    def draw(self) :
        return "drawing"
    
    # method
    def erase(self) :
        return "erasing"


newPoint = PointTwo(10,20)

print(newPoint.x)
print(newPoint.y)
print(newPoint.draw())
print(newPoint.erase())

# ------------------------------------------------
# accessing the details from the instance of the class self is this in JS
class Person :
    # __init__ is constructor built in function
    def __init__(self, name):
        self.name = name

    def who(self):
        # accessing the name from which is set from the constructor function
        print(f"My name is {self.name}")
        return False
    
    def talk(self):
        print(f"Hello user, welcome to the page, I'm {self.name}")
        return False

person = Person("Naveen")

print(person.who())
print(person.talk())


