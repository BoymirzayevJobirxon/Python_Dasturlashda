import turtle as tu
t = tu.Turtle() 
t.screen.bgcolor('red') 
t.left(90)      
t.speed(20)      
t.color('green')  
t.pensize(5)      
t.screen.title("My Fractal Tree") 
 

def draw_fractal(blen):
    if(blen<10):  
        return
    else:
        t.forward(blen)
        t.left(30)
        draw_fractal(3*blen/4)
        t.right(60)
        draw_fractal(3*blen/4)
        t.left(30)
        t.backward(blen)
 
draw_fractal(80) 
t = tu.done()
