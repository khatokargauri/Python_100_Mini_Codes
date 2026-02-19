print('''                                                    .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ''')
print("Welcome to Treasure Island!\nYour mission is to find the treasure.")
cross_road = input("You're at a cross road. Where do you want to go?\n   Type 'left' or 'right'\n ")
if cross_road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    from_lake = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if from_lake == "swim":
        print("Crocodile ate you!Game Over!!!")
    else:
        print("The boat took you to an island where there were 3 houses whose doors were of different colours. Which door do you choose?")
        door = input("'Red','Yellow','Blue'?")
        if door == "Red" or  door == "Blue":
            print("The door opened on the opposite side! You got banged! Game Over!!!")
        else:
            print("You found a trunk full of gold!!!You win!!!!")
else:
    print("You fell into a hole. Game Over!!")
