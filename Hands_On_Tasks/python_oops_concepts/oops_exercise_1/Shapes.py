''' Create a base class, Shape, with a single method, draw. 
    Implement two child classes, Elipse and Rectangle, that override the draw method. 
    And implement __str__ and __repr__.'''
    
class Shape:
    
    def draw(self):
        print("I will draw any Shape")
        
class Ellipse(Shape):
        
    def draw(self):
        print("I will draw Ellipse Only")
        
    def __str__(self):
        return "I'm __str__"
    
    def __repr__(self):
        return "I'm __repr__"
    
class Rectangle(Shape):
    
    def draw(self):
        print("I will draw Rectangle Only")


shape = Shape()
shape.draw()

ellipse = Ellipse()
ellipse.draw()
print(ellipse)
print(repr(ellipse))

rectangle = Rectangle()
rectangle.draw()