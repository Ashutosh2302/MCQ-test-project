import mysql.connector,os
from datetime import datetime
mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='exam')
cur=mydb.cursor()
from login import *
login=menu()
if(login):
    while(True):
        os.system('cls')
        print("\nHi",login[1])
        print("Welcome to MCQ test platform")
        d=dict()
        inans=[]
        score=0
        c=0
        z=0
        o=0
        print()
        print("******MCQ TEST****")
        print()
        print("There will be 5 questions in the test")
        print()
        print("1. C++")
        print("2. Python")
        print("3. HTML")
        print("4. View All your results")
        print("5. exit")
        x=int(input("Enter your choice of subject: "))
        if x==1:
            s="Select question_id,question,option1,option2,option3,option4,correct_ans FROM cppTest ORDER BY RAND() limit 5"
            try:
                cur.execute(s)
            except mysql.connector.errors.ProgrammingError:
                print("Error! Table Doesn't Exist")
            else:
                print()
                results=cur.fetchall()
                 
                print() 
                for row in results:
                    c=c+1
                    print("Q.",c,".",row[1])
                    print()
                    print("1. ",row[2])
                    print("2. ",row[3])
                    print("3. ",row[4])
                    print("4. ",row[5])
                    ans=int(input("Enter Your answer- "))
                    print()
                    if row[6]==ans:
                        score=score+1
                    else:
                        d[c]=row[row[6]+1]
                        z=z+1
                        inans.append(row[ans+1])
                print()
                print("            Your Score-",score,"out of 5")
                if z>0:
                   print("Incorrect Answers- ")
                   print()
                   for a,b in d.items():
                     print("Question. ", a)
                     print("Correct Answer: ",b)
                     print("Your Answer:    ",inans[o])
                     o+=1
                     print()
                s="INSERT into test_results VALUES(%s,%s,%s,%s,%s,%s)"
                a=login[1]
                b="c++"
                c=datetime.now()
                d=score
                e=5
                if score>2:
                    f="Pass"
                else:
                    f="Fail"
                t=(a,b,c,d,e,f)
                cur.execute(s,t)
                mydb.commit()
            
        if x==2:
            s="Select question_id,question,option1,option2,option3,option4,correct_ans FROM pythonTest ORDER BY RAND() limit 5"
            try:
                cur.execute(s)
            except mysql.connector.errors.ProgrammingError:
                print("Error! Table Doesn't Exist")
            else:
                print()
                results=cur.fetchall()
                
                print() 
                for row in results:
                    c=c+1
                    print("Q.",c,".",row[1])
                    print()
                    print("1. ",row[2])
                    print("2. ",row[3])
                    print("3. ",row[4])
                    print("4. ",row[5])
                    ans=int(input("Enter Your answer- "))
                    print()
                    if row[6]==ans:
                        score=score+1
                    else:
                        d[c]=row[row[6]+1]
                        z=z+1
                        inans.append(row[ans+1])
                print()
                print("                 Your Score-",score,"out of 5")
                if z>0:
                   print()
                   print("Incorrect Answers- ")
                   print()
                   for a,b in d.items():
                     print("Question. ", a)
                     print("Correct Answer: ",b)
                     print("Your Answer:    ",inans[o])
                     o+=1
                     print()
                s="INSERT into test_results VALUES(%s,%s,%s,%s,%s,%s)"
                a=login[1]
                b="python"
                c=datetime.now()
                d=score
                e=5
                if score>2:
                     f="Pass"
                else:
                     f="Fail"
                t=(a,b,c,d,e,f)
                cur.execute(s,t)
                mydb.commit()
        if x==3:
            s="Select question_id,question,option1,option2,option3,option4,correct_ans FROM htmltest ORDER BY RAND() limit 5"
            try:
                cur.execute(s)
            except mysql.connector.errors.ProgrammingError:
                print("Error! Table Doesn't Exist")
            else:
                print()
                results=cur.fetchall()
                
                print() 
                for row in results:
                        c=c+1
                        print("Q.",c,".",row[1])
                        print()
                        print("1. ",row[2])
                        print("2. ",row[3])
                        print("3. ",row[4])
                        print("4. ",row[5])
                        ans=int(input("Enter Your answer- "))
                        print()
                        if row[6]==ans:
                            score=score+1
                        else:
                            d[c]=row[row[6]+1]
                            z=z+1
                            inans.append(row[ans+1])
                print()
                print("                 Your Score-",score,"out of 5")
                if z>0:
                   print()
                   print("Incorrect Answers- ")
                   print()
                   for a,b in d.items():
                     print("Question. ", a)
                     print("Correct Answer: ",b)
                     print("Your Answer:    ",inans[o])
                     o+=1
                     print()
                s="INSERT into test_results VALUES(%s,%s,%s,%s,%s,%s)"
                a=login[1]
                b="HTML"
                c=datetime.now()
                d=score
                e=5
                if score>2:
                    f="Pass"
                else:
                    f="Fail"
                t=(a,b,c,d,e,f)
                cur.execute(s,t)
                mydb.commit()
        if x==4:
            s="Select * from test_results where username=%s"
            a=login[1]
            cur.execute(s,(a,))
            results=cur.fetchall()
            print()
            print("Fetching all your results...")
            print()
            time.sleep(5)
            print("Total entries: ",cur.rowcount)
            print()
            for e in results: 
                print("Subject:        ",e[1])
                print("Date & Time:    ",e[2])
                print("marks obtained: ",e[3])
                print("Total Marks:    ",e[4])
                print("Result:         ",e[5])
                print()
                
        if x==5:
            break;
        input("Press any key to continue...")
print("Thankyou for using this application")
input("Press any key to continue...")
