import mysql.connector as con
import prettytable
import random
import datetime
mycon=con.connect(host="localhost",username="root",password="root")
cur=mycon.cursor()
cur.execute("create database if not exists Shop")
cur.execute("use Shop")
cur.execute("create table if not exists Product_Data(Product_ID integer primary key not null, Product varchar(30) not null, Company varchar(30), Product_Type varchar(30), Product_Colour char(15), 5_Star_Ratings integer, Price integer not null,Quantity integer)")
cur.execute("create table if not exists Cust_Data(Cust_ID integer primary key not null,Customer_Name varchar(15) not null,Contact_No bigint not null, Address varchar(40))")
mycon.commit()
def dispA():           #displays product table
    print("Table : Product_Data")
    tab=prettytable.PrettyTable()
    cur.execute("select * from {}".format('Product_Data'))
    dat=cur.fetchall()
    tab=prettytable.PrettyTable()
    for i in dat:
        tab.field_names=['ProductID','ProductName','Company','ProductType','Colour','Rating','Price','Quantity']
        tab.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
    print(tab)
def dispB():           #displays customer table
    print("Table : Cust_Data")
    cur.execute("select * from {}".format('Cust_Data'))
    dat=cur.fetchall()
    tab=prettytable.PrettyTable()
    for i in dat:
        tab.field_names=["CustomerID","Name","Contact Number","Address"]
        tab.add_row([i[0],i[1],i[2],i[3]])
    print(tab)
