import turtle, random,time
colors = ('red', 'green', 'yellow', 'gold','orange')
window = turtle.Screen()
while True:
    window.bgcolor(random.choice(colors))
    time.sleep(1)
window.mainloop()
