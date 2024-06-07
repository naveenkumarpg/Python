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



class Person :
    def name(self):
        print("name")
    
    def talk(self):
        print('Hello name')
