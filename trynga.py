import tkinter
from tkinter import *
from tkinter import messagebox

def depositPg(acct_no, acct_balance):
    
    # depwindow = Tk()
    # depwindow.geometry('500x400')
    # depwindow.title("Deposit")
    # depwindow.configure(bg='skyblue')
    # Label(depwindow, text ='DEPOSIT', font = 'arial 14 bold').pack()

    # text based muna hahaha
    amt_deposit = float(input("Enter amount to be deposited: "))
    acct_balance += amt_deposit
    print("\n Amount Deposited:",amt_deposit)

    print("Account new balance: ", acct_balance)

    return acct_balance
    
    # dep = StringVar()
    # mode = StringVar()
    # #def deposit(self):
    # def Exit():
    #     depwindow.destroy()

    # Label(depwindow, font = 'arial 12 bold',  text ="Enter amount to deposit: ").place(x=10, y = 110)
    # Entry(depwindow, font = 'arial 10', textvariable = dep, bg ='white').place(x=290, y = 110, width=200,height=40)

    # Button(depwindow, font = 'arial 10 bold', text = 'ENTER',padx =2,bg ='limegreen' ,command = mode).place(x=310, y = 260)
    # Button(depwindow, font = 'arial 10 bold',text= 'EXIT', width = 6, command = Exit, bg = 'red').place(x=310, y = 290)

    # depwindow.mainloop()
