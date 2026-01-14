import mysql.connector
con=mysql.connector.connect(host='localhost', user='root', password='root@123')
mycursor=con.cursor()
#CREATING DATABASE
mycursor.execute('create database if not exists bakery')
mycursor.execute('use bakery')
mycursor.execute('create table if not exists cookie_corner(sno int, products VARCHAR(20))')
sql='select * from cookie_corner'
mycursor.execute(sql)
res=mycursor.fetchall()
if res==[]:
    mycursor.execute('insert into cookie_corner values(1, "cake")')
    mycursor.execute('insert into cookie_corner values (2, "pastry")')
    mycursor.execute('insert into cookie_corner values (3, "juice")')
    mycursor.execute('insert into cookie_corner values (4, "butter")')
    mycursor.execute('insert into cookie_corner values (5, "cheese")')
    con.commit()
mycursor.execute('create table if not exists flavour(sno int, varieties VARCHAR(20), cost INT)')
sql1='select * from flavour'
mycursor.execute(sql1)
res1=mycursor.fetchall()
if res1==[]:
    mycursor.execute('insert into flavour values(1, "Vanilla", 550)')
    mycursor.execute('insert into flavour values (2, "Chocolate",560)')
    mycursor.execute('insert into flavour values (3, "Strawberry",600)')
    mycursor.execute('insert into flavour values (4, "Butter_scotch",570)')
    mycursor.execute('insert into flavour values (5, "Jasmine",620)')
    con.commit()
mycursor.execute('create table if not exists pastry_flav(sno int, varieties VARCHAR(20), cost INT)')
sql2='select * from pastry_flav'
mycursor.execute(sql2)
res2=mycursor.fetchall()
if res2==[]:
    mycursor.execute('insert into pastry_flav values(1, "Vanilla", 80)')
    mycursor.execute('insert into pastry_flav values (2, "Chocolate",90)')
    mycursor.execute('insert into pastry_flav values (3, "Strawberry",100)')
    mycursor.execute('insert into pastry_flav values (4, "Butter_scotch",95)')
    mycursor.execute('insert into pastry_flav values (5, "Jasmine",110)')
    con.commit()
mycursor.execute('create table if not exists juices_var(sno int, varieties VARCHAR(20), cost INT)')
sql3='select * from juices_var'
mycursor.execute(sql3)
res3=mycursor.fetchall()
if res3==[]:
    mycursor.execute('insert into juices_var values(1, "Mango", 100)')
    mycursor.execute('insert into juices_var values (2, "Orange",100)')
    mycursor.execute('insert into juices_var values (3, "Lemon",80)')
    mycursor.execute('insert into juices_var values (4, "Strawberry_Milkshake",120)')
    mycursor.execute('insert into juices_var values (5, "Blueberry_Milkshake",140)')
    con.commit()
mycursor.execute('create table if not exists butter_var(sno int, varieties VARCHAR(20), cost INT)')
sql4='select * from butter_var'
mycursor.execute(sql4)
res4=mycursor.fetchall()
if res4==[]:
    mycursor.execute('insert into butter_var values(1, "Unsalted", 25)')
    mycursor.execute('insert into butter_var values (2, "Salted",30)')
    mycursor.execute('insert into butter_var values (3, "Garlic",40)')
    con.commit()
mycursor.execute('create table if not exists cheese_var(sno int, varieties VARCHAR(20), cost INT)')
sql5='select * from cheese_var'
mycursor.execute(sql5)
res5=mycursor.fetchall()
if res5==[]:
    mycursor.execute('insert into cheese_var values(1, "Cottage", 80)')
    mycursor.execute('insert into cheese_var values (2, "Cheddar",90)')
    mycursor.execute('insert into cheese_var values (3, "Mozzarella",110)')
    mycursor.execute('insert into cheese_var values (4, "Camembert",120)')
    con.commit()
    
