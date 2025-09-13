from employee import EmployeeDB

db=EmployeeDB()

db.add_employee(1,"Afzal","PGET")
db.add_employee(2,"Pravin","PGET")

db.check_in(1)
db.check_in(2)

db.check_out(1)
db.check_out(2)


db.show_attendance()
