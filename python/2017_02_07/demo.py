#coding:-utf-8
# #print __name__

def foo():
    print 'foo'
    bar()
def bar():
    print 'bar'


if __name__== '__main__':
    foo()
else:
    print '滚'
