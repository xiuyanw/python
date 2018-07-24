class Hotel:
    def __init__(self,price=200,cutoff=1.0,br=15):
        self.price=price
        self.cutoff=cutoff
        self.br=br
    def cacl(self,days=1):
        return (self.price* self.cutoff+self.br)*days

if __name__ == '__main__':
    stdroom=Hotel()
    bigbed=Hotel(220,0.9)
    print(stdroom.cacl(2))
    print(bigbed.cacl(2))
