def color(func):
    def red(*args):
        return '\033[31;1m%s\033[0m' % func(*args)   #%s为函数执行的结果
    return red
@color
def hello(word):
    return "hello %s!!" % word
@color
def welcome():
    return "how are you"
if __name__ == '__main__':
    # hello=color(hello) #此种写法可以换成为welcome加上@color的写法
    print(hello('China'))


    print(welcome())  #welcome因为有装饰器，所以调用时不是调用welcome
    #而是相当于color(welcome)()
    #color(welcome)返回red，color(welcome)()
    #等价于red()
