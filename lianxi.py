from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine(
    'mysql+pymysql://root:tedu.cn@localhost/tarena',
    encoding='utf8',
    echo=True

)
Base=declarative_base()

class Departments(Base):
    __tablename__='departments'
    dep_id=Column(Integer,primary_key=True)
    dep_name=Column(String(20),nullable=False,unique=True)

    def __str__(self):
        return '[部门ID：%s,部门名称：%s]' %(self.dep_id,self.dep_name)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
