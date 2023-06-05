from tkinter import *

import mysql.connector

db= mysql.connector.connect(host='localhost', user='root', password='', db='employee')

cursor = db.cursor()

def calculate():

    employee_annualsalary.set (employee_salary.get()* 12)

def add():

    EmpId=employee_id.get()

    EmpName=employee_name.get()

    EmpDesgination= employee_designation.get()

    EmpSalary= employee_salary.get()

    AnnualSalary =employee_annualsalary.get()

    cursor.execute('insert into employeedetails values (%s, %s, %s, %s, %s)',[EmpId,EmpName,EmpDesgination,EmpSalary,AnnualSalary])

    db.commit()


def view():

    id= employee_id.get()

    cursor.execute('select * from employeedetails where Empid=%s',[id])

    data =cursor.fetchone()

    employee_name.set(data[1])

    employee_designation.set(data[2])

    employee_salary.set(data[3])

    employee_annualsalary.set(data[4])


def update():

    EmpId= employee_id.get()

    EmpName=employee_name.get()

    EmpDesignation=employee_designation.get()

    EmpSalary= employee_salary.get()

    AnnualSalary= employee_annualsalary.get()

    cursor.execute('update employeedetails set EmpName=%s, EmpDesignation=%s, EmpSalary=%s, AnnualSalary=%s where id=%s' ,[EmpName,EmpDesignation,EmpSalary,AnnualSalary,EmpId])

    db.commit()


def delete():

    id=employee_id.get()

    cursor.execute('delete from employeedetails where EmpId=%s',[id])

    db.commit()

def clear():

    employee_id.set('')

    employee_name.set('')

    employee_designation.set('')

    employee_salary.set('')

    employee_annualsalary.set('')


def overall():

    global viewpage

    viewpage = Toplevel(obj)


    viewpage.geometry('900x500')

    viewpage.title('Employee Mangement')

    viewpage.configure(bg='Lightblue')

    cursor.execute('select * from employeedetails')

    data= cursor.fetchall()

    rows = len(data)

    cols = len(data[0])

    Label(viewpage, text='EmpId', font=('calibri',15, 'bold'), bg='lightblue').grid(row=0,column=0)
    Label(viewpage, text='EmpName', font=('calibri', 15, 'bold'), bg='Lightblue').grid(row=0,column=1)

    Label(viewpage, text='EmpDesignation', font=('calibri' ,15, 'bold'), bg='lightblue').grid(row=0,column=2)

    Label(viewpage, text='EmpSalary', font=('calibri', 15, 'bold'), bg='Lightblue').grid(row=0,column=3)

    Label(viewpage, text="Annual Salary", font=('calibri', 15, 'bold'), bg='lightblue').grid(row=0,column=4)

    for i in range (rows):

        for j in range(cols):

            s=Entry(viewpage, font=("calibri",13))
            s.grid(row=i + 1, column=j)
            s.insert(END, data[i][j])

obj = Tk()

obj.geometry('650x500')

obj.title('Access Control Matrix')

obj.configure(bg='Lightgreen')

Label (obj, text='Employee Mangement', font=('calibri',20), fg='green'). place (x=240,y=18)


employee_id_label = Label (obj, text='EmpID', font=('calibri',17), bg='lightgreen')

employee_id_label.place(x=130,y=70)

employee_id= StringVar()

employee_id_entry = Entry(obj, textvariable=employee_id, font=('calibri',15))

employee_id_entry.place(x=290,y=70)


employee_name_label = Label (obj, text='EmpName', font=('calibri',17), bg='lightgreen')

employee_name_label.place(x=130,y=120)

employee_name= StringVar()

employee_name_entry = Entry(obj, textvariable=employee_name, font=('calibri',15))

employee_name_entry.place(x=290,y=120)


employee_designation_label = Label (obj, text='EmpDesignation', font=('calibri',17), bg='lightgreen')

employee_designation_label.place(x=130,y=170)

employee_designation= StringVar()

employee_designation_entry = Entry(obj, textvariable=employee_designation, font=('calibri',15))

employee_designation_entry.place(x=290,y=170)


employee_salary_label = Label (obj, text='EmpSalary', font=('calibri',17), bg='lightgreen')

employee_salary_label.place(x=130,y=220)

employee_salary= IntVar()

employee_salary_entry = Entry(obj, textvariable=employee_salary, font=('calibri',15))

employee_salary_entry.place(x=290,y=220)


employee_annualsalary_label = Label (obj, text='Annual Salary', font=('calibri',17), bg='lightgreen')

employee_annualsalary_label.place(x=130,y=270)

employee_annualsalary= IntVar()

employee_annualsalary_entry = Entry(obj, textvariable=employee_annualsalary, font=('calibri',15))

employee_annualsalary_entry.place(x=290,y=270)

but_cal=Button(obj,text='Calculate',command=calculate,font=('calibri',11),bg='gray',fg='white',width='8',height='1')
but_cal.place(x=500,y=220)

but_add=Button(obj,text='ADD',command=add,font=('calibri',15),bg='gray',fg='white',width='10',height='1')
but_add.place(x=130,y=350)

but_view=Button(obj,text='  VIEW',command=view,font=('calibri',15),bg='gray',fg='white',width='10',height='1')
but_view.place(x=260,y=350)

but_upd=Button(obj,text='UPDATE',command=update,font=('calibri',15),bg='gray',fg='white',width='10',height='1')
but_upd.place(x=390,y=350)

but_del=Button(obj,text='DELETE',command=delete,font=('calibri',15),bg='gray',fg='white',width='10',height='1')
but_del.place(x=130,y=410)

but_clr=Button(obj,text='CLEAR',command=clear,font=('calibri',15),bg='gray',fg='white',width='10',height='1')
but_clr.place(x=260,y=410)

but_ovr=Button(obj,text='OVERALL',command=overall,font=('calibri',15),bg='gray',fg='white',width='10',height='1')
but_ovr.place(x=390,y=410)

obj.mainloop()