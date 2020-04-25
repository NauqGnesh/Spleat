import sys
import math

class Food:

    def __init__(self, name, fPrice):
        __price = fPrice
        self.__fName = name
        __personAte = 0

    @property
    def getPrice(self):
        return self.__price
    
    @getPrice.setter
    def getPrice(self, p):
        self.__price = p

    @property 
    def foodName(self):
        return self.__fName
    
    @foodName.setter
    def foodname(self, name):
        self.__fName = name
    
    @property
    def personAteIncrement(self):
        self.__personAte += 1