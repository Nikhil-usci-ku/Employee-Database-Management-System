from os import system
from tables import alll
from time import sleep
from tabulate import tabulate



system("cls")
print("*** Welcome to Employee Database Management System ***\n")

def csp(sec:float = 0):
    sleep(sec)
    system("cls")

def main_options():
    while True:
        print("What would you like to do?\n1 --> View Employee Data\n2 --> Add Employee Data\n3 --> Edit Data\nq --> Quit")
        I = input("-->> ")
        try:
            I = int(I)
        except:
            if I.lower() == "q":
                print("Quitted")
                exit()
            print("Wrong Input")
            csp(3)
            continue

        if I == 1:
            viewmain()

        elif I == 2:
            addmain()

        elif I == 3:
            updatemain()

        else:
            print("Wrong Input")
            csp(3)
        csp()

#########################################################################################################

def viewmain():
    Header1 = ["Employee ID","Name","Join Date","Division","Position","Pay","Last Paid","Bonus"]
    Header2 = ["Employee ID","Date of Birth","Father's Name","Mother's Name","Mobile No","Address","Pincode","Country"]
    
    def customview():
        csp()
        Query = input("Enter ID/Name to Search : ")
        Ins = alll.empdbms()
        Dataraw = Ins.viewtable(Query)
        print(f"\n{len(Dataraw)} entry(s) found.")
        if Dataraw == []:
            input("Press any key to return...")
            return
        
        Data1 = []
        Data2 = []
        for singledata in Dataraw:
            Tdata = list(singledata)
            Tdata.pop(5)
            Tdata.pop(8)
            Tdata[2] = Tdata[2].strftime("%Y-%m-%d")
            Tdata[8] = Tdata[8].strftime("%Y-%m-%d")
            try:Tdata[6] = Tdata[6].strftime("%Y-%m-%d")
            except: pass
            Data1.append(Tdata[:8])
            Data2.append([Tdata[0]]+Tdata[8:])

        print("-->> Company Info")
        print(tabulate(Data1,Header1,tablefmt='psql'))
        print()

        print("-->> Personal Info")
        print(tabulate(Data2,Header2,tablefmt='psql'))
        input()

    def allview():
        Ins = alll.empdbms()
        Dataraw = Ins.viewalltables()
        csp()
        Data1 = []
        Data2 = []
        for singledata in Dataraw:
            Tdata = list(singledata)
            Tdata.pop(5)
            Tdata.pop(8)
            Tdata[2] = Tdata[2].strftime("%Y-%m-%d")
            Tdata[8] = Tdata[8].strftime("%Y-%m-%d")
            try:Tdata[6] = Tdata[6].strftime("%Y-%m-%d")
            except: pass
            Data1.append(Tdata[:8])
            Data2.append([Tdata[0]]+Tdata[8:])

        print("-->> Company Info")
        print(tabulate(Data1,Header1,tablefmt='psql'))
        print()

        print("-->> Personal Info")
        print(tabulate(Data2,Header2,tablefmt='psql'))
        input()
    
    while True:
        csp()
        print("How would you like to view Info?\n1 --> By Name/id\n2 --> All Data\n3 --> Back to Main Menu\nq --> Quit ")
        I = input("-->> ")
        try:
            I = int(I)
        except:
            if I.lower() == "q":
                print("Quitted")
                exit()
            print("Wrong Input")
            csp(3)
            continue
        
        if I == 1:
            customview()

        elif I == 2:
            allview()

        elif I == 3:
            return

        else:
            print("Wrong Input")
            csp(3)

#########################################################################################################

def addmain():
    def adddata():
        csp()
        maindatadict = {"Employee ID":None,"Name":None,"Join Date":None,"Division":None,"Position":None}
        financedatadict = {"Pay*":None,"last Pay":None,"Bonus":None}
        otherdatadict = {"Date of Birth*":None,"Father's Name":None,"Mother's Name":None,"Mobile Number*":None,"Address*":None,"Pincode*":None,"Country":None}
        print("Enter Information to Add (QtQt to quit in between)--> ")
        for i in maindatadict:
            MI = input(f"{i}* : ")
            if MI == "QtQt":return 
            maindatadict[i] = MI if MI != "" else None
        for i in financedatadict:
            FI = input(f"{i} : ")
            if FI == "QtQt":return 
            financedatadict[i] = FI if FI != "" else None
        for i in otherdatadict:
            OI = input(f"{i} : ")
            if OI == "QtQt":return 
            otherdatadict[i] = OI if OI != "" else None
        print("All Input Taken")
        csp(3)

        print("You Entered The Following Details -->")

        for d,v in maindatadict.items():
            print(f"{d} : {v}")
        for d,v in financedatadict.items():
            print(f"{d} : {v}")
        for d,v in otherdatadict.items():
            print(f"{d} : {v}")

        print("Press 'C' to add All Info   or 'E' to Return")
        while True:
            I = input("-->")
            if 'e' in I.lower():
                return
            if I.lower() =='c':
                break
        csp(0.3)
        print("\nAdding Information in Database")
        Ins = alll.empdbms()
        Ins.addemployee(maindatadict,financedatadict,otherdatadict)
        print("Information added Successfully")
        input()

    while True:
        csp()
        print("Choose Operation?\n1 --> Add Employee Info\n2 --> Back to Main Menu\nq --> Quit ")
        I = input("-->> ")
        try:
            I = int(I)
        except:
            if I.lower() == "q":
                print("Quitted")
                exit()
            print("Wrong Input")
            csp(3)
            continue
        
        if I == 1:
            adddata()

        elif I == 2:
            return
        
        else:
            print("Wrong Input")
            csp(3)

#########################################################################################################

