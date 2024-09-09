from tkinter import *

def dismiss(window):
    window.grab_release()
    window.destroy()

def press_yes():
    window = Toplevel()
    window.title("Твой ответ")
    window.geometry("230x50")
    window.protocol("WM_DELETE_WINDOW", lambda: dismiss(window))  # перехватываем нажатие на крестик
    close_button = Button(window, text="Не верный", command=lambda: dismiss(window))
    close_button.pack(anchor="center", expand=1)
    window.grab_set()

def press_no():
    window = Toplevel()
    window.title("Твой ответ")
    window.geometry("230x50")
    window.protocol("WM_DELETE_WINDOW", lambda: dismiss(window))  # перехватываем нажатие на крестик
    close_button = Button(window, text="Верный", command=lambda: dismiss(window))
    close_button.pack(anchor="center", expand=1)
    window.grab_set()

root = Tk()
root.title("Тест")
root.geometry('220x100')

ask1 = Label(root, text="2 + 2 = 3?",
             font=('Comic San MS', 24, 'bold'),
             bg='#112233', fg='#00FF00', bd=5
             )
ask1.pack(anchor='n')
btnYes = Button(root, text="Да", command=press_yes)
btnNo = Button(root, text="Нет", command=press_no)
btnYes.place(x=25, y=60)
btnNo.place(x=125, y=60)


root.mainloop()

