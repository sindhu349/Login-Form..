import tkinter as k
import tkinter.messagebox as m

def login():
       username=e1.get()
       password=e2.get()
       if username=='Sin':
              if password=='sin':
                     m.showinfo('info','Succesfully Logged in')
              else:
                    m.showinfo('info','invalid password')
       else:
              m.showinfo('info','invalid username')

w=k.Tk()
w.title('Login form')
w.geometry('400x300')
w.configure(bg='#e75480')

title_font=('Helvetica',20,'bold')
label_font=('Helvetica',14)
button_font=('Helvetica',12)

k.Label(w,text='Login Form',bg='#4CAF50',fg='#fff',font=title_font).grid(row=0,column=0,columnspan=2,pady=(20,10),sticky='n')
k.Label(w,text='username',bg='#e75480',fg='black',font=label_font).grid(row=1,column=0,padx=10,pady=5,sticky='w')
k.Label(w,text='password',bg='#e75480',fg='black',font=label_font).grid(row=2,column=0,padx=10,pady=5,sticky='w')

e1=k.Entry(w,width=20,font=label_font)
e1.grid(row=1,column=1,padx=10,pady=5,sticky='e')
e2=k.Entry(w,width=20,show='*',font=label_font)
e2.grid(row=2,column=1,padx=10,pady=5,sticky='e')

b1=k.Button(w,text='Login',command=login,fg='black',bg='#4CAF50',font=button_font)
b1.grid(row=3,column=0,columnspan=2,pady=10)

w.mainloop()

