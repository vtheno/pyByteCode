#coding=utf-8
from vtype import *
import dis

@check
def add(a:int,b:int) -> str:
    " add : int * int -> int "
    return str(a) + str(b)
#print ( add )
#help(add)
#dis.dis(add)
print ( add(1,2) )


@check
def tup(a:object,b:object) -> object:
    return (a,b)

#print( isinstance(tup,Arrow(Tuple(int,object),Tuple(int,object))) )
#print( tup(1,None) )


@check
def foldl( func : Arrow(Tuple(object,object),object),
           acc  : Tuple(int,object),
           lst  : List(int)  ) -> Tuple(int,object) :
    if lst == [ ]:
        return acc
    return foldl( func,func(lst[0],acc),lst[1:] )
print( "--------------------")
#dis.dis(foldl)
print( foldl( tup,(0,None),[5,4,3,2,1]) )

@check
def Sum(lst : List(int),acc :int) -> int :
    if lst == [ ]:
        return acc
    elif lst == [1]:
        return acc + 1 
    return Sum(lst[1:],acc + 1)
#dis.dis(Sum)
print( Sum( [1,2,3,4,5] ,0) )


