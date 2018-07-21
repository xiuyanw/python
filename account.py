import time
import pickle
import os


def cost(wallet,record):
    try:
        amount=float(input("amount: "))
        comment=input("comment: ")
    except (KeyboardInterrupt,EOFError):
        print("bye-bye")
        choice='3'
    date = time.strftime('%Y-%m-%d')
    with open(wallet,'rb') as fobj:
        balance=pickle.load(fobj) - amount
    with open(wallet,'wb') as fobj:
        pickle.dump(balance,fobj)
    with open(record,'a') as fobj:
        fobj.write(
            '%-12s%-88.2f%-8s%-10s%-20s\n' % (date,amount,'',balance,comment)
        )
def save(wallet,record):
    amount=float(input("amount: "))
    comment=input("comment: ")
    date = time.strftime('%Y-%m-%d')
    with open(wallet,'rb') as fobj:
        balance=pickle.load(fobj) + amount
    with open(wallet,'wb') as fobj:
        pickle.dump(balance,fobj)
    with open(record,'a') as fobj:
        fobj.write(
            '%-12s%-8s%-88.2f%-10s%-20s\n' % (date,'',amount,balance,comment)
        )
def query(wallet,record):
    print(
        '%-12s%-8s%-8s%-10s%-20s' % ("date","cost","save","balance","comment")
    )
    with open(record) as fobj:
        for line in fobj:
            print(line,end='')
    with open(wallet,'rb') as fobj:
        balance=pickle.load(fobj)
        print("Latest Balance: %d" % balance)

def show_menu():
    cmds={'0':cost,"1":save,"2":query}
    prompt="""(0) cost
(1) save
(2) query
(3) exit
please input your choice(0/1/2/3): """
    wallet='wallet.data'    #在这来定义参数，那么另外另外的脚本要引用这个模块中的函数时，好调用。
    record='record.txt'
    if not os.path.exists(wallet):    #加个判断，如果文件不存在才写入10000，如果文件存在，就不做操作，这样解决了每次运行文件就初始化为10000
        with open(wallet,'wb') as fobj:
            pickle.dump(10000,fobj)
    while True:
        try:
            choice=input(prompt).strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt,EOFError):
            print()
            choice='3'   #如果用户选择了ctrl+c或者ctrl+d，就当选择了3
        if choice not in '0123':
            print("Invalid input.Try again.")
            continue
        if choice=='3':
            break
        cmds[choice](wallet,record)



if __name__ == '__main__':
    show_menu()