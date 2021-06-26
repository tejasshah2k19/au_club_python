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


while True:
    print("0 for exit\n1 for insert\n2 for list\nenter choice")
    choice = int(input())

    if choice == 1:
        insertRecord()
    elif choice == 2:
        listAll()
    elif choice == 0:
        break
    else:
        print("invalid choice")


cur.close()
mydb.close()
