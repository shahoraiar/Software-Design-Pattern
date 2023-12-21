from abc import ABC , abstractmethod

class IChair(ABC) : 
    @abstractmethod
    def get_dimensions(self) : 
        pass

class SmallChair(IChair) : 
    def __init__(self, height , width , depth) : 
        self.height = height
        self.width = width
        self.depth = depth
    
    def get_dimensions(self):
        return {'height' : self.height , 
                'width' : self.width , 
                'depth' : self.depth}

class MediumChair(IChair) : 
    def __init__(self, height , width , depth) : 
        self.height = height
        self.width = width
        self.depth = depth
    
    def get_dimensions(self):
        return {'height' : self.height , 
                'width' : self.width , 
                'depth' : self.depth}
#   table
class ITable(ABC) : 
    @abstractmethod
    def get_dimensions(self) : 
        pass 

class SmallTable(ITable) : 
    def __init__(self, height , width , depth) : 
        self.height = height
        self.width = width
        self.depth = depth

    def get_dimensions(self):
        return {'height' : self.height , 
                'width' : self.width , 
                'depth' : self.depth}
    
    
class ChairFactory : 
    def get_chair(name) :
        height = input('enter heigth : ')
        width = input('enter width : ')
        depth = input('enter depth : ') 

        if name == 'schair' : 
            return SmallChair(height , width , depth)
        if name == 'mchair' : 
            return MediumChair(height , width , depth)

class TableFactory : 
    def get_table(name) : 
        if name == 'stable' : 
            height = input('enter heigth : ')
            width = input('enter width : ')
            depth = input('enter depth : ')

            return SmallTable(height , width , depth) 
        
        
class IFurnitureFactory(ABC) : 
    @abstractmethod
    def get_furniture(self) : 
        pass

class FurnitureFactory(IFurnitureFactory) : 
    def get_furniture(name):
        if name == 'CF' :
            name = input('enter (schair/mchair) : ') 
            return ChairFactory.get_chair(name)
        
        elif name == 'TF' : 
            name = input('enter (stable) : ')
            return TableFactory.get_table(name)
        
        else : 
            print("not have factory")

class Client : 
    factory_name = input('enter (CF/TF) : ')
    FF = FurnitureFactory.get_furniture(factory_name) # chairfactory()
    # furniture_name, FF = FurnitureFactory.get_furniture(factory_name)
    print(f"factory name : {factory_name}|| || {FF.get_dimensions()}")
    # print(f"Factory name: {factory_name} || Furniture name: {furniture_name} || Object Type: {type(FF)} || {FF.get_dimensions()}")
    
if __name__ == '__main__' : 
    Shahoraiar = Client()



