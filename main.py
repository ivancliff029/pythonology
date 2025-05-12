import db

class Payroll:
    payroll_db = db.initializeDatabase()
    def __init__(self,fullname:str, email, phone:int, amount:int, category:str):
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.amount = amount
        self.category = category
    def saveData(self):
        db.saveUserInfo(self.fullname,self.email,self.phone,self.amount,self.category)
    def getData(self):
        print(db.displayData())

    def __str__(self):
        return f'{self.fullname} {self.email} {self.phone} {self.amount} {self.category}'
    
# p1 = Payroll("Java Junior","java@allspacetechnologies.com","700567787","100000","programmer")
# p2 = Payroll("Ed Agaba","ed@allspacetechnologies.com","734455567","200000","programmer")
# p3 = Payroll("Elijah Owen","owen@allspacetechnologies.com","700567787","60000","seo")

# employees = [p1,p2,p3]
# for employee in employees:
#     employee.saveData()

p1 = Payroll("Java Junior","java@allspacetechnologies.com","700567787","100000","programmer")
print(p1.getData())
