from random import choice
import string
all_ch=string.ascii_letters+string.digits#+string.punctuation

def gen_pass(n=8):
    result=''
    for i in range(n):
        ch=choice(all_ch)
        result+=ch
    return result




if __name__=='__main__':
    print(gen_pass())

