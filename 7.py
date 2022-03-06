
import json
import sqlite3
file = open("E:\python-projct\daba\db.json", "r")
myjson = file.read()
file.close()
mydic=json.loads(myjson)
# print(mydic)
data_list=mydic["user"]
print(data_list)
mydb=sqlite3.connect("example.db")
mycursor= mydb.cursor()
# mycursor.execute("CREATE TABLE USER(id INT AUTO_INCREMENT PRIMARY KEY ,email VARCHAR(255),age VARCHAR(255))")
sql="INSERT INTO user(id,email,age) VALUES(?,?,?)"
for i in data_list:
    val=(i["id"],i["email"],i["age"])
#mycursor.execute(sql,val)
sql="SELECT email FROM user"
mecute= mycursor.execute(sql)
result=mecute.fetchall()
print(result)
print("enter your email:")
email=input()
for i in result:
    # print(i[0])
    if (email==i[0]):
        print("yes")
    else:
        print("no")
    
mydb.commit()
mydb.close()