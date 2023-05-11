import mysql.connector
from  mysql.connector import errorcode
HOST = "aws.connect.psdb.cloud"
USER = "qh0ae2v6u97o4pg9hkdi"
PASS = "pscale_pw_VaZ7EuD1PTBp6i2SoHKbLXINXscUk8Li30bDV5nryH"
DBNM = "pyproject"


class midb():
    def __init__(self):
        self.db = mysql.connector.connect(host=HOST,user=USER,password=PASS,database=DBNM)
        self.cur = self.db.cursor()


    def viewtable(self):
        self.cur.execute("select * from main_info;")
        result = self.cur.fetchall()
        return result
    
    def addemployee(self,empid,fname,jdate,div,pos):
        try:
            self.cur.execute("insert into main_info values('%s','%s','%s','%s','%s');" %(empid,fname,jdate,div,pos))
            self.db.commit()
            return True
        except mysql.connector.Error as Err:
            print(Err.msg.split("vttablet: ")[1].split(" (errno")[0])
            return False

    def getemployee(self,getvar:str,BOOL:bool = False):
        self.cur.execute("select * from main_info where id='%s';" %getvar) if BOOL else self.cur.execute("select * from main_info where name like '%%%s%%';" %(getvar))
        return self.cur.fetchall()

    def delemployee(self,eid:str):
        self.cur.execute("select id from main_info where id='%s';" %eid)
        try:
            self.cur.fetchone()[0]
            self.cur.execute("delete from main_info where id='%s';" %eid)
            self.db.commit()
            return True
        except TypeError:
            return False


    def updateemployee(self,eid:str):
        pass
    

    def run(self,cmd):
        self.cur.execute(cmd)
        result = self.cur.fetchall()
        print(*[i for i in result],sep="\n")
        self.db.commit()
        

A = midb()
# def getinfo():
#     a = input("Unique ID : ")
#     b = input("Name : ")
#     c = input("Join date : ")
#     d = input("Division : ")
#     e = input("Position : ")
#     A.addemployee(a,b,c,d,e)
# getinfo()

# # # A.run("SELECT * FROM main_info where name like '%Nikhil%';")
# # # A.run("describe main_info;")
# print(A.viewtable())
# # print(A.delemployee("000"))

# A.run("delete from main_info;")
# A.run("delete from finance_info;")
# A.run("delete from demographic_info;")

A.run("select * from main_info;")
A.run("select * from finance_info;")
A.run("select * from demographic_info;")