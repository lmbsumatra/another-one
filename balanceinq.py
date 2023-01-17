from openpyxl import load_workbook

from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
from tkinter import simpledialog

# root=Tk()
# root.geometry('600x500')
# root.resizable(0,0)

# trial uli for acct no and balance

def balanceInq(acct_no, bal_inq):

    mainFrame = Frame(root, height=500, width=600)
    mainFrame.place(x=0,y=0)

    x = acct_no
    m = bal_inq
    print("Balance Inquiry\n")

    print("\nAccount Number: ", x)

    print("Your balance: ", m)

    print("After reviewing your account balance,\nenter [C] to continue.")

    # mainFrame.mainloop()
    