while True:
    print("""
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|                                                                                                                                                                     |
|               = = = = = =  = = = = =        = = = = =  = = = =   =       =  = = = =      = = = =   = = = = =  = = = =  = = = =  = = = = =                           |
|                 =       =  =                    =      =     =   = =     =  =            =             =      =     =  =     =  =                                   |
|                 =       =  =                    =      =     =   =  =    =  =            =             =      =     =  =     =  =                                   |
|                 =       =  =                    =      =     =   =   =   =  =            =             =      =     =  = = = =  =                                   |
|                 =       =  = = = =              =      =     =   =    =  =  =  =  =      = = = =       =      =     =  =  =     = = = =                             |
|                 =       =  =                    =      =     =   =     = =  =     =            =       =      =     =  =   =    =                                   |
|                 =       =  =                    =      =     =   =      ==  =     =            =       =      =     =  =    =   =                                   |
|               = = = = = =  = = = = =        = = =      = = = =   =       =  = = = =      = = = =       =      = = = =  =     =  = = = = =                           |
|                                                                                                                                                                     |
|                                                                                                                                                                     |
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        



            
        Identity Required for Access. Please Choose from below:
        
        1. Admin
        2. Customer
        3. Exit
        """)
    ans=input("Enter your choice: ")
    if ans=='1':
        print("""Entered as Admin. You have access to data. Please Choose :
                    A. Modify Product Details
                    B. Modify Customer Details
                """)
        ans11=input("Enter your choice: ")
        if ans11=='A':
            ansa='y'
            while ansa=='y':
                print("""

                Choose from below:
                1. Display All Products
                2. Add A New Product
                3. Update An Existing Product
                4. Remove A Product
                5. Search A Particular Product
                6. Exit
                """)
                try:
                    ans12=input("Enter your choice:")
                except:
                    print("Invalid")
                    continue
                if ans12=='1':
                    dispA()               
                elif ans12=='2':
                    def addva1():
                        while True:
                            try:                                
                                ID=int(input("Enter ProductID:"))
                                Name=input("Enter Product Name:")
                                Company=input("Enter Company Name:")
                                Type=input("Enter Type of Product:")
                                Colour=input("Enter Colour of the Product:")
                                Rating=int(input("Enter Amount of 5 Star Ratings:"))
                                Price=int(input("Enter Product Price:"))
                                Qty=int(input("Enter Quantity:"))
                            except:
                                print("Error. Please enter valid values.")
                                continue
                            b="insert into {} values({},'{}','{}','{}','{}',{},{},{})".format('Product_Data',ID,Name,Company,Type,Colour,Rating,Price,Qty)
                            cur.execute(b)
                            mycon.commit()
                            print("Updated table Product_Data:")
                            dispA()
                            ans4=input("If you wish to add another product ,press 'y' for yes and 'n' for no: ")
                            if ans4=="y":
                                continue
                            else:
                                return               

                    addva1()
                elif ans12=='3':
                    dispA()
                    ans='yes'
                    while True:
                        try:
                            a=int(input("Enter ID of product you wish to update:"))
                            cur.execute("select * from Product_Data where Product_ID={}".format(a))
                            dat=cur.fetchall()
                            c=cur.rowcount
                            if c>0:
                                break
                        
                            elif c==0:
                                print("ID doesnt exist")
                        except:
                            print("Invalid ID type")
                    
                    
                    print("""Choose which value you want to update:
                                        a. Product Name
                                        b. Product Company
                                        c. Type
                                        d. Colour
                                        e. Rating
                                        f. Price
                                        g. Quantity
                                        """)
                    
                    while ans=='yes':
                        x='y'
                        while x=='y':
                            ansx=input("Enter your choice(a,b,c,d,e,f,g): ")
                            if ansx=='a':
                                try:
                                    Name=input("Enter new name:")
                                    h="update Product_Data set Product='{}' where Product_ID={}".format(Name,a)
                                    cur.execute(h)
                                    mycon.commit()
                                    print("Updated")
                                except:
                                    print("Error")
                            elif ansx=='b':
                                try:
                                    Company=input("Enter new name of company:")
                                    h="update Product_Data set Company='{}' where Product_ID={}".format(Company,a)
                                    cur.execute(h)
                                    mycon.commit()
                                    print("Updated")
                                except:
                                    print("Error")
                                
                            elif ansx=='c':
                                try:
                                    Type=input("Enter new type:")
                                    h="update Product_Data set Product_Type='{}' where Product_ID={}".format(Type,a)
                                    cur.execute(h)
                                    mycon.commit()
                                    print("Updated")
                                except:
                                    print("Error")
                            elif ansx=='d':
                                try:
                                    Colour=input("Enter new colour:")
                                    h="update Product_Data set Product_Colour='{}' where Product_ID={}".format(Colour,a)
                                    cur.execute(h)
                                    mycon.commit()
                                    print("Updated")
                                except:
                                    print("Error")
                            elif ansx=='e':
                                try:
                                    Rating=int(input("Enter new rating:"))
                                    h="update Product_Data set 5_Star_Ratings='{}' where Product_ID={}".format(Rating,a)
                                    cur.execute(h)
                                    mycon.commit()
                                    print("Updated")
                                except:
                                    print("Error")
                            elif ansx=='f':
                                try:
                                    Price=int(input("Enter new price:"))
                                    h="update Product_Data set Price='{}' where Product_ID={}".format(Price,a)
                                    cur.execute(h)
                                    mycon.commit()
                                    print("Updated")
                                except:
                                    print("Error")
                            elif ansx=='g':
                                try:
                                    Qty=int(input("Enter new quantity:"))
                                    h="update Product_Data set Quantity='{}' where Product_ID={}".format(Qty,a)
                                    cur.execute(h)
                                    mycon.commit()
                                    print("Updated")
                                except:
                                    print("Error")
                            else:
                                print("Retry")

                            x=input("Press 'y' if you wish to update a different field or press 'n' to skip: ")
                        else:
                            dispA()
                            x=''
                            ans=''
                    
                    
                elif ans12=='4': #to delete product record
                    ans='y'
                    while ans=='y':
                        try:
                            a=int(input("Enter ID of product you wish to remove: "))
                            cur.execute("delete from Product_Data where Product_ID={}".format(a))
                            mycon.commit()
                            c=cur.rowcount
                            if c>0:
                                print("Record Deleted.")
                            else:
                                print("ID doesnt exist")
                        except:
                            print("Invalid ID type")
                        ans=input("If you wish to delete another product press 'y' or press 'n' to skip: ")
                elif ans12=='5': #to search for a record
                    ans='y'
                    while ans=='y':
                        try:
                            a=int(input("Enter ID of product you wish to search:"))
                            cur.execute("select * from Product_Data where Product_ID={}".format(a))
                            dat=cur.fetchall()
                            c=cur.rowcount
                            if c>0:
                                tab=prettytable.PrettyTable()
                                for i in dat:
                                    tab.field_names=['ProductID','ProductName','Company','ProductType','Colour','Rating','Price','Quantity']
                                    tab.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
                                print(tab)
                            else:
                                print("ID doesnt exist")
                        except:
                            print("Invalid ID type")
                        ans=input("If you wish to search another product press 'y' or press 'n' to skip: ")                    
                else:
                    ansa='n'
                    break
        if ans11=='B':
            ansa='y'
            while ansa=='y':
                print("""

                Choose from below:
                1. Display All Customers
                2. Update An Existing Customer
                3. Remove A Customer
                4. Search A Particular Customer
                5. Exit
                """)
                ans12=input("Enter your choice(1,2,3,4,5):")
                if ans12=='1':
                    dispB()
                elif ans12=='2':
                    ans='yes'
                    while True:
                        try:
                            a=int(input("Enter ID of customer you wish to update:"))
                            cur.execute("select * from Cust_Data where Cust_ID={}".format(a))
                            dat=cur.fetchall()
                            c=cur.rowcount
                            if c>0:
                                break
                        
                            elif c==0:
                                print("ID doesnt exist")
                        except:
                            print("Invalid ID type")
                    
                    
                    print("""Choose which value you want to update:
                                        a. Name
                                        b. Contact Number
                                        c. Address
                                        """)
                    
                    while ans=='yes':
                        x='y'
                        while x=='y':
                            ansx=input("Enter your choice(a,b,c): ")
                            if ansx=='a':
                            
                                try:
                                    Name=input("Enter new name:")
                                    h="update Cust_Data set Customer_Name='{}' where Cust_ID={}".format(Name,a)
                                    cur.execute(h)
                                    mycon.commit()
                                    print("Updated")
                                except:
                                    print("Error")
                            elif ansx=='b':
                                try:
                                    Cont=input("Enter new number:")
                                    h="update Cust_Data set Contact_No='{}' where Cust_ID={}".format(Cont,a)
                                    cur.execute(h)
                                    mycon.commit()
                                    print("Updated")
                                except:
                                    print("Error")
                                
                            elif ansx=='c':
                                try:
                                    Addr=input("Enter new address:")
                                    h="update Cust_Data set Address='{}' where Cust_ID={}".format(Addr,a)
                                    cur.execute(h)
                                    mycon.commit()
                                    print("Updated")
                                except:
                                    print("Error")
                            x=input("Press 'y' if you wish to update a different field: ")
                        else:
                            dispB()
                            x=''
                            ans=''
                elif ans12=='3':
                    ans='y'
                    while ans=='y':
                        try:
                            a=int(input("Enter ID of customer you wish to remove: "))
                            cur.execute("delete from Cust_Data where Cust_ID={}".format(a))
                            mycon.commit()
                            c=cur.rowcount
                            if c>0:
                                print("Record Deleted")
                            else:
                                print("ID doesnt exist")
                        except:
                            print("Invalid ID type")
                        ans=input("If you wish to delete record of another customer press 'y'  or press 'n' to skip: ")
                elif ans12=='4':
                    ans='y'
                    while ans=='y':
                        try:
                            a=int(input("Enter ID of customer you wish to search:"))
                            cur.execute("select * from Cust_Data where Cust_ID={}".format(a))
                            dat=cur.fetchall()
                            c=cur.rowcount
                            if c>0:
                                tab=prettytable.PrettyTable()
                                for i in dat:
                                    tab.field_names=["CustomerID","Name","Contact Number","Address"]
                                    tab.add_row([i[0],i[1],i[2],i[3]])
                                print(tab)
                            else:
                                print("ID doesnt exist")
                        except:
                            print("Invalid ID type")
                        ans=input("If you wish to search details of another customer press 'y' or press 'n' to skip: ")
                else:
                    break
    elif ans=='2':
        anse='y'
        while anse=='y':
            print(""" Welcome. Please choose:
                        A. Show Products
                        B. Add Products To Cart And Proceed To Buy
                        C. Exit""")
            ans=input("Enter your choice(A/B/C):")
            if ans=='A':
                print(""" Please Choose:
                    1. Show ALL PRODUCTS
                    2. Show FILTERED PRODUCTS
                    3. Exit""")
                ans1=input("Enter your choice(1/2/3):")
                if ans1=='1':
                    dispA()
                elif ans1=='2':
                    cont='yes'
                    while cont=='yes':
    
                        print(""" Choose which FILTER you wish to APPLY:
                        a. Type
                        b. Company
                        c. Price Range
                        d. Return""")
                        ans2=input("Enter your choice(a/b/c):")
                        if ans2=='a':
                            ansx='y'
                            while ansx=='y':
                                try:
                                    a=input("Enter TYPE of the products you wish to search:")
                                    cur.execute("select * from Product_Data where Product_Type='{}'".format(a))
                                    dat=cur.fetchall()
                                    c=cur.rowcount
                                    if c>0:
                                        tab=prettytable.PrettyTable()
                                        for i in dat:
                                            tab.field_names=['ProductID','ProductName','Company','ProductType','Colour','Rating','Price','Quantity']
                                            tab.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
                                        print(tab)
                                    else:
                                        print("No products availabe of TYPE",a)
                                except:
                                    print("Error")
                                ansx=input("Enter 'y' if you want to APPLY SAME FILTER or press 'n' to CHANGE:")
                        elif ans2=='b':
                            ansx='y'
                            while ansx=='y':
                                try:
                                    a=input("Enter NAME of the COMPANY of the products you wish to search:")
                                    cur.execute("select * from Product_Data where Company='{}'".format(a))
                                    dat=cur.fetchall()
                                    c=cur.rowcount
                                    if c>0:
                                        tab=prettytable.PrettyTable()
                                        for i in dat:
                                            tab.field_names=['ProductID','ProductName','Company','ProductType','Colour','Rating','Price','Quantity']
                                            tab.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
                                        print(tab)
                                    else:
                                        print("No products available of the Company",a)
                                        
                                except:
                                    print("Error")
                                ansx=input("Enter 'y' if you want to APPLY SAME FILTER or press 'n' to CHANGE:")
                        elif ans2=='c':
                            ansx='y'
                            while ansx=='y':
                                try:
                                    print("Enter PRICE RANGE of the products you wish to search:")
                                    a1=int(input("Enter minimum limit:"))
                                    a2=int(input("Enter maximum limit:"))
                                    if a1>a2:
                                        a1,a2=a2,a1                        
                                    cur.execute("select * from Product_Data where Price between {} and {}".format(a1,a2))
                                    dat=cur.fetchall()
                                    c=cur.rowcount
                                    if c>0:
                                        tab=prettytable.PrettyTable()
                                        for i in dat:
                                            tab.field_names=['ProductID','ProductName','Company','ProductType','Colour','Rating','Price','Quantity']
                                            tab.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
                                        print(tab)
                                    else:
                                        print("No products available in the provided range",a1,"to",a2)
                                        
                                except:
                                    print("Error")
                                ansx=input("Enter 'y' if you want to APPLY SAME FILTER or press 'n' to CHANGE:")
                        else:
                            break
                        cont=input("Enter 'yes' if you want to CHANGE FILTER or press 'n' to exit:")
                else:
                    break
            elif ans=='B':
                dispA()
                ans13='y'
                ans14='y'
                L=[] #creating a list to add records
                while ans13=='y':
                    while ans14=='y':
                        try:
                            pname=input("Enter name of the product:")
                            pqty=int(input("Enter the quantity of above product you wish to buy:"))
                            cur.execute("select * from product_data where Product='{}'".format(pname))
                            dat=cur.fetchall()
                            qty=dat[0][7]
                        except:
                            print("Invalid Values. Product DOES NOT EXIST or INVALID DATA TYPE")
                            continue
                        if pqty>qty:
                            print("Quantity exceeded. Available Quantity:",qty)
                        else:
                            qty=qty-pqty
                            h="update product_data set Quantity={} where Product='{}'".format(qty,pname)
                            cur.execute(h)
                            mycon.commit()
                            cur.execute("select * from product_data where Product='{}'".format(pname))
                            dat=cur.fetchall()
                            print("Added To Cart.")
                            for i in dat:
                                rec=[i[1],i[2],i[4],i[6],pqty*i[6],pqty]
                            L.append(rec)
                        ans14=input("Press 'y' if you wish to add another product to the cart or press 'n' to PROCEED TO PAYMENT:")
                    print()
                    print()
                    print()
                    print()
                    print()
                    print("YOUR CART:")
                    tab=prettytable.PrettyTable()
                    a=0
                    Tot=0 # Initiating total cost variable
                    while a<len(L):
                        tab.field_names=['Product','Company','Colour','Price','Quantity','Summed Price']
                        tab.add_row([L[a][0],L[a][1],L[a][2],L[a][3],L[a][5],L[a][4]])
                        Tot+=L[a][4]
                        a+=1
                    print(tab)
                    print("Total Cost: ₹ ",Tot)
                    print(''' PROCEED:
                                1. Buy Cart
                                2. Cancel Cart''')
                    ans15=input("Enter your choice:")
                    if ans15=='1':
                        print("Please fill-up The following Form:")
                        ansk='y'
                        while ansk=='y':
                            try:
                                ID=random.randint(100,10000)
                                time=datetime.datetime.now()
                                name=input("Enter your name:")
                                cont=int(input("Enter your contact number:"))
                                addr=input("Enter your address:")
                                print("Proceeding...")
                                ansk='n'
                            except:
                                print("Invalid values")
                                ansk='y'
                        print("Generating BILL>>>>>>>>")
                        print("Generated")
                        print()
                        print()
                        print('''      YOUR BILL:''')
                        tab=prettytable.PrettyTable()
                        print()
                        print()
                        print("TIME OF ORDER:",time)
                        a=0
                        while a<len(L):
                            tab.field_names=['Product','Company','Colour','Price','Quantity']
                            tab.add_row([L[a][0],L[a][1],L[a][2],L[a][3],L[a][5]])
                            a+=1
                        print(tab)
                        print()
                        print("Total Cost: ₹ ",Tot)
                        print(" ORDERED SUCCESSFULLY")
                        a="insert into cust_data values({},'{}',{},'{}')".format(ID,name,cont,addr)
                        cur.execute(a)
                        mycon.commit()
                        tab=prettytable.PrettyTable()
                        tab.field_names=['Product_ID','Customer Name','Contact Number','Address']
                        tab.add_row([ID,name,cont,addr])
                        print("Customer Details: ")
                        print(tab)
                        ans13='n'
                    else:
                        print("ORDER CANCELLED!")
                        break
            else:
                break
    else:
        print("EXITING WEBSITE...")
        print("EXITED")
        break
                        
        
                
                
                
                
        
              
