#coding=utf-8
from typecheck import *
import dis

@check
def add(a:int,b:int) -> str:
    " add : int * int -> int "
    return str(a) + str(b)
dis.dis(add)
print ( add )
help(add)
print ( add(1,2) )
class IntList(list): pass
@check
def Sum(lst : list) -> int:
    " Sum : int list -> int "
    if lst == [ ]:
        return 0
    return lst[0] + Sum( lst[1:] )

print( Sum )
help(Sum)
a = [1,2,3] 
dis.dis(Sum) 
print( Sum( a ) )
