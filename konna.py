import turtle
 
#aken
aken = turtle.Screen()
aken.setup(700,700)
 
#kujund kaheksanurk
t = turtle.Turtle()
for x in range(0,8):
    t.forward(50)
    t.left(45)


 #kujundi lehed
for x in range(0,8):   
    t.right(90) 
    t.forward(180)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(180)
    t.right(45)
    
turtle.exitonclick()