from logging import log
import mysql.connector

def login_to_database():
    f = open("Passwords.txt")
    L = f.readlines()
    
    username = L[0].strip('\n')
    password = L[1].strip('\n')
    myconn = mysql.connector.connect(
    host="localhost",
    user=username,
    password=password
    )

    return myconn


def newApp():
    conn = login_to_database()
    cur = conn.cursor()
    cur.execute("show databases")
    
    myresult = cur.fetchall()
    if ('memoappdb',) not in myresult:
        cur.execute("create database MemoAppDB")
    cur.execute("use memoappdb")
    cur.execute("show tables")
    myresult = cur.fetchall()
    if ('employeedetails',) not in myresult:
        cur.execute("create table employeedetails(id int PRIMARY KEY,name varchar(25) NOT NULL, email varchar(100))")


def getemployees():
    conn = login_to_database()
    cur = conn.cursor()
    
    newApp()
    cur.execute("use memoappdb")
    cur.execute("select * from employeedetails")
    myresult = cur.fetchall()
    L = [str(i[0]) + ':' + i[1] for i in myresult]
    return L

def updatevals(id,name,email):
    mycon = login_to_database()
    cur = mycon.cursor()
    newApp()
    cur.execute("use memoappdb")
    command = "insert into employeedetails values(" +id+',"'+name+'","'+email+'")'
    cur.execute(command)
    mycon.commit()
    return 1


def getRecipientEmail(r):
    conn = login_to_database()
    cur = conn.cursor()
    cur.execute("use memoappdb")
    cmmnd = 'select email from employeedetails where id = "' + r + '"'
    cur.execute(cmmnd)
    res = cur.fetchall()
    return res[0][0]