def updatemain():
    def deletedata():
        Header1 = ["Employee ID","Name","Join Date","Division","Position","Pay","Last Paid","Bonus"]
        Header2 = ["Employee ID","Date of Birth","Father's Name","Mother's Name","Mobile No","Address","Pincode","Country"]
        csp()
        Query = input("Enter ID to Delete : ")
        Ins = alll.empdbms()
        Dataraw = Ins.viewtable(Query)
        if Dataraw:
            Dataraw = [Dataraw[0]]
        if Dataraw == []:
            print(f"\n{len(Dataraw)} entry(s) found.")
            input("Press any key to return...")
            return
        
        Data1 = []
        Data2 = []
        for singledata in Dataraw:
            Tdata = list(singledata)
            Tdata.pop(5)
            Tdata.pop(8)
            Tdata[2] = Tdata[2].strftime("%Y-%m-%d")
            Tdata[8] = Tdata[8].strftime("%Y-%m-%d")
            try:Tdata[6] = Tdata[6].strftime("%Y-%m-%d")
            except: pass
            Data1.append(Tdata[:8])
            Data2.append([Tdata[0]]+Tdata[8:])

        print("-->> Company Info")
        print(tabulate(Data1,Header1,tablefmt='psql'))
        print()

        print("-->> Personal Info")
        print(tabulate(Data2,Header2,tablefmt='psql'))

        C = input("\nWould you like to delete the following data (Y/N) --> ")
        if C.lower() == "y":
            Ins.deletedata(Tdata[0])
            print("Employee Data deleted successfully.")
        else:
            print("Operation Aborted.")
        input("Press any key to return...")


    def updatedata():
        Header1 = ["Employee ID","Name","Join Date","Division","Position","Pay","Last Paid","Bonus"]
        Header2 = ["Employee ID","Date of Birth","Father's Name","Mother's Name","Mobile No","Address","Pincode","Country"]
        csp()
        Query = input("Enter ID to Search : ")
        Ins = alll.empdbms()
        Dataraw = Ins.viewtable(Query)
        if Dataraw:
            Dataraw = [Dataraw[0]]
        if Dataraw == []:
            print(f"\n{len(Dataraw)} entry(s) found.")
            input("Press any key to return...")
            return
        
        Data1 = []
        Data2 = []
        for singledata in Dataraw:
            Tdata = list(singledata)
            Tdata.pop(5)
            Tdata.pop(8)
            Tdata[2] = Tdata[2].strftime("%Y-%m-%d")
            Tdata[8] = Tdata[8].strftime("%Y-%m-%d")
            try:Tdata[6] = Tdata[6].strftime("%Y-%m-%d")
            except: pass
            Data1.append(Tdata[:8])
            Data2.append([Tdata[0]]+Tdata[8:])

        print("-->> Company Info")
        print(tabulate(Data1,Header1,tablefmt='psql'))
        print()

        print("-->> Personal Info")
        print(tabulate(Data2,Header2,tablefmt='psql'))

        C = input("\nWould you like to Edit the following data (Y/N) --> ")
        if C.lower() == "n":
            print("Operation Aborted.")
            input("Press any key to return...")
            return
       
        csp()
        maindatadict = {"Employee ID":Tdata[0],"Name":Tdata[1],"Join Date":Tdata[2],"Division":Tdata[3],"Position":Tdata[4]}
        financedatadict = {"Pay*":Tdata[5],"last Pay":Tdata[6],"Bonus":Tdata[7]}
        otherdatadict = {"Date of Birth*":Tdata[8],"Father's Name":Tdata[9],"Mother's Name":Tdata[10],"Mobile Number*":Tdata[11],
                         "Address*":Tdata[12],"Pincode*":Tdata[13],"Country":Tdata[14]}
        Edits = {}
        print("Enter Information to Edit or press Enter to Skip (QtQt to quit in between)--> ")

        for i in maindatadict:
            MI = input(f"{i}* ({maindatadict[i]}) : ")
            if MI == "QtQt":return 
            if MI != "":
                maindatadict[i] = MI
                Edits[i] = MI
        
        for i in financedatadict:
            FI = input(f"{i} ({financedatadict[i]}) : ")
            if FI == "QtQt":return 
            if FI != "":
                financedatadict[i] = FI
                Edits[i] = FI

        for i in otherdatadict:
            OI = input(f"{i} ({otherdatadict[i]}) : ")
            if OI == "QtQt":return
            if OI != "":
                otherdatadict[i] = OI
                Edits[i] = OI

        print("All Edits Recorded")
        csp(3)

        if Edits:
            print("You Edited The Following Parameters -->")
            for d,v in Edits.items():
                print(f"{d} : {v}")
        else:
            print("No Editing was performed")
            input("Press any key to return...")
            return
        
        print("Press 'C' to Confirm Edit  or 'E' to Return")
        while True:
            I = input("-->")
            if 'e' in I.lower():
                return
            if I.lower() =='c':
                break
        csp(0.3)
        print(f"Editing Information for {Tdata[0]}")
        Ins = alll.empdbms()
        Ins.deletedata(Tdata[0])
        Ins.addemployee(maindatadict,financedatadict,otherdatadict)
        print("Information Edited Successfully")
        input("Press any key to return...")

    while True:
        csp()
        print("What would you like to Update?\n1 --> Delete Data\n2 --> Update Data\n3 --> Back to Main Menu\nq --> Quit ")
        I = input("-->> ")
        try:
            I = int(I)
        except:
            if I.lower() == "q":
                print("Quitted")
                exit()
            print("Wrong Input")
            csp(3)
            continue
        
        if I == 1:
            deletedata()

        elif I == 2:
            updatedata()

        elif I == 3:
            return

        else:
            print("Wrong Input")
            csp(3)

main_options()