#coding=utf-8
from types import CodeType
from types import FunctionType
from opcode import opmap
from opcode import opname
import dis
def typcheck(v,typ):
    #print(v,typ)
    if isinstance(v,typ):
        return v
    else:
        raise TypeError("\n\t \033[0;31;43m Fail isinstance ({},{}) \033[0m".format(repr(v),typ.__name__))

def check(func):
    _globals_ = func.__globals__
    typs = func.__annotations__.copy()
    ret = typs.pop('return')
    _code_ = func.__code__
    o_varnames = list(_code_.co_varnames)
    o_names = list(_code_.co_names)
    o_consts = list(_code_.co_consts)
    n_consts = o_consts + list( set( list(typs.values()) + [ret]) ) + [typcheck]
    #print( "new consts:",n_consts )
    info = {}
    for k,v in typs.items():
        info[o_varnames.index(k)] = v
    o_binlst = list( _code_.co_code )
    o_argcount = _code_.co_argcount
    lst = [ ]
    n = o_argcount
    for i in range(n):
        lst += [opmap["LOAD_CONST"],len(n_consts)-1,
                opmap["LOAD_FAST"],i,
                opmap["LOAD_CONST"],n_consts.index( info[i] ),
                opmap["CALL_FUNCTION"],2,
                opmap["POP_TOP"],0 ]
    n = len(o_binlst) - 2
    #        ------------
    # func   ^ stack top 
    # result | 
    last = [ opmap["LOAD_CONST"],len(n_consts)-1,
             opmap["ROT_TWO"],0,# Swaps the two top-most stack items.
             opmap["LOAD_CONST"],n_consts.index( ret ),
             opmap["CALL_FUNCTION"],2
    ]
    while n < len(o_binlst) :
        t = o_binlst[n + 1]
        last += [o_binlst[n],t]
        n +=2

    o_binlst = o_binlst[0:len(o_binlst)-2]
    lstbin = lst + o_binlst + last
    code = CodeType(_code_.co_argcount,       # argcount
                    _code_.co_kwonlyargcount, # kwonlyargcount
                    _code_.co_nlocals,        # nlocals
                    _code_.co_stacksize,      # stacksize
                    _code_.co_flags,          # flags
                    bytes(lstbin),            # codestring
                    tuple(n_consts),          # consts
                    _code_.co_names,          # names
                    _code_.co_varnames,       # varnames
                    _code_.co_filename,       # filename
                    _code_.co_name,           # name
                    _code_.co_firstlineno,    # firstlineno
                    _code_.co_lnotab,         # lnotab
                    _code_.co_freevars,       # freevars
                    _code_.co_cellvars,       # cellvars
                )
    
    #dis.dis(code)
    #dis.show_code(code)
    #print( lstbin )
    return FunctionType(code,_globals_)

__all__ = ["check"]
