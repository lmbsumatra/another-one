import openpyxl
from balanceinq import balanceInq

from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
from tkinter import simpledialog
root=Tk()
root.geometry('600x500')
root.resizable(0,0)

def loginPg():
    
    mainFrame = Frame(root, height=500, width=600)
    mainFrame.place(x=0,y=0)
    print("Log In")

    # getting log in infos
    get_username = '04588IIIUD'
    get_password = 'Password12345'
    counter = 0

    # checking for username
    for i, j, k, l, m, n, o, p, q in rws:
        if i == get_username:
            db_user.extend([i, j, k, l, m, n, o, p, q])    # if user is true, append data to db_user list
        counter = counter + 1
        
    # if user false, send a notice
    if len(db_user) == 0:
        print("is empty")

    # checking password
    if get_password == db_user[8]:
        balanceInq(db_user[0], db_user[7])

    # changing user infos
    change = 'I'+str(4)
    data[change].value = 'heyheyhey'
    xl.save("nag-iisa-lang-to.xlsx")
    mainFrame.mainloop()
            
db_user = []    
xl = openpyxl.load_workbook("nag-iisa-lang-to.xlsx")
data = xl.active
rws = data.iter_rows(min_row = 1, max_col= 9, max_row = None, min_col = 1, values_only = True)


loginPg()