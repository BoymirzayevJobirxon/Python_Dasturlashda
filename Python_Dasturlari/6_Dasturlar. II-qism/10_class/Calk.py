import tkinter as tk
win = tk.Tk()
win.title("itrobo.ru")
win.geometry("400x400")
num1 = tk.Entry(win)
num1.grid(row = 0, column = 0)
num2 = tk.Entry(win)
num2.grid(row = 2, column = 0)
res = tk.Label(win, text = "-")
res.grid(row = 4, column = 0)
def summation():
    one = float(num1.get())
    two = float(num2.get())
    result = one + two
    res.configure(text = "= %s" % result)
button = tk.Button(win, text = "Сумма", command = summation)
button.grid(row = 1, column = 1)
win.mainloop()
