import mysql.connector
mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="rajkumardb")
mysqlcursor=mysqldb.cursor()

# #created table into databae
## mysqlcursor.execute("create table knowledge_base(rollno INT, name VARCHAR(30),marks INT)")

# try:
# # insert value into table(knowledge_base)
   
#     mysqlcursor.execute("insert into knowledge_base(rollno,name,marks) values(6,'RAJA',10)")
#     # here i am commiting that recorde is inserted into database
#     mysqldb.commit()   # what is commit()
#     # display msg to the user
#     print("record is inserted into table")
# except:
#     mysqldb.rollback()
# mysqldb.close()  # yaha db se connection close ho raha hai




#DISPLAY RECORDS

try:
    mysqlcursor.execute("select * from knowledge_base")
    result=mysqlcursor.fetchall()
    for i in result:
        rollno=i[0]
        name=i[1]
        marks=i[2]
        print(rollno,name,marks)
except:
    print("some issue in the code")
mysqlcursor.close()


# # UDATE the records
# try:
#     mysqlcursor.execute("update knowledge_base set name='Sachin' where rollno=2")
#     mysqldb.commit()
#     print("record updated")
# except:
#     mysqldb.rollback()


# # DELETE record
# try:
#     mysqlcursor.execute("delete from knowledge_base where rollno=6")
#     mysqldb.commit()
#     print("record deleted")
# except:
#     mysqldb.rollback()
# mysqldb.close()