#ITEMS IN SHOP
def items():
    print('Items in the shop:')
    comm='select * from cookie_corner'
    mycursor.execute(comm)
    res=mycursor.fetchall()
    for items in res:
        print('serial_no:\tproduct:')
        print(items[0],'\t',items[1],'\n')

#varieties OF CAKE
def item():
    print('varieties available for Cakes:')
    s='select * from flavour'
    mycursor.execute(s)
    rs=mycursor.fetchall()
    for i in rs:
        print('serial_no.\tvarieties\tcost')
        print(i[0],'\t',i[1],'\t',i[2],'\n')

#varieties OF PASTRY
def pastries():
    print('varieties available for pastry:')
    s='select * from pastry_flav'
    mycursor.execute(s)
    rs=mycursor.fetchall()
    for i in rs:
        print('serial_no.\tvarieties\tcost')
        print(i[0],'\t',i[1],'\t',i[2],'\n')

#varieties OF JUICES
def juices():
    print('varieties available for Juice:')
    s='select * from juices_var'
    mycursor.execute(s)
    rs=mycursor.fetchall()
    for i in rs:
        print('serial_no.\tvarieties\tcost')
        print(i[0],'\t',i[1],'\t',i[2],'\n')

#varieties OF BUTTER
def butters():
    print('varieties available for butter:')
    s='select * from butter_var'
    mycursor.execute(s)
    rs=mycursor.fetchall()
    for i in rs:
        print('serial_no.\tvarieties\tcost')
        print(i[0],'\t',i[1],'\t',i[2],'\n')

#varieties OF CHEESE
def cheeses():
    print('varieties available for Cheese:')
    s='select * from cheese_var'
    mycursor.execute(s)
    rs=mycursor.fetchall()
    for i in rs:
        print('serial_no.\tvarieties\tcost')
        print(i[0],'\t',i[1],'\t',i[2],'\n')

