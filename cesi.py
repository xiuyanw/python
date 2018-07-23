
# def foo():
#     x=15
#     print(x)
def bar():
    global x
    x=100
    print(x)

if __name__ == '__main__':
    # foo()
    bar()
print(x)

def bbb():
    len="hello"
    print(len)
bbb()