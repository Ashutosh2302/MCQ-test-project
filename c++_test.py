import mysql.connector,os
mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='exam')
cur=mydb.cursor()
while(True):
    os.system('cls')
    print("1. Create C++ test table")
    print("2. Add Question")
    print("3. Show All Questions")
    print("4. Delete Question")
    print("5. Delete All Questions")
    print("6. Delete Table")
    print("7. Exit")
    x=int(input("Enter your choice"))
    if x==1:
        s="CREATE table cppTest(question_id int PRIMARY KEY,question varchar(200),option1 varchar(100),option2 varchar(100),option3 varchar(100),option4 varchar(100),correct_ans int)"
        try:
         cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
         print("Table Already Exists")
        else:
         print("Table Created!")
            
    if x==2:
        s="INSERT into cppTest VALUES(%s,%s,%s,%s,%s,%s,%s)"
        a=input("Enter Question ID: ")
        b=input("Enter Question: ")
        c=input("Enter option 1: ")
        d=input("Enter option 2: ")
        e=input("Enter option 3: ")
        f=input("Enter option 4: ")
        g=input("Enter correct answer: ")
        b1=(a,b,c,d,e,f,g)
        try:
            cur.execute(s,b1)
        except mysql.connector.errors.ProgrammingError:
            print("Error! Table Doesn't Exist")
        except mysql.connector.errors.IntegrityError:
            print("Error! Question ID cannot be same")
        else:
            print("Insertion Successfull")
            mydb.commit()
            
    if x==3:
        s="Select * FROM cppTest"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Error! Table Doesn't Exist")
        else:
            print()
            results=cur.fetchall()
            print("Total Enteries in Table: ",cur.rowcount)
            print()
           
            for row in results:
                print("Question ID  ",row[0])
                print("Question     ",row[1])
                print("option 1     ",row[2])
                print("option 2     ",row[3])
                print("option 3     ",row[4])
                print("option 4     ",row[5])
                print("correct ans  ",row[6])
                print()
                
    if x==4:
        s="DELETE FROM cppTest WHERE question_id=%s"
        a=input("Enter Question ID: ")
        try:
            cur.execute(s,(a,))
        except mysql.connector.errors.ProgrammingError:
            print("Error! Table Doesn't Exist")
        else:
            print("Deletion Successfull")
            mydb.commit()
            
    if x==5:
        s="TRUNCATE table cppTest"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Error! Table Doesn't Exist")
        else:
            print("Deletion Successfull")
            mydb.commit()
            
    if x==6:
        s="DROP table cppTest"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Error! Table Doesn't Exist")
        else:
            print("Deletion Successfull")
            mydb.commit()

    if x==7:
         break;
    input("Press any key to continue...")
print("Thankyou For Using this application")
input("Press any key to exit...")




        


            
