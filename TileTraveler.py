#Questions:
#1.The second implementation was a lot easier because you had already programmed a solution to your problem so you had all the "meat" but just had to "put it on the bones" in the second one 
#2.The second implementation is a lot more readable; a lot more stylishly set up and every step/function is explained for the avarege reader.
#3.It made the code a lot more readable and easier to debug.


#The first project without functions:
#x=1
#y=1
#while (str(x) + str(y)) != "31":
#    if x == 1 and y == 3:
#        print("You can travel: ", end='')
#        print("(E)ast","or ", end='')
#        print("(S)outh.",)
#        direction = 0
#        direction = input("Direction: ").lower()
#        while direction != "e" and direction != "s":
#            print("Not a valid direction!")
#            direction = input("Direction: ").lower()
#        else:
#            if direction == "e":
#                x=2
#                y=3
#            elif direction == "s":
#                x=1
#                y=2
#        
#    elif x == 1 and y == 2:
#        print("You can travel: ", end='')
#        print("(N)orth","or ",end='')
#        print("(E)ast","or ", end='')
#        print("(S)outh.")
#        direction = 0
#        direction = input("Direction: ").lower()
#        while direction != "e" and direction != "s" and direction != "n":
#            print("Not a valid direction!")
#            direction = input("Direction: ").lower()
#        else:
#            if direction == "e":
#                x = 2
#                y = 2
#            elif direction == "s":
#                x=1
#                y=1
#            elif direction == "n":
#                x=1
#                y=3
#    elif x== 1 and y == 1:
#        print("You can travel: ", end='')
#        print("(N)orth.",)
#        direction = 0
#        direction = input("Direction: ").lower()
#        while direction != "n":
#            print("Not a valid direction!")
#            direction = input("Direction: ").lower()
#        else:
#                x=1
#                y=2
#    elif x== 2 and y == 3:
#        print("You can travel: ", end='')
#        print("(E)ast","or ", end='')
#        print("(W)est.")
#        direction = 0
#        direction = input("Direction: ").lower()
#        while direction != "e" and direction != "w":
#            print("Not a valid direction!")
#            direction = input("Direction: ").lower()
#        else:
#            if direction == "e":
#                x=3
#                y=3
#            elif direction == "w":
#                x=1
#                y=3
#            
#    elif x == 2 and y == 2:
#        print("You can travel: ", end='')
#        print("(S)outh","or ",end='')
#        print("(W)est.",)
#        direction = 0
#        direction = input("Direction: ").lower()
#        while direction != "w" and direction != "s":
#            print("Not a valid direction!")
#            direction=input("Direction: ").lower()
#       else:
#            if direction == "w":
#                x=1
#                y=2
#            elif direction == "s":
#                x=2
#                y=1
#        
#    elif x == 2 and y == 1:
#        print("You can travel: ", end='')
#        print("(N)orth.",)
#        direction = 0
#        direction = input("Direction: ").lower()
#        while direction != "n":
#            print("Not a valid direction!")
#            direction = input("Direction: ").lower()
#        else:
#            x=2
#            y=2
#
#    elif x==3 and y==3:
#        print("You can travel: ", end='')
#        print("(S)outh","or ",end='')
#        print("(W)est.",)
#        direction = 0
#        direction = input("Direction: ").lower()
#        while direction != "w" and direction!="s":
#            print("Not a valid direction!")
#            direction = input("Direction: ").lower()
#        else:
#
#            if direction == "w":
#                x=2
#                y=3
#            elif direction == "s":
#                x=3
#                y=2
#    
#    elif x == 3 and y == 2:
#        print("You can travel: ", end='')
#        print("(N)orth","or ",end='')
#        print("(S)outh.")
#        direction = 0
#        direction = input("Direction: ").lower()
#        while direction !="n" and direction !="s":
#            print("Not a valid direction!")
#            direction = input("Direction: ").lower()
#        else:
#            if direction == "n":
#                x=3
#                y=3
#            elif direction == "s":
#                print("Victory!")
#                break


#The second project with functions:
def Move_North(x,y):
    """This function moves you from your current position to north"""
    y+=1
    return x,y
def Move_South(x,y):
    """This function moves you from your current position to south"""
    y=y-1
    return x,y