#USER INTERFACE 
def for_order():
    print ('what do you want to order?')
    items()
    d=int(input('Enter your serial No of the item to buy:'))
    if d==1:
        print('which cake do you want?')
        item()
        print('### NOTE: THE COST IS AS PER 500 GRAMS OF CAKE ###')
        print('Choose which cake do you want?')
        ck=int(input('Enter your Choice:'))
        if ck==1:
            print('How much Quantity of Vanilla cake do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from flavour where varieties='Vanilla'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Vanilla Cake:', qty)
            print('total amount',qty*c)
            print('\n')
            bill()
            print('\n')
        elif ck==2:
            print('How much Quantity of Chocolate cake do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from flavour where varieties='Chocolate'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Chocolate Cake:', qty)
            print('Total amount', qty*c)
            print('\n')
            bill()
            print('\n')
        elif ck==3:
            print('How much Quantity of strawberry cake do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from flavour where varieties='Strawberry'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Strawberry Cake:',qty)
            print('total amount', qty*c)
            print('\n')
            bill()
            print('\n')
        elif ck==4:
            print('How much Quantity of Butter_scotch cake do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from flavour where varieties='Butter_scotch'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Butter_scotch Cake:', qty)
            print('total amount', qty*c)
            print('\n')
            bill()
            print('\n')
        elif ck==5:
            print('How much Quantity of jasmin cake do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from flavour where varieties='Jasmine'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Jasmin Cake:', qty) 
            print('total amount', qty*c)
            print('\n')
            bill()
            print('\n')
        else:
            print('Enter Valid choice')
    elif d==2:
        print('which pastry do you want?')
        pastries()
        print('### NOTE: THE COST IS AS PER 100 GRAMS OF PASTRY ###')
        print('Choose which pastry do you want?')
        pt=int(input('Enter your Choice:'))
        if pt==1:
            print('How much Quantity of Vanilla pastry do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from pastry_flav where varieties='Vanilla'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Vanilla Pastry:', qty)
            print('total amount',qty*c)
            print('\n')
            bill()
            print('\n')
        elif pt==2:
            print('How much Quantity of Chocolate pastry do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from pastry_flav where varieties='Chocolate'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Chocolate Pastry:', qty)
            print('Total amount', qty*c)
            print('\n')
            bill()
            print('\n')
        elif pt==3:
            print('How much Quantity of strawberry pastry do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from pastry_flav where varieties='Strawberry'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Strawberry Pastry:',qty)
            print('total amount', qty*c)
            print('\n')
            bill()
            print('\n')
        elif pt==4:
            print('How much Quantity of Butter_scotch pastry do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from pastry_flav where varieties='Butter_scotch'")
            d=mycursor.fetchall()
            c=int(d[0][0])
        else:
            print('Enter Valid choice')
    elif d==3:
        print('which juice do you want?')
        juices()
        print('### NOTE: THE COST IS AS PER 250 ML OF JUICE ###')
        print('Choose which juice do you want?')
        jc=int(input('Enter your Choice:'))
        if jc==1:
            print('How much Quantity of Mango juice do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from juices_var where varieties='Mango'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Mango Juice:', qty)
            print('total amount',qty*c)
            print('\n')
            bill()
            print('\n')
        elif jc==2:
            print('How much Quantity of Orange juice do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from juices_var where varieties='Orange'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Orange Juice:', qty)
            print('Total amount', qty*c)
            print('\n')
            bill()
            print('\n')
        elif jc==3:
            print('How much Quantity of Lemon juice do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from juices_var where varieties='Lemon'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Lemon Juice:',qty)
            print('total amount', qty*c)
            print('\n')
            bill()
            print('\n')
        elif jc==4:
            print('How much Quantity of Strawberry Milkshake do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from juices_var where varieties='Strawberry_Milkshake'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Strawberry Milkshake:', qty)
            print('total amount', qty*c)
            print('\n')
            bill()
            print('\n')
        else:
            print('Enter Valid choice')
    elif d==4:
        print('which butter do you want?')
        butters()
        print('### NOTE: THE COST IS AS PER 100 GRAMS OF BUTTER ###')
        print('Choose which butter do you want?')
        bc=int(input('Enter your Choice:'))
        if bc==1:
            print('How much Quantity of Unsalted butter do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from butter_var where varieties='Unsalted'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Unsalted Butter:', qty)
            print('total amount',qty*c)
            print('\n')
            bill()
            print('\n')
        elif bc==2:
            print('How much Quantity of Salted butter do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from butter_var where varieties='Salted'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Salted Butter:', qty)
            print('Total amount', qty*c)
            print('\n')
            bill()
            print('\n')
        elif bc==3:
            print('How much Quantity of Garlic butter do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from butter_var where varieties='Garlic'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Garlic Butter:',qty)
            print('total amount', qty*c)
            print('\n')
            bill()
            print('\n')
        else:
            print('Enter Valid choice')
    elif d==5:
        print('which cheese do you want?')
        cheeses()
        print('### NOTE: THE COST IS AS PER 100 GRAMS OF CHEESE ###')
        print('Choose which cheese do you want?')
        cc=int(input('Enter your Choice:'))
        if cc==1:
            print('How much Quantity of Cottage cheese do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from cheese_var where varieties='Cottage'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Cottage Cheese:', qty)
            print('total amount',qty*c)
            print('\n')
            bill()
            print('\n')
        elif cc==2:
            print('How much Quantity of Cheddar cheese do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from cheese_var where varieties='Cheddar'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Cheddar Cheese:', qty)
            print('Total amount', qty*c)
            print('\n')
            bill()
            print('\n')
        elif cc==3:
            print('How much Quantity of Mozzarella cheese do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from cheese_var where varieties='Mozzarella'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Mozzarella Cheese:',qty)
            print('total amount', qty*c)
            print('\n')
            bill()
            print('\n')
        elif cc==4:
            print('How much Quantity of Camembert cheese do you want?')
            qty=int(input('Enter Qty:'))
            print('You have sucessfully ordered your item!!!:')
            print('\n')
            Bill(name, phone)
            mycursor.execute("Select cost from cheese_var where varieties='Camembert'")
            d=mycursor.fetchall()
            c=int(d[0][0])
            print('Total Quantity of Camembert Cheese:', qty)
            print('total amount', qty*c)
            print('\n')
            bill()
            print('\n')
        else:
            print('Enter Valid choice')
    else:
        print('Enter valid serial number')

#ADMIN INTERFACE

def admin():
    print('Welcome  ADMIN')
    print('WHAT IS YOUR GOAL TODAY?')
    print('Choose 1 for DISPLAYING ITEMS')
    print('Choose 2 for UPDATING PRICES')
    print('Choose 3 for EXIT')
    ch=int(input('Enter your choice:'))
    if ch==1:
        items()
        print('Choose an Item')
        it=int(input('Enter the serial number:'))
        if it==1:
            item()
        elif it==2:
            pastries()
        elif it==3:
            juices()
        elif it==4:
            butters()
        elif it==5:
            cheeses()
        else:
            print('Enter valid serial number')
        admin()
    elif ch==2:
        print('What would you like to update?')
        print('1. To update cake')
        print('2. To update pastries')
        print('3. To update juices')
        print('4. To update butter')
        print('5. To update cheese')
        upd=int(input('Enter your choice:'))
        if upd==1:
            print('choose flavour')
            item()
            flav=int(input('Enter serial number:'))
            if flav==1:
                ucost=int(input('Enter the updated cost:'))
                mycursor.execute('update flavour set Cost=%s where varieties="Vanilla"',(ucost,))
            elif flav==2:
                ucost=int(input('Enter the updated cost:'))
                mycursor.execute('update flavour set Cost=%s where varieties="Chocolate"',(ucost,))
            elif flav==3:
                ucost=int(input('Enter the updated cost:'))
                mycursor.execute('update flavour set Cost=%s where varieties="Strawberry"',(ucost,))
            elif flav==4:
                ucost=int(input('Enter the updated cost:'))
                mycursor.execute('update flavour set Cost=%s where varieties="Butter_scotch"',(ucost,))
            elif flav==5:
                ucost=int(input('Enter the updated cost:'))
                mycursor.execute('update flavour set Cost=%s where varieties="Jasmine"',(ucost,))
            else:
                print('Enter valid serial number')
        elif upd==2:
            print('choose flavour')
            pastries()
            flav1=int(input('Enter serial number:'))
            if flav1==1:
                pcost=int(input('Enter the updated cost:'))
                mycursor.execute('update pastry_flav set Cost=%s where varieties="Vanilla"',(pcost,))
            elif flav1==2:
                pcost=int(input('Enter the updated cost:'))
                mycursor.execute('update pastry_flav set Cost=%s where varieties="Chocolate"',(pcost,))
            elif flav1==3:
                pcost=int(input('Enter the updated cost:'))
                mycursor.execute('update pastry_flav set Cost=%s where varieties="Strawberry"',(pcost,))
            elif flav1==4:
                pcost=int(input('Enter the updated cost:'))
                mycursor.execute('update pastry_flav set Cost=%s where varieties="Butter_scotch"',(pcost,))
            elif flav1==5:
                pcost=int(input('Enter the updates cost:'))
                mycursor.execute('update pastry_flav set Cost=%s where varieties="Jasmine"',(pcost,))
            else:
                print('Enter valid serial number')
        elif upd==3:
            print('choose flavour')
            juices()
            flav2=int(input('Enter serial number:'))
            if flav2==1:
                jcost=int(input('Enter the updated cost:'))
                mycursor.execute('update juices_var set Cost=%s where varieties="Mango"',(jcost,))
            elif flav2==2:
                jcost=int(input('Enter the updated cost:'))
                mycursor.execute('update juices_var set Cost=%s where varieties="Orange"',(jcost,))
            elif flav2==3:
                jcost=int(input('Enter the updated cost:'))
                mycursor.execute('update juices_var set Cost=%s where varieties="Lemon"',(jcost,))
            elif flav2==4:
                jcost=int(input('Enter the updated cost:'))
                mycursor.execute('update juices_var set Cost=%s where varieties="Strawberry_Milkshake"',(jcost,))
            elif flav2==5:
                jcost=int(input('Enter the updates cost:'))
                mycursor.execute('update juices_var set Cost=%s where varieties="Blueberry_Milkshake"',(jcost,))
            else:
                print('Enter valid serial number')
        elif upd==4:
            print('choose variety')
            butters()
            flav3=int(input('Enter serial number:'))
            if flav3==1:
                bcost=int(input('Enter the updated cost:'))
                mycursor.execute('update butter_var set Cost=%s where varieties="Unsalted"',(bcost,))
            elif flav3==2:
                bcost=int(input('Enter the updated cost:'))
                mycursor.execute('update butter_var set Cost=%s where varieties="Salted"',(bcost,))
            elif flav3==3:
                bcost=int(input('Enter the updated cost:'))
                mycursor.execute('update butter_var set Cost=%s where varieties="Garlic"',(bcost,))
            else:
                print('Enter valid serial number')
        elif upd==5:
            print('choose flavour')
            pastries()
            flav4=int(input('Enter serial number:'))
            if flav4==1:
                ccost=int(input('Enter the updated cost:'))
                mycursor.execute('update cheese_var set Cost=%s where varieties="Cottage"',(ccost,))
            elif flav4==2:
                ccost=int(input('Enter the updated cost:'))
                mycursor.execute('update cheese_var set Cost=%s where varieties="Cheddar"',(ccost,))
            elif flav4==3:
                ccost=int(input('Enter the updated cost:'))
                mycursor.execute('update cheese_var set Cost=%s where varieties="Mozzarella"',(ccost,))
            elif flav4==4:
                ccost=int(input('Enter the updated cost:'))
                mycursor.execute('update cheese_var set Cost=%s where varieties="Camembert"',(ccost,))
            else:
                print('Enter valid serial number')
    elif ch==3:
        Main()
    else:
        print('Enter Valid choice')

#FOR BILLING 

def Bill(name, phone):
    print('...............................................................................................................................................')
    print('YOUR BILL')
    print('...............................................................................................................................................')
    print('Customer name:',name)
    print('Contact :', phone)
def bill():
    print('@@@@@@@@@@@@@@@@@@@@ THANK YOU@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@ VISIT US AGAIN@@@@@@@@@@@@@@@@')

#ENTRANCE CODE

print('______________________________Welcome to Cookie Corner___________________________________')
print('_____________________________The Sweetest spot in Town____________________________________')
print('_________________________________Indulge in the Corner______________________________________')
name=input("Please Enter your name:")
phone=input("Please Enter your contact:")
ph=str(phone)
    
#MAIN CODE
def Main():
    ch='Y'
    while ch=='Y':
        print("PLEASE CHOOSE 1 FOR CUSTOMER")
        print("PLEASE CHOOSE 2 FOR ADMIN")
        print("PLEASE CHOOSE 3 FOR EXIT")
        choice=int(input("Enter your choice:"))
        if choice==3:
            ch='N'
        elif choice==2:
            passwrd=input("Enter the Password:")
            if passwrd=='root@123':
                admin()
            else:
                print('you have entered the wrong password')
                print('Please try again later')
                Main()
        elif choice==1:
            print('press 1 to see the MENU', sep='.......')
            print('press 2 to order any item')
            print('press 3 to EXIT')
            e=int(input('Enter your choice:'))
            if e==3:
                ch='N'
            elif e==1:
                print("Items in the shop:")
                items()
                Main()
            elif e==2:
                for_order()
            else:
                print("Wrong Input")
                Main()
Main()
