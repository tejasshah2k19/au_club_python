import  mysql.connector as c


"""
    open mysql command line 
    enter password
    create dabase pythonclub; 
    use pythonclub;
    create table users (
        userId integer primary ket auto_increment,
        fname varchar(30),
        email varchar(30),
        password varchar(30)
    );
    
"""

#pip install mysql-connector-python



mydb = c.connect(host="localhost",user="root",password="root",db="pythonclub")
cur = mydb.cursor() # this cursor is responsible to execute any query in db
#cur.execute("show tables")
#data = cur.fetchall()
#print(data)

#cur.callproc("procedure")

def listAll():
    cur.execute("select * from users")
    data = cur.fetchall()
   # print(data)
    print("\n\nAllRecords\n\n")
    for s in data:
        print(s)


def insertRecord():
    print("Enter firstname email and password")
    firstName = input()
    email = input()
    password = input()

    cur.execute("insert into users (fname,email,password) values (%s,%s,%s)",(firstName,email,password))

    print(cur.rowcount,"  record(s) inserted")

    cur.execute("commit")

def deleteRecord():
    fname = input("Enter name")
    cur.execute("delete from users where fname like %s",(fname,))
    if cur.rowcount == 0:
        print("Name not found")
    else:
        print(cur.rowcount," record(s) deleted")

    cur.execute("commit")

def getDataByEmail(email):
    cur.execute("select * from users where email like %s",(email,))
    if cur.rowcount == 0:
        return None
    else:
        user = cur.fetchone()
        return user

def updateUser(oldUser):

    firstName = olduser[1]
    password = olduser[3]
    email = olduser[2]

    print("your first name : ",firstName)
    choice = input("do you want to update name? Yy|Nn")
    if choice == "y" or choice == "Y":
        firstName = input("enter new first name")


    print("your password : ", password)
    choice = input("do you want to update password? Yy|Nn")
    if choice == "y" or choice == "Y":
        password = input("enter password")

    cur.execute("update users set fname = %s , password = %s where email = %s",(firstName,password,email))
while True:
    print("0 for exit\n1 for insert\n2 for list\n3 for delete\n4 for update\nenter choice")
    choice = int(input())

    if choice == 1:
        insertRecord()
    elif choice == 2:
        listAll()
    elif choice == 3:
        deleteRecord()
    elif choice == 4:
        print("enter email ")
        email = input()

        olduser = getDataByEmail(email)
        if olduser == None:
            print("Invalid user")
        else:
            updateUser(olduser)

        # for u in olduser:
        #     updateUser(u)



    elif choice == 0:
        break
    else:
        print("invalid choice")


cur.close()
mydb.close()
