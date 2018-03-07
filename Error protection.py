import turtle 

def Blankboard(t):
    horiz1 = [0,90]
    horiz2 = [0,180]
    vert1 = [90,270]
    vert2 = [180,270]
    fullhoriz = [horiz1, horiz2]
    fullvert = [vert1, vert2]
    
    for pnt in fullhoriz:
        t.penup()
        t.setpos(pnt)
        t.pendown()
        t.forward(270)
        
    t.right(90)
    
    for pnt in fullvert:
        t.penup()
        t.setpos(pnt)
        t.pendown()
        t.forward(270)

def startgame(t,n):
    Blankboard(n)
    pnt1 = [45,225]
    pnt2 = [135,225]
    pnt3 = [225,225]
    pnt4 = [45,135]
    pnt5 = [135,135]
    pnt6 = [225,135]
    pnt7 = [45,45]
    pnt8 = [135,45]
    pnt9 = [225,45]
    allpoints = [pnt1, pnt2, pnt3, pnt4, pnt5, pnt6, pnt7, pnt8, pnt9]
    count = 1
    for pnt in allpoints:
        t.penup()
        t.setpos(pnt)
        t.write(str(count))
        t.pendown
        count += 1

def draw_x(t,pnt):
    t.penup()
    t.setpos(pnt)
    t.pendown()
    t.seth(315)
    t.forward(45)
    t.forward(-90)
    t.forward(45)
    t.right(90)
    t.forward(45)
    t.forward(-90)
    
def draw_O(t,pnt):
    pnt[1] = pnt[1]-35
    t.penup()
    t.setpos(pnt)
    t.pendown()
    t.circle(35,360,360)

def player1_turn():
    pnt1 = [45,225]
    pnt2 = [135,225]
    pnt3 = [225,225]
    pnt4 = [45,135]
    pnt5 = [135,135]
    pnt6 = [225,135]
    pnt7 = [45,45]
    pnt8 = [135,45]
    pnt9 = [225,45]
    choice = input("Player 1, please type the number of your selection")
    for number in range(9):
        count = 1
        if choice == str(count):
            choice = int(choice)
        count += 1
    if type(choice) != type(1):
        print(type(choice))
        print("Please make a valid selection between 1 and 9.")
        player1_turn()
    if choice == 1:
        return pnt1
    elif choice == 2:
        return pnt2
    elif choice == 3:
        return pnt3
    elif choice == 4:
        return pnt4
    elif choice == 5:
        return pnt5
    elif choice == 6:
        return pnt6
    elif choice == 7:
        return pnt7
    elif choice == 8:
        return pnt8
    elif choice == 9:
        return pnt9
    else:
        print(type(choice))
        print("Please make a valid selection between 1 and 9.")
        player1_turn()

def player2_turn():
    pnt1 = [45,225]
    pnt2 = [135,225]
    pnt3 = [225,225]
    pnt4 = [45,135]
    pnt5 = [135,135]
    pnt6 = [225,135]
    pnt7 = [45,45]
    pnt8 = [135,45]
    pnt9 = [225,45]
    choice = int(input("Player 2, please type the number of your selection"))
    if choice == 1:
        return pnt1
    elif choice == 2:
        return pnt2
    elif choice == 3:
        return pnt3
    elif choice == 4:
        return pnt4
    elif choice == 5:
        return pnt5
    elif choice == 6:
        return pnt6
    elif choice == 7:
        return pnt7
    elif choice == 8:
        return pnt8
    elif choice == 9:
        return pnt9
    else:
        print("Please make a valid selection between 1 and 9.")
        player2_turn()
        
wn = turtle.Screen()
wn.setworldcoordinates(0, 0, 270, 270)

gameboard = turtle.Turtle()
gameboard.speed(0)

numbers = turtle.Turtle()
numbers.speed(0)

player1 = turtle.Turtle()
player1.speed(0)
player1.pensize(5)

player2 = turtle.Turtle()
player2.speed(0)
player2.pensize(5)

print (player1_turn())
wn.exitonclick()
