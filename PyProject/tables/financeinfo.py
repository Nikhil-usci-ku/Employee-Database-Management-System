import mysql.connector
from  mysql.connector import errorcode
HOST = "aws.connect.psdb.cloud"
USER = "qh0ae2v6u97o4pg9hkdi"
PASS = "pscale_pw_VaZ7EuD1PTBp6i2SoHKbLXINXscUk8Li30bDV5nryH"
DBNM = "pyproject"

class empdbms():
    def __init__(self):
        self.db = mysql.connector.connect(host=HOST,user=USER,password=PASS,database=DBNM)
        self.cur = self.db.cursor()


    def viewtable(self,tablename):
        self.cur.execute(f"select * from {tablename};")#finance_info
        result = self.cur.fetchall()
        return result
    
    def viewalltables(self):
        self.cur.execute("select * from main_info,finance_info,demographic_info;")
        result = self.cur.fetchall()
        return result
A = empdbms()
print(*[i for i in A.viewalltables()])





class fidb():
    def __init__(self):
        self.db = mysql.connector.connect(host=HOST,user=USER,password=PASS,database=DBNM)
        self.cur = self.db.cursor()


    def viewtable(self):
        self.cur.execute("select * from finance_info;")
        result = self.cur.fetchall()
        return result
    
    def addesalary(self,empid,pay,ldate,bonus):
        cmd = f"insert into finance_info values('{empid}','{pay}'"
        cmd+= f",'{ldate}'" if ldate!="" else ",null"
        cmd+= f",{bonus});" if bonus!="" else ",null);"
        try:
            self.cur.execute(cmd)
            self.db.commit()
        except mysql.connector.Error as Err:
            print(Err.msg.split("vttablet: ")[1].split(" (errno")[0])

    def getemployee(self,getvar:str,BOOL:bool = False):
        self.cur.execute("select * from finance_info where id='%s';" %getvar) if BOOL else self.cur.execute("select * from main_info where name like '%%%s%%';" %(getvar))
        return self.cur.fetchall()

    def delemployee(self,eid:str):
        self.cur.execute("select id from finance_info where id='%s';" %eid)
        try:
            self.cur.fetchone()[0]
            self.cur.execute("delete from finance_info where id='%s';" %eid)
            self.db.commit()
            return True
        except TypeError:
            return False
    

A = fidb()
# A.delemployee("qe221")
# def getpay():
#     a = input("Unique ID : ")
#     b = input("Pay : ")
#     c = input("Last Pay : ")
#     d = input("Bonus : ")
#     A.addesalary(a,b,c,d)

# # getpay()

# # A.run("SELECT * FROM main_info where %';")
print(A.viewtable())



