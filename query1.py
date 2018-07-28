from dbconn import Departments,Employees,Session,Salary
session=Session()
# qset=session.query(Departments).order_by(Departments.dep_id)
# print(qset)
# for dep in qset:
#     print('%s:%s'%(dep.dep_id,dep.dep_name))

# qset=session.query(Employees.name,Employees.phone)
# print(qset)
# for name,phone in qset:
#     print('%s:%s'%(name,phone))
# qset=session.query(Departments.dep_name.label('部门'))
# print(qset)
# for row in qset:
#     print(row.部门)
# qset=session.query(Employees.name,Employees.email).order_by(Employees.emp_id)[2:4]
# print(qset)#qset因为切片的原因,已经是元组组成的列表了.不再是sql语句了.
# qset=session.query(Employees.name).filter(Employees.dep_id>1).filter(Employees.gender=='女')
# # print(qset)
# for name in qset:
#     print(name)

# session.close()