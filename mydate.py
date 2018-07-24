class Date:
    def __init__(self,year,month,date):
        self.year=year
        self.month=month
        self.date=date

    @classmethod   #类方法不用创建实例即可调用，cls表示类本身。
    def create(cls,dstr):
        y,m,d=map(int,dstr.split('-'))
        dt=cls(y,m,d)
        return dt
    @staticmethod
    def is_data_valid(dstr):
        y,m,d=map(int,dstr.split('-'))
        return 1<=d<=31 and 1<=m<=12 and y<4000
if __name__ == '__main__':
    bith_date=Date(1995,12,5)
    print(bith_date.year)
    print(Date.is_data_valid('2000-5-4'))
    day=Date.create('2000-5-4')
    print(day.month)

