#coding=utf-8
import tinydb,time
import sqlite3
from tqdm import *
def start():
    conn = sqlite3.connect('data.db')
    print "Opened database successfully";
    c = conn.cursor()
    c.execute('''CREATE TABLE COMPANY
           (
           EMAILS           TEXT    NOT NULL,
           PASSWD            TEXT     NOT NULL);''')
    print "Table created successfully"
    conn.commit()
    conn.close()

def test():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    print "Opened database successfully";

    c.execute("INSERT INTO COMPANY (EMAILS,PASSWD) \
          VALUES ('747306970@qq.com','123456')");

    conn.commit()
    print "Records created successfully";
    conn.close()


def search():
    conn = sqlite3.connect("/Volumes/My Passport/database/Exploit.in/"+'data.db')
    c = conn.cursor()
    print "Opened database successfully";
    start = time.time()
    cursor = c.execute("""SELECT *
     FROM COMPANY
     WHERE EMAILS IN (SELECT EMAILS
                  FROM COMPANY
                  WHERE PASSWD = 123456) ;""")
    num=0
    for row in tqdm(cursor):
        num=num+1
        #print "EMAILS = ", row[0]
    print num
    print "Operation done successfully";
    conn.close()
    end = time.time()
    print(str(end - start) + "s")


def rewrite(file):
    file_object = open(file,'rU')
    start=time.time()
    count=len(["" for line in open(file, "r")])
    print(str(count)+"items")

    conn = sqlite3.connect("/Volumes/My Passport/database/Exploit.in/"+'data.db')
    c = conn.cursor()
    print "Opened database successfully";


    try:
        for line in tqdm(file_object):
            try:
                text=line.split(":")
                content="INSERT INTO COMPANY (EMAILS,PASSWD) \
                          VALUES ('"+text[0]+"','"+text[1].replace("\n","")+"')"
                #print content
                c.execute(content)
            except Exception as e:
                pass
    finally:
        conn.commit()
        print "Records created successfully"
        conn.close()
        file_object.close()


    end=time.time()
    print(str(end-start)+"s")
#rewrite("/Volumes/My Passport/database/Exploit.in/1.txt")
search()
#for i in range(8,111):
#    rewrite("/Volumes/My Passport/database/Exploit.in/"+str(i)+".txt")
#    print str(i)+".txt finished"




