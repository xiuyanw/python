class A:
    def foo(self):
        print("in A foo")
    def hello(self):
        print("hello A")
class B:
    def bar(self):
        print("in B bar")
    def nihao(self):
        print("hello B")

class C(B,A):
    pass

if __name__ == '__main__':
    c=C()
    c.foo()
    c.bar()
    c.hello()
    c.nihao()
