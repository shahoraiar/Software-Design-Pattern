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
        return 3.1416 * self.radius * self.radius
    
    def calculate_perimeter(self):
        return 2 * 3.1416 * self.radius
    
class Square(Shape) : 
    def __init__(self , length) :
        self.length = length

    def calculate_area(self):
        return self.length * self.length
    
    def calculate_perimeter(self):
        return 0.5 * self.length * self.length
    
#color   
class Color(ABC) : 
    @abstractmethod
    def Fill(self) : 
        pass
    
class Red(Color) : 
    def Fill(self) :
        return "Inside Red::fill() Method"

class Blue(Color) : 
    def Fill(self) :
        print("Inside Blue::fill() Method")

class AbstractFactory(ABC) : 
    @abstractmethod
    def create_shape() : 
        pass 
    @abstractmethod
    def create_color() : 
        pass 

class ShapeFactory(AbstractFactory) : 
    def create_shape(name):
        if name == 'circle' : 
            radius = input("enter radius : ")
            return Circle(float(radius))
        
        elif name == 'square' : 
            length = input("enter length : ")
            return Square(float(length))
        
        else : 
            print("not have a shape")
    def create_color():
        return None
    
class ColorFactory(AbstractFactory) : 
    def create_color(name):
        if name == 'red' : 
            return Red()
        
        elif name == 'blue' : 
            return Blue() 
        
        else : 
            print("not have a color")
    def create_shape():
        return None
    

class Factory : 
    @staticmethod
    def create_factory(name) : 
        if name == 'SF' : 
            shape_name = input('enter shape name(circle/square) : ')
            return ShapeFactory.create_shape(shape_name) 
        elif name == 'CF' : 
            color_name = input('enter color name(red/blue) : ')
            return ColorFactory.create_color(color_name)
        
def Client() : 
    factory_name = input('enter factory name (SF/CF) : ')

    factory = Factory() 
    f = factory.create_factory(factory_name) #ShapeFactory()
    
    if factory_name == 'SF' : 
        print(f"{f.calculate_area()}")
        print(f.calculate_perimeter())
    elif factory_name == 'CF' : 
        print(f.Fill())
        
if __name__ == '__main__' : 
    Client()
        


