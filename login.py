import mysql.connector,os,time
mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='exam')
cur=mydb.cursor()
def signIn():
        os.system('cls')
        print("\n***SIGN IN***\n")
        usernameIn=input("Enter username: ")
        passwordIn=input("Enter password: ")
        t=(usernameIn,passwordIn)
        s="Select * from user";
        cur.execute(s)
        results=cur.fetchall()
        if t in results:
            print("Logging you in...")
            time.sleep(5)
            return 1,usernameIn
        else:
            print("Wrong Credentials, Please try again!!")
            time.sleep(3)
            os.system('cls')
            return(signIn())
            


def signUp():
        os.system('cls')
        print("\n***SIGN UP***\n")
        u=input("Enter username: ")
        p=input("Enter password: ")
        t=(u,p)
        s="INSERT into user VALUES(%s,%s)";
        print()
        try:
                cur.execute(s,t)
        except mysql.connector.errors.IntegrityError:
                print("Error! Username already exist, Please try again!!")
                time.sleep(2)
                os.system('cls')
                signUp()
        else:
                mydb.commit()
                print("Registration successfull")
                print("Please signIn now..")
                time.sleep(2)
                signIn()

def menu():
        print("1. SignIn")
        print("2. SignUp")
        q=int(input("Enter your choice: "))
        if q==1:
             time.sleep(2)
             return(signIn())
        if q==2:
             time.sleep(2)
             signUp()
     

