from tkinter import *
window=Tk()
window.title('Simple Interest Calculator')
window.geometry("500x300")
window.configure(bg='lightcyan')

def calculate():
    prin=int(principalentry.get())
    rat=int(rateentry.get())
    tim=int(timeentry.get())
    amount=(prin*rat*tim)/100
    si = Label(text=f"{amount}", font=("Comic Sans MS",30))
    si.place(x=200,y=220)

principal=Label(window, text="Principal:", fg = "black", bg = "lightcyan", font=("Comic Sans MS", 15),bd=5)
rate=Label(window, text="Rate of Interest:", fg = "black", bg = "lightcyan", font=("Comic Sans MS", 15),bd=5)
time=Label(window, text="Principal:", fg = "black", bg = "lightcyan", font=("Comic Sans MS", 15),bd=5)

principal.place(x=50,y=20)
rate.place(x=50,y=90)
time.place(x=50,y=160)

interest=Label(window, text="Interest:", font=("Comic Sans MS", 15))
interest.place(x=50,y=230)

principalvalue=StringVar()
ratevalue=StringVar()
timevalue=StringVar()

principalentry=Entry(window,text=principalvalue, font=("Comic Sans MS", 20), width=8)
rateentry=Entry(window,text=ratevalue, font=("Comic Sans MS", 20), width=8)
timeentry=Entry(window,text=timevalue, font=("Comic Sans MS",20), width=8)

principalentry.place(x=200, y=20)
rateentry.place(x=200, y=90)
timeentry.place(x=200, y=160)

btn = Button(text="Calculate", font=("Comic Sans MS",15), command=calculate)
btn2 = Button(window,text="Exit", command=lambda:exit(),font=("Comic Sans MS",15), width=8)
btn.place(x=350,y=20)
btn2.place(x=350, y=90)

window.mainloop()