from random import randint

storlek = int(input("Hur stor julgran? "))
spaces = storlek + 1
bredd = 1


for i in range(storlek):
    if i != 0:
        print("\033[0;32;40m " * spaces, end="")
        for i in range(bredd):
            x = randint(0,10)
            if x > 1:
                print("\033[0;32;40m*", end="")
            else:
                print("\033[0;31;40m0", end="")
        print()
    else:
        print("\033[0;32;40m " * (spaces - 1), "\033[0;33;40m0")
    spaces -= 1
    bredd += 2

for i in range(3):
    print(" "* (storlek), end="")
    print("\033[0;33;40m***")