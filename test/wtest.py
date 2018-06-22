#coding=utf-8
import dis
import opcode
from types import CodeType
from types import FunctionType


def showCodeInfo(co):
    print( " --------start------- ")
    for i in dir(co):
        if i.startswith('co'):
            t = getattr(co,i)
            print( '  ',repr(t),'\t: (',i,':',type(t).__name__,')' )
    print( " ---------end--------- ")

code = compile('lambda x:x','<string>','exec')
lamc = code.co_consts[0]
showCodeInfo(code)
dis.dis(code)
showCodeInfo(lamc)
dis.dis(lamc)

dis.show_code(code)
dis.show_code(lamc)

# inspect.CO_OPTIMIZED             1
# inspect.CO_NEWLOCALS             2
# inspect.CO_VARARGS               4
# inspect.CO_VARKEYWORDS           8
# inspect.CO_NESTED               16
# inspect.CO_GENERATOR            32
# inspect.CO_NOFREE               64 
# inspect.CO_COROUTINE           128 
# inspect.CO_ITERABLE_COROUTINE  256
# inspect.CO_ASYNC_GENERATOR     512

def parseCo_Flags(num):
    pass
