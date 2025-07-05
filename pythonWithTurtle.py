import turtle as t

t.width(5)
    
t.color("#ff0000")


# for _ in range(4):
#     t.forward(1)
#     t.left(90)
    
# t.penup()

    
# t.goto(-80, 150)
# t.color('green')
    
# message = "Welcome to Python and Turtle!"
    
# t.write(message, font=("Arial", 20, "normal"))
    
# print(message)  
    
print(t.pos())
print("y position: ", t.ycor())
print("x position: ", t.xcor())

# def drawTriangle(length):
#     for _ in range(3):
#         t.forward(length)
#         t.left(120)

# def drawSquare(length):
#     for _ in range(4):
#         t.forward(length)
#         t.left(90)

# def drawHouse(length):
#     drawSquare(length)
#     t.left(90)
#     t.forward(length)
#     t.left(90)
#     drawTriangle(length)

# def drawSoi(space, length):
#     for _ in range(space):
#         drawHouse(length)
#         t.forward(length)

# def drawPhase(space, length):
#     for _ in range(space):
#         drawSoi(space, length)
#         t.forward(length)


# def darwVillage(length):
#     for _ in range(3):
#         drawPhase(3, length)
#         t.forward(length) 


t.done()