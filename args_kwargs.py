# -*- coding:utf-8 -*-


"""
可变长度的参数
*args 用来将参数打包成tuple给函数体调用
      1参数打包成tuple
      2tuple解包成参数
**kwargs 打包关键字参数成dict给函数体调用
"""

def case1(*args):
    print args, type(args)

def case2(x,y,*args):
    print x, y, args

def case3():
    def fun_all(fun, *args):
        a = args
        print a
        fun(*a)

    def fun1(args1):
        print "fun1:{0}".format(args1)

    def fun2(args1,args2):
        print "fun2:{0},{1}".format(args1,args2)

    fun_all(fun1,1)
    fun_all(fun2,1,2)

if __name__ == '__main__':
    case3()