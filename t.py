import turtle
my=turtle.Turtle()
def square():
    
    my.forward(100)
    my.left(90)
    my.forward(100)
    my.left(90)
    my.forward(100)
    my.left(90)
    my.forward(100)


    
    
    
def cube():
    
    square()
    my.right(45)
    square()
    square()
    
for i in range(10):
    cube()
    cube()
    my.forward(50)
    cube()
    cube()
    cube()
    my.left(90)
    my.forward(135)
    my.right(90)
    my.forward(40)
    my.right(90)
    my.forward(35)






