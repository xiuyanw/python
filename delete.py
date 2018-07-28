from dbconn import Departments,Employees,Session,Salary
session=Session()
# xz=Departments(dep_id=5,dep_name='行政部')
# session.add(xz)
dev=session.query(Departments).get(5)
session.delete(dev)
session.commit()
session.close()