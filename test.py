#coding=utf-8
import dis
from let import let
@let( {'a' : 1 ,'b':2} )
def add():
    c = a + b
    return c + a + b 
print( '1+2+1+2', add() )

#print( 'add' )
#dis.dis(add)
#print( 'end' )
def app():
    a = 1
    b = 2
    c = a + b
    return c + a + b
print( app() )
#print( 'app' )
#dis.dis(app)
#print( 'end' )
def acc():
    c = a + b
    return c + a + b
import timeit
t = 100#0#0000
t1 = timeit.timeit('add()',globals={'add':add},number=t)
t2 = timeit.timeit('add()',globals={'add':app},number=t)
t3 = timeit.timeit('add()',globals={'add':acc,'a':1,'b':2},number=t)
print( t1 * 1000000 )
print( t2 * 1000000 )
print( t3 * 1000000 )
