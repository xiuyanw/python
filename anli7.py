import time
import pickle
dt=time.strftime('%Y-%m-%d')
with open('/tmp/qianbao','wb') as fobj:
    pickle.dump(10000,fobj)

    alist = ["时间", "收入", "开销", "余额", "说明"]
    data = ('%-10s%-10s%-10s%-10s%-10s' % (alist[0], alist[1], alist[2], alist[3], alist[4]))
    with open('/tmp/jilu','wb') as fobj:
        pickle.dump(data,fobj)
def kaixiao():
    try:
        number=int(input("请输入开销的金额："))
        shuoming=input("请输入说明：")
    except ValueError:
        print('invalid number')
    except (KeyboardInterrupt, EOFError):
        print("\nbye")
    with open('/tmp/qianbao', 'rb') as afobj:
        yue = pickle.load(afobj)
        yue -= number
        with open('/tmp/qianbao', 'wb') as bfobj:
            pickle.dump(yue, bfobj)
    data=("%-20s%-10s%-10s%-10s%-10s" % (dt,'',number,yue,shuoming))
    with open('/tmp/jilu','ab') as fobj:
        pickle.dump(data,fobj)
def shouru():
    try:
        number=int(input("请输入收入的金额："))
        shuoming=input("请输入说明：")
    except ValueError:
        print('invalid number')
    except (KeyboardInterrupt, EOFError):
        print("\nbye")
    with open('/tmp/qianbao', 'rb') as afobj:
        yue = pickle.load(afobj)
        yue += number
        with open('/tmp/qianbao', 'wb') as bfobj:
            pickle.dump(yue, bfobj)

    data=("%-20s%-10s%-10s%-10s%-10s" % (dt,number,'',yue,shuoming))
    with open('/tmp/jilu','ab') as fobj:
        pickle.dump(data,fobj)
def chaxun():
    with open('/tmp/jilu','rb') as  fobj:
        while True:
            try:
                data = pickle.load(fobj)
            except EOFError:
                break
            if data:
                print(data)
def show_menu():
    cmds={'0':kaixiao,"1":shouru,"2":chaxun}
    prompt="""(0)  开销
(1)  收入
(2)  查询
(3)  退出
请输入你的选择[0/1/2/3]："""
    while True:
        choice=input(prompt)
        if choice not in '0123':
            print("input invalid!!")
        if choice=='3':
            break
        cmds[choice]()

if __name__ == '__main__':
    show_menu()