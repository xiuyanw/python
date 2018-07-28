from dbconn import Employees,Session

zhangsan=Employees(emp_id=1,name='张三',gender="男",phone='13311530548',email='1273405387@qq.com',dep_id=1)
lisi=Employees(emp_id=2,name='李四',gender="男",phone='13311530555',email='1273405387@qq.com',dep_id=2)
harry=Employees(emp_id=3,name='harry',gender="女",phone='13311530555',email='1273405387@qq.com',dep_id=3)
alice=Employees(emp_id=4,name='alice',gender="女",phone='13311530555',email='1273405387@qq.com',dep_id=4)

session=Session()
session.add_all([zhangsan,lisi,harry,alice])
session.commit()
session.close()

