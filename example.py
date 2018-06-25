#coding=utf-8
from typecheck import *
import dis
@check
def add(a:int,b:int) -> int:
    " add : int * int -> int "
    return str(a) + str(b)
dis.dis(add)
print ( add )
help(add)
print ( add(1,2) )


