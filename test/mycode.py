#coding=utf-8
import dis
import opcode
from types import CodeType
"""
CodeType(
        argcount,             #   integer
        kwonlyargcount,       #   integer
        nlocals,              #   integer
        stacksize,            #   integer
        flags,                #   integer
        codestring,           #   bytes
        consts,               #   tuple
        names,                #   tuple
        varnames,             #   tuple
        filename,             #   string
        name,                 #   string
        firstlineno,          #   integer
        lnotab,               #   bytes
        freevars,             #   tuple
        cellvars              #   tuple
        )
"""

def code():
    return a + 1

dis.dis(code.__code__)
co_code = code.__code__.co_code
print( co_code,type(co_code) )
l1 = [i for i in co_code]
print( l1 )
l2 = [124] + [i for i in l1[1:]]
co_code2 = bytes(l2)
print( l2 ,co_code2 )


code = 'x + 2'
a = compile(code,'<string>','eval')
def showCodeInfo(co):
    print( " --------start------- ")
    for i in dir(co):
        if i.startswith('co'):
            t = getattr(co,i)
            print( '  ',repr(t),'\t: (',i,':',type(t).__name__,')' )
    print( " ---------end--------- ")
dis.dis(a)
bincode = a.co_code

print( a.co_names,a.co_consts )
lstbin = [i for i in bincode]
print( bincode,lstbin )
print( opcode.opmap['LOAD_CONST'] )
print( opcode.opmap['STORE_NAME'] )


def f(x):
    return x
    
dis.dis(f)

m = CodeType(0,            # argcount
             0,            # kwonlyargcount
             0,            # nlocals
             2,            # stacksize
             64,           # flags
             bytes(lstbin),# codestring
             (66,),        # consts
             ('x',),       # names
             tuple(),      # varnames
             '<string>',   # filename
             'm',    # name
             1,            # firstlineno
             b'',          # lnotab
             tuple(),      # freevars
             tuple(),      # cellvars
)
print( m )
x = 0
print( eval(m) )
print( m )
d = compile('a = 2','<string>','exec')
showCodeInfo(d)
dis.dis(d)
print( list(d.co_code) )
lstbin = [opcode.opmap["LOAD_CONST"],0,
          opcode.opmap["STORE_NAME"],0,
          opcode.opmap["LOAD_NAME"],0,
          opcode.opmap["RETURN_VALUE"],0]
print(lstbin)
c = CodeType(0,            # argcount
             0,            # kwonlyargcount
             0,            # nlocals
             2,            # stacksize
             64,           # flags
             bytes(lstbin),# codestring
             (66,None),        # consts
             ('x',),       # names
             tuple(),      # varnames
             '<string>',   # filename
             'm',    # name
             1,            # firstlineno
             b'',          # lnotab
             tuple(),      # freevars
             tuple(),      # cellvars
)
print( eval(c) )
showCodeInfo(c)
def setf(variable,value):
    temp = value
    variable = temp
    return variable
dis.dis(setf)
showCodeInfo(setf.__code__)
lstbin = [opcode.opmap["LOAD_FAST"],1,
          opcode.opmap["STORE_FAST"],0,
          opcode.opmap["LOAD_FAST"],0,
          opcode.opmap["RETURN_VALUE"],0]

s = CodeType(2,            # argcount
             0,            # kwonlyargcount
             2,            # nlocals
             1,            # stacksize
             67,           # flags
             bytes(lstbin),# codestring
             (None,),        # consts
             tuple(),       # names
             ('variable','value'),      # varnames
             '<string>',   # filename
             'setv',    # name
             1,            # firstlineno
             b'',          # lnotab
             tuple(),      # freevars
             tuple(),      # cellvars
)
from types import FunctionType
ss = FunctionType(s,# code
                  globals(),# globals
              )
print( "----------" )
print( ss(a,1) )


