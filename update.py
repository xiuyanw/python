from dbconn import Departments,Employees,Session,Salary
session=Session()

ops=session.query(Departments).filter(Departments.dep_id==2)
print(ops)
ops.update({Departments.dep_name:'运维部'})
dev=session.query(Departments).get(3)
dev.dep_name="开发部"

session.commit()
session.close()