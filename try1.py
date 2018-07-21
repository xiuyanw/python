try:
    n = int(input("number: "))   #容易发生异常的语句
    result =100/n

except (ValueError,ZeroDivisionError):
    print('invalid number')

except (KeyboardInterrupt,EOFError):   #可以合并写。要用括号扩起来，中间用逗号分隔。
    print("\nbye")
else:
    print(result)    #异常不发生时执行else.
finally:
    print("Done")
#不管异常是否发生都必须执行的语句。，比如对文件打开时候，如果发生异常可能导致文件没有被关闭，可以把关闭程序放在finally。