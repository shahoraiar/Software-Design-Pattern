from abc import ABC , abstractmethod

class Shape(ABC) : 
    @abstractmethod
    def calculate_area(self) : 
        pass 
    @abstractmethod
    def calculate_perimeter(self) : 
        pass

class Circle(Shape) : 
    def __init__(self , radius) : 
        self.radius = radius

    def calculate_area(self):
        return  self.radius * self.radius
    def calculate_perimeter(self):
        return 2 * 3.1416 * self.radius
    
class Color(ABC) : 
    @abstractmethod
    def fill(self) : 
        pass

class Red(Color) : 
    def fill(self):
        print(f"inside red:: fill() method")

class AbstractFactory(ABC) : 
    @abstractmethod
    def create_color(self , name) : 
        pass 
    @abstractmethod
    def create_shape(self , name) : 
        pass

class ShapeFactory(AbstractFactory) : 
    def create_shape(self, name):
        if name == 'circle' : 
            radius = input("enter radius : ")
            return Circle(float(radius))
        else : 
            print("no shape")

    def create_color(self, name):
        return None

class ColorFactory(AbstractFactory) : 
    def create_color(self, name):
        if name == 'red' : 
            return Red() 
        
        else : 
            print('no color')
    def create_shape(self, name):
        return None

class Factory : 
    @staticmethod
    def create_factory(choice) : 
        if choice == 'shape' : 
            return ShapeFactory()
        elif choice == 'color'  : 
            return ColorFactory()
        
def client() : 
    type = input('enter (shape/color) : ')
    type_factory = Factory.create_factory(type) #shapefactory()
    
    if type == 'shape' : 
        shape_name = input('enter the shape name(circle) : ')
        shape = type_factory.create_shape(shape_name) #circle : input
        print(f"the area of the {shape_name} is : {shape.calculate_area()}  ")
        print(f"the perimeter of the {shape_name} is : {shape.calculate_perimeter()}  ")
        
    elif type == 'color' : 
        color_name = input('enter color(red) : ')
        c = type_factory.create_color(color_name) #red()
        c.fill()

# if __name__ == '__main__': 
client()
