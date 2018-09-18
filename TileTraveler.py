x=1
y=1
while (str(x) + str(y)) != "31":
    if x == 1 and y == 3:
        print("You can travel: ", end='')
        print("(E)ast ", end='')
        print("(S)outh ",)
        direction = input("Direction: ")
        if direction == "E":
            x=2
            y=3
        elif direction == "S":
            x=1
            y=2
        else:
            print("Not a valid direction!")
    elif x == 1 and y == 2:
        print("You can travel: ", end='')
        print("(E)ast ", end='')
        print("(S)outh ",end='')
        print("(N)orth ",)
        direction = input("Direction: ")
        if direction == "E":
            x = 2
            y = 2
        elif direction == "S":
            x=1
            y=1
        elif direction == "N":
            x=1
            y=3
        else:
            print("Not a valid direction!")
    elif x== 1 and y == 1:
        print("You can travel: ", end='')
        print("(N)orth ",)
        direction = input("Direction: ")
        if direction == "N":
            x=1
            y=2
        else:
            print("Not a valid direction!")
    elif x== 2 and y == 3:
        print("You can travel: ", end='')
        print("(E)ast ", end='')
        print("(W)est ",)
        direction = input("Direction: ")
        if direction == "E":
            x=3
            y=3
        elif direction == "W":
            x=1
            y=3
        else:
            print("Not a valid direction!")
    elif x == 2 and y == 2:
        print("You can travel: ", end='')
        print("(W)est ",end='')
        print("(S)outh ",)
        direction = input("Direction: ")
        if direction == "W":
            x=1
            y=2
        elif direction == "S":
            x=2
            y=1
        else:
            print("Not a valid direction!")
    elif x == 2 and y == 1:
        print("You can travel: ", end='')
        print("(N)orth ",)
        direction = input("Direction: ")
        if direction == "N":
            x=2
            y=2
        else:
            print("Not a valid direction!")
    elif x==3 and y==3:
        print("You can travel: ", end='')
        print("(W)est ",end='')
        print("(S)outh ",)
        direction = input("Direction: ")
        if direction == "W":
            x=2
            y=3
        elif direction == "S":
            x=3
            y=2
        else:
            print("Not a valid direction!")
    elif x == 3 and y == 2:
        print("You can travel: ", end='')
        print("(N)orth ",end='')
        print("(S)outh ",)
        direction = input("Direction: ")
        if direction == "N":
            x=3
            y=3
        elif direction == "S":
            break
        else:
            print("Not a valid direction!")
    