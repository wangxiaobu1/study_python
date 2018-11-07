# -*- coding:utf-8 -*-


"""
可变长度的参数
*args 用来将参数打包成tuple给函数体调用
      1.参数打包成tuple
      2.tuple解包成参数
**kwargs 打包关键字参数成dict给函数体调用
      1.参数打包成dict
      2.dict解包成参数
使用顺序some_func(fargs, *args, **kwargs)
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

def case4(**kwargs):
    print kwargs, type(kwargs)

def case5():

    def fun_all(fun, **kwargs):
        fun(**kwargs)

    def fun1(args1, args2, args3):
        print "args1:%s" %args1
        print "args2:%s" %args2
        print "args3:%s" % args3
    def fun2(args1):
        print args1.keys()
    fun_all(fun1,args1=1,args2=2,args3=3)

def case6():
    def test_args_kwargs(arg1, arg2, arg3):
        print("arg1:", arg1)
        print("arg2:", arg2)
        print("arg3:", arg3)

    args = ("two", 3, 5)
    test_args_kwargs(*args)

    kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
    test_args_kwargs(**kwargs)


if __name__ == '__main__':
    case5()