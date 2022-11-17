from tkinter import *
from bills import *


root = Tk()
root.title('S.E.B.A.T.')
root.geometry('500x250')

def openAdmin(Bills):
    adminButton.destroy()
    customerButtom.destroy()
    
    bills = Button(master=adminFrame, text='Bills', height=2, width=10, fg='white', bg='black')
    bills.pack()

    def Bills():
        bills.destroy()
        profits.destroy()
        sales.destroy()
        tax.destroy()
        exit.destroy()

        bayad = Label(master=billFrame, text=f'Electricity: {electricity.get_bills}', height=2, width=10, fg='white', bg='black')


    profits = Button(master=adminFrame, text='Profits', height=2, width=10, fg='white', bg='black')
    profits.pack()

    sales = Button(master=adminFrame, text='Sales', height=2, width=10, fg='white', bg='black')
    sales.pack()

    tax = Button(master=adminFrame, text='Tax', height=2, width=10, fg='white', bg='black')
    tax.pack()

    exit = Button(master=adminFrame, text='Exit', height=2, width=10, fg='white', bg='black')
    exit.pack()

adminFrame = Frame()    
adminFrame.pack()

billFrame = Frame()
billFrame.pack()

adminButton = Button(root, text='Admin', height=2, width=10, fg='black', bg='gray', font=('arial', 20), command=openAdmin)
adminButton.pack()
customerButtom = Button(root, text='Customer', height=2, width=10, fg='black', bg='gray', font=('arial', 20))
customerButtom.pack()

outerFrame = Frame()
outerFrame.pack()


root.mainloop()