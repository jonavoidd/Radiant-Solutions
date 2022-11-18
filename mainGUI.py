from tkinter import *
from bills import *


root = Tk()
root.title('S.E.B.A.T.')
root.geometry('500x250')



def outside():

    adminButton = Button(root, text='Admin', height=2, width=10, fg='black', bg='gray', font=('arial', 20), command=openAdmin)
    adminButton.pack()
    customerButtom = Button(root, text='Customer', height=2, width=10, fg='black', bg='gray', font=('arial', 20))
    customerButtom.pack()

    outerFrame = Frame(root)
    outerFrame.pack(expand=True)
    adminFrame = Frame(master=outerFrame, bg='gray')    
    adminFrame.pack(expand=True)
    billFrame = Frame(master=outerFrame, bg='gray')
    billFrame.pack(expand=True)
    profitFrame = Frame(master=outerFrame, bg='gray')
    profitFrame.pack(expand=True)

    def openAdmin():
        adminButton.destroy()
        customerButtom.destroy()
    
        def Bills():
            bills.destroy()
            profits.destroy()
            sales.destroy()
            tax.destroy()
            exit.destroy()
            to_pay = Label(master=billFrame, fg='white', bg='black')
            to_pay.config(text=f'Electricity: {electricity.get_bills()}\nWater: {water.get_bills()}')
            to_pay.pack()

        def Profits():
            bills.destroy()
            profits.destroy()
            sales.destroy()
            tax.destroy()
            exit.destroy()
            earn = Label(master=profitFrame, fg='white', bg='black')
            earn.config()
            earn.pack()

        def Sales():
            bills.destroy()
            profits.destroy()
            sales.destroy()
            tax.destroy()
            exit.destroy()
            sold = Label(master=profitFrame, fg='white', bg='black')
            sold.config()
            sold.pack()

        def Tax():
            bills.destroy()
            profits.destroy()
            sales.destroy()
            tax.destroy()
            exit.destroy()
            toll = Label(master=profitFrame, fg='white', bg='black')
            toll.config()
            toll.pack()

        def Exit():
            bills.destroy()
            profits.destroy()
            sales.destroy()
            tax.destroy()
            exit.destroy()
            outerFrame.pack()


        bills = Button(master=adminFrame, text='Bills', height=2, width=10, fg='white', bg='black', command=Bills)
        bills.pack()
        profits = Button(master=adminFrame, text='Profits', height=2, width=10, fg='white', bg='black', command=Profits)
        profits.pack()
        sales = Button(master=adminFrame, text='Sales', height=2, width=10, fg='white', bg='black', command=Sales)
        sales.pack()
        tax = Button(master=adminFrame, text='Tax', height=2, width=10, fg='white', bg='black', command=Tax)
        tax.pack()
        exit = Button(master=adminFrame, text='Exit', height=2, width=10, fg='white', bg='black', command=Exit)
        exit.pack()

    



root.mainloop()