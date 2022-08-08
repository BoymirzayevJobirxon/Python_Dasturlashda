from tkinter import *
def onclick():
    pass

root = Tk()
text = Text(root)
text.insert(INSERT, "Here, I start the text ...") 
text.insert(END, "... and here, I finish it.")
text.pack()
text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")
root.mainloop()
