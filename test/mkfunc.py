#coding=utf-8
import dis
import opcode
from types import CodeType
from types import FunctionType

def makelambda():
    varnames = ('a','b')
    lstbin = [ opcode.opmap["LOAD_FAST"],0,
               opcode.opmap["LOAD_FAST"],1,
               opcode.opmap["BINARY_ADD"],0,
               opcode.opmap["RETURN_VALUE"],0,]
    code = CodeType(2,                     # argcount
                    0,                     # kwonlyargcount
                    2,                     # nlocals
                    2,                     # stacksize
                    67,                    # flags
                    bytes(lstbin),         # codestring
                    tuple(),               # consts
                    tuple(),               # names
                    tuple(varnames),       # varnames
                    '<string>',            # filename
                    '<lambda>',            # name
                    1,                     # firstlineno
                    b'',                   # lnotab
                    tuple (),               # freevars
                    tuple (),              # cellvars
                )
    return FunctionType(code,globals())
add = makelambda()
print( add(1,2) )
