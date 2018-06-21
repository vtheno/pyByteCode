#coding=utf-8
from let import let
@let( {'a' : 1 ,'b':2} )
def add():
    c = a + b
    return c + a + b 
print( add() )
