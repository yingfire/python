#!/usr/bin/python
#coding:utf-8
'''
doc(__doc__)
'''
#2017_02_07
'''
import demo
if __name__ == "__main__":
    print "相等"
else:
    print "不相等"


#输出当前文件的绝对路径+文件名
print __file__
#显示doc文件
print __doc__
'''
#2017_02_08

#函数
''''
def foo(name):
    print name, '去嫖娼'
'''
#foo('laowu')
#foo('wuyangyang')
'''
def login(username):
    if username == 'sb':
        return '登陆成功'
    else:
        return '滚'
def detail(user):
    print '光将军'

if __name__ == '__main__':
    user = raw_input('please enter you name:')
    #检查用户是否合法
    res = login(user)
    if res == '登陆成功':
        detail(user)
    else:
        print 'hehe,nimabi!'
'''
'''
#当有默认参数的时候,需要放到后面
def foo(name,action='chifan',where='bj'):
    print name,'去',action,where
foo('laowu','papa')
foo('gunag','zhuangbi')
foo('wuyangyang','piaochang')
foo('me',where='cq',action='kj')
#me 去 gg cq
'''
'''
#参数问题
def show1(arg):
    for item in arg:
        print item

def show2(arg1,arg2):
        print arg1,arg2


show1 (['batt'',''linux'])

show2 ('numb1','numb2')


#可以传多个参数,会包装成一个列表
def show(*arg):
    for item in arg:
        print item

show('1','2','3','4')
#传入的参数为一个字典
def show3(**kargs):
    for item in kargs.items():
        print item
show3(name='liubz',age='22')

#当传入的参数为字典时需要添加**
def show(**kargs):
    for item in kargs.items():
        print item
user_dict = {'k1':'123','k2':'234'}

show(**user_dict)
'''
'''
#xrange 只有进行迭代的时候才会创建,和xreadline相似
print range(10)
print xrange(10)

for item in xrange(10):
    print item

'''
'''
#yield
def foo():
    yield 1
    yield 2
    yield 3
    yield 4
re = foo()
print re
#<generator object foo at 0x0000000003528120>

for item in re:
    print item
'''

'''
f = open('D:/tmp.txt','r')
f.read()
f.close()
#等于下面

with open('D:/temp.txt','r') as f:
    print 'xxx'
'''
'''
def Readlines():
    seek = 0
    while True:
        with open('D:temp.txt','r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return

for item in Readlines():
    print item
'''
'''
#三元运算
temp = None
if 1>3:
    temp = 'gt'
else:
    temp = 'lt'
print temp

result = 'gt' if 1>3 else 'lt'

print result
'''
'''
#lambda表达式,匿名函数(当函数特别简单，不会被多次调用)
def foo(x,y):
    return x+y
print foo(4,10)


temp = lambda x,y:x+y
print temp(4,10)

[lambda x:x*2 for i in range(10)]
'''
#内置函数
#help()
#a = []
#help(a)
dir()
vars()
print dir()
print vars()
#['__builtins__', '__doc__', '__file__', '__name__', '__package__']
#{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__file__': '/project/python/python/2017_02_07/index.py', '__doc__': '\ndoc(__doc__)\n', '__package__': None}
#type()




















