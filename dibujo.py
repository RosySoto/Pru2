__author__ = 'kaue'
import turtle,time
colors = ['blue', 'yellow', 'blue', 'green', 'yellow', 'orange', 'orange']
t1=turtle.Pen()
turtle.bgcolor('black')
t1.speed(0)
for x in range(1000):
    t1.pencolor(colors[x%7])
    if x%2==0:
        t1.forward(x)
    else:
        t1.backward((x-1))
    t1.left(52)
time.sleep(30)
