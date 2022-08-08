import tkinter as tk
win = tk.Tk()
win.title("itrobo.ru")
win.geometry("300x300")
res = tk.Label(win, text = "-")
res.grid(row = 23, column = 10)
def onclick():
    res.configure(text = "меня нажали")
button = tk.Button(win, text = "нажми меня", command = onclick)
button.grid(row = 1, column = 1)
win.mainloop()
