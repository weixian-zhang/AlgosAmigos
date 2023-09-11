

from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def create():
        pass
    

class ProductA(IProduct):
    
    def create(self):
        return 'A'
    
class productB(IProduct):
    def create(self):
        return 'B'
    
class Factory:
    
    def create_product(self, type):
        
        if type =='a':
            return ProductA()
        elif type =='b':
            return ProductA()