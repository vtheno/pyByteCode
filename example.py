#coding=utf-8
from typecheck import *

@check
def add(a:int,b:int) -> int:
    " add : int * int -> int "
    return a + b
print ( add )
help(add)
print ( add(1,'2') )
