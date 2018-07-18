sum100=0
for i in range(1,101):
    sum100+=i
print(sum100)

fib_1=[0,1]
leng=int(input("please input a number:"))
for i in range(leng-len(fib_1)):
    fib_1.append(fib_1[-1]+fib_1[-2])
print(fib_1)
print(len(fib_1))