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

class let(object):
    def __init__(self,env):
        self.env = env
    def genCode(self,old_const,old_varnames):
        length_c = len(list(old_const))
        length_v = len(list(old_varnames))
        code = [ ]
        keys = list(self.env.keys())
        for i in range(len(keys)):
            code += [opcode.opmap["LOAD_CONST"],length_c + i,
                     opcode.opmap["STORE_FAST"],length_v + i]
        return code
    def processGlobals(self,lst,names,varnames):
        #print( lst )            # LOAD_GLOBAL => 116
        #print( names )
        ts = list(filter( lambda i: lst[i] == opcode.opmap["LOAD_GLOBAL"] ,range(len(lst))))
        #print( ts )
        #print( t!=None )
        for t in ts:
            i = lst[t+1]
            #print(i)
            if self.env.get(names[i]) :
                if lst[t] == opcode.opmap["LOAD_GLOBAL"]:
                    lst[t] = opcode.opmap["LOAD_FAST"]
                    lst[t+1] = varnames.index(names[i])
        return lst
    def __call__(self,func):
        self.func = func
        _globals_ = func.__globals__
        _code_ = func.__code__
        varnames  = list(_code_.co_varnames) + [v for v in self.env.keys()]
        nlocals   = len(varnames)
        binlst = list(_code_.co_code)
        lstbin = self.processGlobals(binlst,_code_.co_names,varnames)
        genCo = self.genCode(_code_.co_consts,_code_.co_varnames)
        lstbin = genCo + lstbin
        consts = list(_code_.co_consts) + [v for v in self.env.values()] 
        code = CodeType(_code_.co_argcount,       # argcount
                        _code_.co_kwonlyargcount, # kwonlyargcount
                        nlocals,                  # nlocals
                        _code_.co_stacksize,      # stacksize
                        _code_.co_flags,          # flags
                        bytes(lstbin),            # codestring
                        tuple(consts),            # consts
                        _code_.co_names,          # names
                        tuple(varnames),          # varnames
                        _code_.co_filename,       # filename
                        _code_.co_name,           # name
                        _code_.co_firstlineno,    # firstlineno
                        _code_.co_lnotab,         # lnotab
                        _code_.co_freevars,       # freevars
                        _code_.co_cellvars,       # cellvars
                    )
        #_globals_.update(self.env)
        function = FunctionType(code,_globals_)
        return function
    def __repr__(self):
        return "Where ({}) => {}".format(self.env,self.func)
def example():
    @let({'a':666})
    def test():
        return a
        
    dis.dis(test)
    showCodeInfo(test.__code__)
    print( test )
    print( test() )
__all__ = ["let"]

