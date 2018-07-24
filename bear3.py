class BearToy:
    def __init__(self,nm,color,size):
        self.color=color
        self.size=size
        self.name=nm

    def sing(self):
        print("lalala...")
    def speak(self):
        print("hello world!! My name is %s" %self.name)

class NewBear(BearToy):
    def __init__(self,nm,color,size,date):
        super(NewBear,self).__init__(nm,color,size)
        self.date=date
    def run(self):
        print("running....")

if __name__ == '__main__':
    b1=NewBear("tom","red","small","2018-07-20")
    print(b1.color)
    print(b1.name)
    b1.sing()
    b1.run()
    b1.speak()
    print(b1.date)