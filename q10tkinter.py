import tkinter as tkk
s = tkk.Tk()
s.geometry('500x500')

l =  tkk.StringVar()
m =  tkk.StringVar()
n =  tkk.StringVar()

def prt():
    a = int(l.get())
    b = int(m.get())
    c = int(n.get())
    print('Your simple interest is',a*b*c)
tkk.Label(s,text='Principal Amount',).grid(row = 100, column = 100)
tkk.Label(s,text='Rate',).grid(row = 200, column =100 )
tkk.Label(s,text='Time',).grid(row =300 , column =100 )
tkk.Label(s, text= 'Simple Interest Calculator').grid(row = 0, column = 150)
tkk.messagebox.showinfo("Simple Interest", prt)
P = tkk.Entry(s,  textvariable = l).grid(row =100, column = 150)
R = tkk.Entry(s, textvariable = m).grid(row =200, column = 150)
T = tkk.Entry(s, textvariable = n).grid(row =300, column = 150)
B = tkk.Button(s, text = 'Press for Simple Interest', command = prt ).grid(row = 400, column =150)
s.mainloop()