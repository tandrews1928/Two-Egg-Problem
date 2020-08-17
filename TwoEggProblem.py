from random import randrange

egg1 = True
egg2 = True
tries = 0
floor = randrange(100)
print("The random floor is ", floor)
while egg1:
    for i in range(10, 101, 10): #check every 10 floors
        tries = tries + 1
        if (i == floor): #found the floor
            print("the floor found is ", floor)
        if (i > floor): #broken egg
            egg1 = False
            break
t = i - 10
while egg2:
    for j in range(t, i, 1):   #check each floor between i - 10 and i
        tries = tries + 1     
        if (j == floor): #found the floor
            print("the floor found is ", floor)
        if (j > floor): #broken egg
            egg2 = False
            break