def Move_West(x,y):
    """This function moves you from your current position to west"""
    x=x-1
    return x,y
def Move_East(x,y):
    """This function moves you from your current position to east"""
    x+=1
    return x,y

def Has_Not_Won(x,y):
    """This function returns "True" if you have not won the game and "False if you have won"""
    if x == 3 and y == 1:
        return False
    else:
        return True

def Where_U_Can_Move(x,y):
    """This function checks your position and prints where you can move to next"""
    if x == 1 and y == 3:
        print("You can travel: ", end='')
        print("(E)ast","or ", end='')
        print("(S)outh.",)
    elif x == 1 and y == 2:
        print("You can travel: ", end='')
        print("(N)orth","or ",end='')
        print("(E)ast","or ", end='')
        print("(S)outh.")
    elif x== 1 and y == 1:
        print("You can travel: ", end='')
        print("(N)orth.",)
    elif x== 2 and y == 3:
        print("You can travel: ", end='')
        print("(E)ast","or ", end='')
        print("(W)est.")
    elif x == 2 and y == 2:
        print("You can travel: ", end='')
        print("(S)outh","or ",end='')
        print("(W)est.",)
    elif x == 2 and y == 1:
        print("You can travel: ", end='')
        print("(N)orth.",)
    elif x==3 and y==3:
        print("You can travel: ", end='')
        print("(S)outh","or ",end='')
        print("(W)est.",)
    elif x == 3 and y == 2:
        print("You can travel: ", end='')
        print("(N)orth","or ",end='')
        print("(S)outh.")

def To_Move(direction,x,y):
    """This function actually lets you move depending on your position and choise of direction"""
    if x == 1 and y == 3:
        while direction != "e" and direction != "s":
            print("Not a valid direction!")
            direction = input("Direction: ").lower()
        else:
            if direction == "e":
                x,y = Move_East(x,y)
                return x , y
            elif direction == "s":
                x,y = Move_South(x,y)
                return x , y
    elif x == 1 and y == 2:
        while direction != "e" and direction != "s" and direction != "n":
            print("Not a valid direction!")
            direction = input("Direction: ").lower()
        else:
            if direction == "e":
                x,y = Move_East(x,y)
                return x , y
            elif direction == "s":
                x,y = Move_South(x,y)
                return x , y
            elif direction == "n":
                x,y = Move_North(x,y)
                return x , y
    elif x== 1 and y == 1:
        while direction != "n":
            print("Not a valid direction!")
            direction = input("Direction: ").lower()
        else:
            x,y = Move_North(x,y)
            return x , y
    elif x== 2 and y == 3:
        while direction != "e" and direction != "w":
            print("Not a valid direction!")
            direction = input("Direction: ").lower()
        else:
            if direction == "e":
                x,y = Move_East(x,y)
                return x , y
            elif direction == "w":
                x,y = Move_West(x,y)
                return x , y
    elif x == 2 and y == 2:
        while direction != "w" and direction != "s":
            print("Not a valid direction!")
            direction=input("Direction: ").lower()
        else:
            if direction == "w":
                x,y = Move_West(x,y)
                return x , y
            elif direction == "s":
                x,y = Move_South(x,y)
                return x , y
    elif x == 2 and y == 1:
        while direction != "n":
            print("Not a valid direction!")
            direction = input("Direction: ").lower()
        else:
            x,y = Move_North(x,y)
            return x , y
    elif x==3 and y==3:
        while direction != "w" and direction!="s":
            print("Not a valid direction!")
            direction = input("Direction: ").lower()
        else:
            if direction == "w":
                x,y = Move_West(x,y)
                return x , y
            elif direction == "s":
                x,y = Move_South(x,y)
                return x , y
    elif x == 3 and y == 2:
        while direction !="n" and direction !="s":
            print("Not a valid direction!")
            direction = input("Direction: ").lower()
        else:
            if direction == "n":
                x,y = Move_North(x,y)
                return x , y
            elif direction == "s":
                x,y = Move_South(x,y)
                return x , y

    




x=1
y=1
while Has_Not_Won(x,y):
    Where_U_Can_Move(x,y)
    direction=input("Direction: ").lower()
    x,y = To_Move(direction,x,y)
else:
    print("Victory!")
