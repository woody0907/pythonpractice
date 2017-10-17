__author__ = 'woody'
from oop.SecondClass import SecondClass
class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data+other)

    def __str__(self):
        return '[ThirdClass:%s]' % self.data

    def mul(self,other):
        self.data *= other

if __name__ == '__main__':
    t = ThirdClass("Hello")
    t.display()
    print(t)
    b = t+" World"
    b.display()
    t.mul(3)
    print(t)
