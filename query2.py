from dbconn import Departments,Employees,Session,Salary
from sqlalchemy import and_,or_

session=Session()
# qset=session.query(Employees.name).filter(and_(Employees.dep_id==2,Employees.gender=='男'))
# # print(qset)
# for name in qset:
#     print(name)
#
# qset=session.query(Employees.name).filter(or_(Employees.dep_id==2,Employees.gender=='女'))
# print(qset)
# for name in qset:
#     print(name)
# qset=session.query(Employees.name,Employees.phone).filter(Employees.emp_id==2)
# print(qset.all())
# print(qset.first())
# print(qset.one())
# print(qset.scalar())
qset=session.query(Employees.name,Departments.dep_name).join(Departments,Employees.dep_id==Departments.dep_id)
print(qset.all())
session.close()