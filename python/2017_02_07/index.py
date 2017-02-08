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
#当有默认参数的时候,需要放到后面
def foo(name,action='chifan',where='bj'):
    print name,'去',action,where
foo('laowu','papa')
foo('gunag','zhuangbi')
foo('wuyangyang','piaochang')
foo('me',where='cq',action='kj')
#me 去 gg cq