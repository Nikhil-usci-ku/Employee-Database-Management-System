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
        self.cur.execute("select * from demographic_info;")
        result = self.cur.fetchall()
        return result
    
    def addemographicinfo(self,empid,dob,fname,mname,mob,address,pin,cty):
        cmd = f"insert into demographic_info values('{empid}','{dob}'"
        cmd+= f",'{fname}'" if fname!="" else ",null"
        cmd+= f",'{mname}'" if mname!="" else ",null"
        cmd+= f",{mob},'{address}',{pin}"
        cmd+= f",'{cty}');" if cty!="" else ",null);"
        try:
            self.cur.execute(cmd)
            self.db.commit()
        except mysql.connector.Error as Err:
            print(Err.msg.split("vttablet: ")[1].split(" (errno")[0])
            print(Err)

    def getemployee(self,getvar:str,BOOL:bool = False):
        self.cur.execute("select * from demographic_info where id='%s';" %getvar) if BOOL else self.cur.execute("select * from main_info where name like '%%%s%%';" %(getvar))
        return self.cur.fetchall()

    def delemployee(self,eid:str):
        self.cur.execute("select id from demographic_info where id='%s';" %eid)
        try:
            self.cur.fetchone()[0]
            self.cur.execute("delete from demographic_info where id='%s';" %eid)
            self.db.commit()
            return True
        except TypeError:
            return False
        

# A = midb()
# def getodinfo():
#     a = input("Unique ID* : ")
#     b = input("Date of Birth* : ")
#     c = input("Father's Name : ")
#     d = input("Mother's Name : ")
#     e = input("Mobile No* : ")
#     f = input("Address* : ")
#     g = input("Pincode* : ")
#     h = input("Country : ")
#     A.addemographicinfo(a,b,c,d,e,f,g,h)
# getodinfo()

# # A.run("SELECT * FROM main_info where name like '%Nikhil%';")
# A.viewtable()





