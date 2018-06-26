#coding=utf-8
from types import CodeType
from types import FunctionType
from opcode import opmap
from opcode import opname
import dis
def typcheck(v,typ):
    #print( "typcheck:",v,type(v),typ)
    if isinstance(v,typ):
        #print( v, typ )
        return v
    else:
        raise TypeError("\n\t \033[0;31;43m Fail isinstance ({},{}) \033[0m".format(repr(v),repr(typ)))

def check(func):
    _globals_ = func.__globals__
    temp = {}
    old_annotations = {}
    temp.update(func.__annotations__)
    old_annotations.update(func.__annotations__)
    typs = temp
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
    mlst = [ ]
    n = o_argcount
    for i in range(n):
        mlst += [opmap["LOAD_CONST"],len(n_consts)-1,
                opmap["LOAD_FAST"],i,
                opmap["LOAD_CONST"],n_consts.index( info[i] ),
                opmap["CALL_FUNCTION"],2,
                opmap["POP_TOP"],0 ]
    jumps = [opmap["POP_JUMP_IF_FALSE"],
             opmap["POP_JUMP_IF_TRUE"],
             opmap["JUMP_IF_TRUE_OR_POP"],
             opmap["JUMP_IF_FALSE_OR_POP"],
             opmap["JUMP_ABSOLUTE"]]
    jump_forward = opmap["JUMP_FORWARD"]
    OffSet = len(mlst)
    #        ------------
    # func   ^ stack top 
    # result | 
    last = [ opmap["LOAD_CONST"],len(n_consts)-1,
             opmap["ROT_TWO"],0,# Swaps the two top-most stack items.
             opmap["LOAD_CONST"],n_consts.index( ret ),
             opmap["CALL_FUNCTION"],2,
             opmap["RETURN_VALUE"],0]
    new_binlst = o_binlst
    lset = len(last) - 2
    old_addrs = list()
    for i in range(len(o_binlst)):
        if o_binlst[i] in jumps:
            old_addrs+= [ o_binlst[i+1] ]
    lst = new_binlst
    for i in old_addrs:
        new_binlst[i] = [-1,new_binlst[i]]
        new_binlst[i+1] = [-1,new_binlst[i+1]]
    acc = [ ]
    while lst :
        op,arg = lst[0],lst[1]
        if op == opmap["RETURN_VALUE"]:
            acc += last
        else:
            acc += [op,arg]
        lst = lst[2:]
    new_binlst = mlst + acc

    new_addrs = list()
    for i in range(len(new_binlst)):
        op = new_binlst[i]
        if isinstance(op,list):
            new_addrs += [i]
            new_binlst[i] = new_binlst[i][1]
            new_binlst[i+1] = new_binlst[i+1][1]
    for i in range(len(new_binlst)):
        op = new_binlst[i]
        if op in jumps:
            new_binlst[i+1] = new_addrs[0]
            new_addrs = new_addrs[1:]

    lstbin = new_binlst
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
    func  = FunctionType(code,_globals_)
    func.__annotations__= old_annotations
    return func

__all__ = ["check"]
