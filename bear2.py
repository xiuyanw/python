class Vendor:
    def __init__(self,phone,email):
        self.phone=phone
        self.email=email
    def call(self):
        print("calling %s" % self.phone)


class BearToy:    #相当于一个玩具，有很多方面的属性，自身的属性，相关联的属性，如生产厂商的，购买用户的等等。
    def __init__(self,color,size,phone,email,name,age):
        self.color=color
        self.size=size
        self.vendor=Vendor(phone,email)
        self.user=User(name,age)

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

if __name__ == '__main__':
    bigbear=BearToy("red","big","0287856987","1273405387@qq.com","bob",23)
    print(bigbear.size)
    print(bigbear.color)
    print(bigbear.vendor.phone)
    print(bigbear.vendor.email)
    bigbear.vendor.call()
    print(bigbear.user.name)
    print(bigbear.user.age)