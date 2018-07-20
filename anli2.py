import  string
import keyword
import sys
def check_id(idt):
    first_list = string.ascii_letters + '_'
    all_list=first_list+string.digits

    if  keyword.iskeyword(idt):
        return "%s is keyword" %idt
    if idt[0] not in first_list:
        return "1st invalid"

    for ind,val in enumerate(idt[1:]):
        if val not in all_list:
            return  'char in postion #%s invalid'% (ind+2)

    return "%s is valid" % idt

if __name__=="__main__":
    print(check_id(sys.argv[1]))
