from dbconn import Salary,Session

zhangsan=Salary(auto_id=1,emp_id=1,date='2018-07-30',basic=5000,awards=1050)
lisi=Salary(auto_id=2,emp_id=2,date='2018-07-30',basic=5000,awards=1050)

session=Session()

session.add_all([zhangsan,lisi])
session.commit()
session.commit()