from abc import ABC , abstractmethod

class IChair(ABC) : 
    @staticmethod
    def get_dimensions(self) : 
        pass 

class SmallChair(IChair) : 
    def __init__(self , height , width , depth) :
        self.height = height
        self.width = width
        self.depth = depth
    def get_dimensions(self):
        return {'height' : self.height , 
                'width' : self.width,
                'depth' : self.depth}

class MediumChair(IChair) : 
    def __init__(self , height , width , depth) :
        self.height = height
        self.width = width
        self.depth = depth
    def get_dimensions(self):
        return {'height' : self.height , 
                'width' : self.width,
                'depth' : self.depth}
    
class BigChair(IChair) : 
    def __init__(self , height , width , depth) :
        self.height = height
        self.width = width
        self.depth = depth
    def get_dimensions(self):
        return {'height' : self.height , 
                'width' : self.width,
                'depth' : self.depth}
    
# table 
class ITable(ABC) : 
    @staticmethod
    def get_dimensions(self) : 
        pass 

class SmallTable(ITable) : 
    def __init__(self , height , width , depth) :
        self.height = height
        self.width = width
        self.depth = depth
    def get_dimensions(self):
        return {'height' : self.height , 
                'width' : self.width,
                'depth' : self.depth}

class MediumTable(ITable) : 
    def __init__(self , height , width , depth) :
        self.height = height
        self.width = width
        self.depth = depth
    def get_dimensions(self):
        return {'height' : self.height , 
                'width' : self.width,
                'depth' : self.depth}

class BigTable(ITable) : 
    def __init__(self , height , width , depth) :
        self.height = height
        self.width = width
        self.depth = depth
    def get_dimensions(self):
        return {'height' : self.height , 
                'width' : self.width,
                'depth' : self.depth}
    
#make factory
class ChairFactory : 
    def get_chair(name) : 
        height = input('enter chair height : ')
        width = input('enter chair width : ')
        depth = input('enter chair depth : ')

        if name == 'schair' : 
            return SmallChair(height , width , depth)
        elif name == 'mchair' : 
            return MediumChair(height , width , depth)
        elif name == 'bchair' : 
            return BigChair(height , width , depth)
        else : 
            print('not have chair')

class TableFactory : 
    def get_table(name) : 
        height = input('enter table height : ')
        width = input('enter table width : ')
        depth = input('enter table depth : ')

        if name == 'stable' : 
            return SmallTable(height , width , depth)
        elif name == 'mtable' : 
            return MediumTable(height , width , depth)
        elif name == 'btable' : 
            return BigTable(height , width , depth)
        else : 
            print('not have table')

# abstract furniture
class IFurnitureFactory(ABC) : 
    @abstractmethod
    def get_furniture() : 
        pass 

class FurnitureFactory(IFurnitureFactory) : 
    def get_furniture(self,name):
        if name == 'CF' : 
            choice = input('enter (schair/mchair/bchair) : ')
            return ChairFactory.get_chair(choice)
        elif name == 'TF' : 
            choice = input('enter (stable/mtable/btable) : ')
            return TableFactory.get_table(choice)
        else : 
            print('not have Furniture_Factory')

class Client :
    factory_name = input('enter (CF/TF) : ') 
    f = FurnitureFactory() 
    final = f.get_furniture(factory_name)

    if factory_name == 'CF' : 
        print (final.get_dimensions())
    elif factory_name == 'TF' : 
        print(final.get_dimensions())
    else : 
        print('wrong input')

if __name__ == '__main__' : 
    shaoraiar = Client()



