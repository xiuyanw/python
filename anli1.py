import getpass

userdb={}

def login():
    username = input("username: ")
    password = getpass.getpass("password: ")
    if userdb.get(username) !=password:  #如果用户名不存在，.get返回值为none，跟password不一致。
        print("\033[31;1mlogin failed,please register\033[0m")
    else:
        print("\033[32;1mlogin succeful\033[0m")

def register():
    username=input("username: ")
    if username in userdb:
        print("%s already exists." % username)
    else:
        password=input("password: ")
        userdb[username]=password


def show_menu():
    cmds = {'0':register, '1': login}
    prompt = '''(0) register
(1) login
(2) exit
please input your choice[0/1/2]:'''
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '012':
            print("invalid input.try again")
            continue
        if choice == '2':
            break
        cmds[choice]()


if __name__ == '__main__':
    try:
        show_menu()
    except IndexError:
        print("\033[31;1minput invalid\033[0m")
    except (KeyboardInterrupt,EOFError):
        print("bye")

