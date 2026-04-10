print('##########################################')
print("                                             '")
print('             \tGas agency\n')
print('########################################')
import mysql.connector
mydb=mysql.connector.connect(host='localhost',password='Abhi@@Kr7869',user='root')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists gas2")
mycursor.execute("use gas2")
mycursor.execute("create table if not exists complain(user_id int not null primary key,complain varchar(100))")
mycursor.execute("create table if not exists customer(user_id int not null,name varchar(25) not null,number varchar(10) primary key,date date not null)")
mycursor.execute("create table if not exists cylander(order_id int not null,user_id int primary key,name varchar(25) not null,order_date date not null)")
mycursor.execute("create table if not exists sno(user_id int not null,order_id int not null)")
mycursor.execute("create table if not exists staff(username varchar(25) not null,pass varchar(25) not null)")
mydb.commit()
x=0
#user id-10000
#order id=6001
mycursor.execute("select * from sno")
for i in mycursor:
    x=1
if x==0:
    mycursor.execute("insert into sno values(10000,6001)")
    mydb.commit()
x=0
mycursor.execute("select*from staff")
for i in  mycursor:
    x=1
if x==0:
    mycursor.execute("insert into staff values('admin','1234')")
    mydb.commit()
while True:
    print("""
1.Customer Login
2.Staff Login
3.Exit
""")
    ch=int(input("Enter your choice:"))
    if ch==1:
        loop1='n'
        while loop1=='n' or loop1=='N':
            print("""
1.Login
2.New User
3.Go Back
""")
            ch=int(input("Enter your choice:"))
            if ch==1:
                user=input("Enter your user_id:")
                mycursor.execute("select*from customer where user_id='"+user+"'")
                x=0
                for i in mycursor:
                    t_user,t_name,t_num,t_date=i
                    x=1
                if x==0:
                    print("No user Find Please Register It First.")
                else:
                    print(f"(t_name)Logged in Successfully...")
                    print("""
                1.Book Your Cylander
                2.MyOrder
                3.Billing Details
                4.Complain
                5.Cancel Order
                6.Surrender Your Connection
                7.Log out""")
                    ch=int(input("Enter your choice:"))
                    if ch==1:
                        sure=input("Are You Sure(y/n):").lower()
                        if sure=='y':
                            mycursor.execute("select*from sno")
                            for i in mycursor:
                                t_user,t_order=i
                            t_order+=1
                            mycursor.execute("insert into cylander values('"+str(t_order)+"','"+str(user)+"','"+t_name+"',now())")
                            mycursor.execute("update sno set order_id='"+str(t_order)+"'")
                            mydb.commit()
                            print("Order placed successfully and you can pay usnig Cash On Delivery or Online using Net Banking as you wish.")
                    elif ch==2:
                        mycursor.execute("select*from cylander")
                        for i in mycursor:
                            t_order,t_user,t_name,t_odate=i
                        print(f"Order ID->{t_order}")
                        print(f"User ID->{t_user}")
                        print(f"User Name->{t_name}")
                        print(f"Order Date->{t_odate}")
                        print(f"Your Cylander will be delivered within 20 days from{t_order}")
                    elif ch==3:
                        print("Your Amount to be paid is 1100.")
                    elif ch==4:
                        print("Please enter your complain is short.")
                        mycursor.execute("select*from complain where user_id='"+user+"'")
                        x=0
                        for i in mycursor:
                            t_user,t_complain=i
                            x=1
                        if x==0:
                            complain=input("Enter your complain.:")
                            mycursor.execute("insert into complain values('"+str(user)+"','"+complain+"')")
                            mydb.commit()
                        else:
                            print(f"{complain}")
                    elif ch==5:
                        sure=input("Are you sure you want to cancel the order.:").lower()
                        if sure=='y':
                            mycursor.execute("delete from cylander where user_id='"+str(user)+"'")
                            mydb.commit()
                        elif sure=='n':
                            print("Your order is still on....")
                    elif ch==6:
                        sure=input("Are you Sure(/n):").lower()
                        if sure=='y':
                            mycursor.execute("delete from customer where user_id='"+str(user)+"'")
                            mydb.commit()
                            print("Successfully deleted.")
                        elif ch=='n':
                            print("okk You connection is not cancelled.")
                    elif ch==7:
                        break
            elif ch==2:
                name=input("Enter your name:")
                num=input("Enter your number:")
                mycursor.execute("select* from sno")
                for i in mycursor:
                    t_user,t_order=i
                t_user+=1
                mycursor.execute("insert into customer values('"+str(t_user)+"','"+name+"','"+num+"',now())")
                mycursor.execute("update sno set user_id='"+str(t_user)+"'")
                mydb.commit()
                print(f"Registered Successfully with user ID{t_user}")
            elif ch==3:
                break
    elif ch==2:
        pas=input("Enter your password:")
        mycursor.execute("select * from staff")
        for i in mycursor:
            t_username,t_pas=i
        if pas==t_pas:
            print("Logged in Successfully...")
            loop3='n'
            while loop3=='n' or loop3=='N':
                print("""
        1.View Orders
        2.Delet Orders
        3.Delete Connection
        4.Logout
    """)
                ch=int(input("Enter your choice:"))
                if ch==1:
                    mycursor.execute("select * from cylander")
                    for i in mycursor:
                        t_order,t_user,t_name,t_odate=i
                        print(f"{t_order}|{t_user}|{t_name}|{t_odate}")
                elif ch==2:
                    user_id=int(input("Enter User_id:"))
                    mycursor.execute("delete from cylander where user_id='"+str(user_id)+"'")
                    mydb.commit()
                elif ch==3:
                    user_id=int(input("Enter User_id:"))
                    mycursor.execute("delete from customer where user_id='"+str(user_id)+"'")
                    mycursor.execute("delete from cylander where user_id='"+str(user_id)+"'")
                    mydb.commit()
                elif ch==4:
                    break
            else:
                print("Worng Password...")
    elif ch==3:
        break
