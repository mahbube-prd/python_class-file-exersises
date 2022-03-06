from cProfile import label
import sqlite3
from tkinter import *
from turtle import update
window=Tk()
class work():
    data_base="example.db"
    def __init__(self):
        self.mydb=sqlite3.connect(self.data_base)
        self.my_cursor=self.mydb.cursor()
    
    def close_database(self):
        self.mydb.close()

    def create_table(self):
        sql="CREATE TABLE WORK (id INT AUTO_INCREMENT PRIMARY KEY, name warchar(255))"
        self.my_cursor.execute(sql)
    
    def insert_data(self,id,name):
        sql= "INSERT INTo work (id,name) VALUES(?,?)"
        val=(id,name)
        self.my_cursor.execute(sql,val)
        self.mydb.commit()
    
    def delete_data(self,id):
        sql="DELETE FROM work WHERE id=?"
        val=(id,)
        self.my_cursor.execute(sql)
        self.mydb.commit()

    def select_all(Self):
        sql="SELECT *FROM WORK"
        result= Self.my_cursor.execute(sql)
        return result.fetchall()

    def update_one(self,id,name,value):
        sql=f"UPDATE work SET `{name}`='{value}'WHERE id={id}"
        self.my_cursor.execute(sql)
        self.mydb.commit()
  
def Update():
    my_ent = ent.get()
    lbl["text"]=my_ent
    obj.update_one(4,"name",my_ent)
    
obj=work()
# obj.create_table()
# obj.insert_data(4,"om")
# obj.delete_data(2)
# obj.update_one(1,"id","3")
result = obj.select_all()
for i in result:
    lbl=Label(window,text=i[1])
    lbl.place(x=40,y=50)
ent=Entry()
ent.place(x=100,y=70)

btn = Button(window,text="update",command=Update)
btn.place(x=140,y=140)


window.geometry("900x600")
window.mainloop()

obj.close_database()

    
