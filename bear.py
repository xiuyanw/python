class BearToy:
    def __init__(self,nm,color,size):
        """__init__在实例时自动执行，实例本身自动作为第一个参数传递给self"""
        self.color=color  #绑定属性到实例
        self.size=size
        self.name=nm
    def sing(self):
        print("lalala....")
    def speak(self):
        print("my name is %s" %self.name)
if __name__ == '__main__':
    tidy=BearToy("Tidy","orange","small") #调用__init__
    print(tidy.color)
    print(tidy.size)
    tidy.sing()
    tidy.speak()
