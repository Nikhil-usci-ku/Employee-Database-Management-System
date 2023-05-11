import mysql.connector

HOST = "aws.connect.psdb.cloud"
USER = "qh0ae2v6u97o4pg9hkdi"
PASS = "pscale_pw_VaZ7EuD1PTBp6i2SoHKbLXINXscUk8Li30bDV5nryH"
DBNM = "pyproject"

class empdbms():
    def __init__(self):
        self.db = mysql.connector.connect(host=HOST,user=USER,password=PASS,database=DBNM)
        self.cur = self.db.cursor()


    def viewtable(self,info:str):
        self.cur.execute(f"select * from main_info left join finance_info on main_info.id = finance_info.id left join demographic_info on finance_info.id = demographic_info.id where main_info.id = '{info}';")
        result = self.cur.fetchall()
        if result != []:
            return result
        self.cur.execute(f"select * from main_info left join finance_info on main_info.id = finance_info.id left join demographic_info on finance_info.id = demographic_info.id where main_info.name like '%{info}%';")
        result = self.cur.fetchall()
        return result
    
    def viewalltables(self):
        self.cur.execute("select * from main_info left join finance_info on main_info.id = finance_info.id left join demographic_info on finance_info.id = demographic_info.id group by main_info.id;")
        result = self.cur.fetchall()
        return result
        
    def deletedata(self,empid):
        self.cur.execute(f"delete from main_info where id = '{empid}';")
        self.cur.execute(f"delete from finance_info where id = '{empid}';")
        self.cur.execute(f"delete from demographic_info where id = '{empid}';")
        self.db.commit()
    
    def addemployee(self,main,finance,other):
        ID = main["Employee ID"]

        d1 = {"Employee ID":"id","Name":"name","Join Date":"joined","Division":"dvn","Position":"pos"}
        col1 = "" 
        val1 = ""
        for c,v in main.items():
            if v:
                col1 += f"{d1[c]},"
                val1 += f"'{v}',"
        cmd1 = "insert into main_info ("+col1[:-1]+") values ("+val1[:-1]+");"

        d2 = {"Pay*":"pay","last Pay":"last","Bonus":"bonus"}
        col2 = "id," 
        val2 = f"'{ID}',"
        for c,v in finance.items():
            if v:
                col2 += f"{d2[c]},"
                val2 += f"'{v}',"
        cmd2 = "insert into finance_info ("+col2[:-1]+") values ("+val2[:-1]+");"

        d3 = {"Date of Birth*":"dob","Father's Name":"father","Mother's Name":"mother","Mobile Number*":"mobile","Address*":"address","Pincode*":"pin","Country":"country"}
        col3 = "id," 
        val3 = f"'{ID}',"
        for c,v in other.items():
            if v:
                col3 += f"{d3[c]},"
                val3 += f"'{v}',"
        cmd3 = "insert into demographic_info ("+col3[:-1]+") values ("+val3[:-1]+");"


        self.cur.execute(cmd1)
        self.cur.execute(cmd2)
        self.cur.execute(cmd3)
        self.db.commit()

# A = empdbms()
# print(A.viewtable(""))
# print(A.viewalltables())
# Header = ["Employee ID","Name","Join Date","Division","Position","Pay","Last Paid","Bonus","Date of Birth","Father's Name","Mother's Name","Mobile No","Address","Pincode","Country"]