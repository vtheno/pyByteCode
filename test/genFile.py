#coding=utf-8
import marshal
import struct
import time
import imp
import sys

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
                    'add',            # name
                    1,                     # firstlineno
                    b'',                   # lnotab
                    tuple (),               # freevars
                    tuple (),              # cellvars
                )
    return FunctionType(code,{})
def make():
    consts = [makelambda().__code__,'<func>',None]
    args   = [ ]
    names  = ['add',]
    lstbin = [ opcode.opmap["LOAD_CONST"],0,
               opcode.opmap["LOAD_CONST"],1,
               opcode.opmap["MAKE_FUNCTION"],0,
               opcode.opmap["STORE_FAST"],0,
               opcode.opmap["LOAD_FAST"],0,
               opcode.opmap["RETURN_VALUE"],0,]
    code = CodeType(0,                     # argcount
                    0,                     # kwonlyargcount
                    0,                     # nlocals
                    2,                     # stacksize
                    64,                    # flags
                    bytes(lstbin),         # codestring
                    tuple( consts ),       # consts
                    tuple( names ),        # names
                    tuple( args + names ), # varnames
                    '<string>',            # filename
                    '<nil>',               # name
                    1,                     # firstlineno
                    b'',                   # lnotab
                    tuple (),              # freevars
                    tuple (),              # cellvars
                )
    return FunctionType(code,{})
add = make()
print( add )
print( add() ) 
#"""
filename     = 'newfile.pyc'
magic_number = imp.get_magic()
gen_time     = struct.pack('i',int(time.time()))
padding      = bytes( [65,0,0,0] )
data         = marshal.dumps(add.__code__)
with open(filename,'wb') as f:
    f.write(magic_number)
    f.write(gen_time)
    f.write(padding)
    f.write(data)
#"""
