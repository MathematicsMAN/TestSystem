from tkinter import *
from tkinter import messagebox as mb


def press_ans():
    if var.get() == right_ans:
        mb.showinfo("ответ", "Верно!!")
    else:
        mb.showerror("ответ", "Не верно!!")

root = Tk()
root.title("Тест")
root.geometry('420x300')

ask1 = Label(text="Сколько будет 2 + 2?",
             font=('Comic San MS', 24, 'bold'),
             bg='#112233', fg='#00FF00', bd=5
             )
ask1.pack(anchor='n')

right_ans = 4

var = IntVar()
var.set(0)
ans1 = Radiobutton(text='3', value=3, variable=var,
                   font=('Comic San MS', 24, 'bold'))
ans2 = Radiobutton(text='4', value=4, variable=var,
                   font=('Comic San MS', 24, 'bold'))
ans3 = Radiobutton(text='5', value=5, variable=var,
                   font=('Comic San MS', 24, 'bold'))
ans1.place(x=10, y=60)
ans2.place(x=10, y=100)
ans3.place(x=10, y=140)

btn = Button(text="Ответить", command=press_ans)
btn.place(x=30, y=200)

root.mainloop()

