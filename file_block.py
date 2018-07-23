def blocks(fobj):
    block=[]
    counter=0
    for line in fobj:
        block.append(line)
        counter+=1
        if counter==10:
            yield block   #停止执行，把数据返回给下面的lines，等到for循环继续，就清空block和counter,下次取值从这里继续执行。
            block=[]
            counter=0
    if block:          #如果block没有被清空，且不足10行时，把数据取出来。
        yield block


if __name__ == '__main__':
    fobj=open('/tmp/passwd')
    for lines in blocks(fobj):
        print(lines)
        print()
    fobj.close()