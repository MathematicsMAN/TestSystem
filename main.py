import json
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

with open("test.json", "r", encoding="UTF-8") as file_in:
    data = json.load(file_in)

for ask in data["asks"]:
    ask1 = Label(text=ask["ask"],
                 font=('Comic San MS', 24, 'bold'),
                 bg='#112233', fg='#00FF00', bd=5
                 )
    ask1.pack(anchor='n')

    var = StringVar()
    var.set("0")
    n = len(ask["ans"])
    for i in range(n):
        ans = Radiobutton(text=ask["ans"][i],
                          value=ask["ans"][i],
                          variable=var,
                           font=('Comic San MS', 12, 'bold'))
        ans.place(x=10, y=60 + i*30)
    right_ans = ask["right_ans"]
    btn = Button(text="Ответить", command=press_ans)
    btn.place(x=30, y=60 + n*30)

root.mainloop()

