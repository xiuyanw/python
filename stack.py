
stack=[]
def push_it():
    item=input("item to push:")
    stack.append(item)
    print("\033[32;1m%s added to the list\033[0m" % item)

def pop_it():
    if stack:
        print("\033[31;1mfrom stack popped %s\033[0m" %stack.pop())


def view_it():
    print(stack)


def show_menu():
    cmds = {'0':push_it,'1':pop_it,'2':view_it}   #定义一个字典，把函数放在字典中，不加().加了()就成调用函数了，那么0对应的就是函数的返回值了。
    prompt = '''(0)  push it
(1) pop it
(2) view it
(3)exit
please input you choice(0/1/2/3):'''
    while True:
        choice = input(prompt).strip()[0]   #.strip去除两端空白。再取下标为0的字符。
        # if len(choice)==0:
        #     print("Invalid input.Try again.")
        #     continue
        if choice not in '0123':
            print('Invalid input. Try again.')
            continue
        if choice=='3':
            break
        cmds[choice]()   #调用上面的字典，通过key取value。相当于shell中的case语句.



if __name__ == "__main__":
    try:
        show_menu()
    except IndexError:
        print("input invalid")
