# f=open("/tmp/passwd")
# for line in f:
#     print(line,end='')
# f.close()

with open("/tmp/passwd") as f:

    print(f.readline(),end='')
    print(f.tell())

def pstar(num=30):
    print("*"*num)


pstar(10)

import star
print(star.hi)
print(star.pstar(30))