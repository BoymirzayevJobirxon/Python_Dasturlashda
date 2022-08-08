import tkinter as tk
win = tk.Tk()
win.title("itrobo.ru")
win.geometry("300x300")
res = tk.Label(win, text = "Привет")
res.grid(row = 1, column = 0)
win.mainloop()
