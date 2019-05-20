import random
a = 4
def diceroll(a):
    print("          rolling dice ......")
    print("                  rolling......")
    y = int(random.randint(1,10))
    if y==a:
        print(" CONGRAT'S YOU WON ")
    else:
        print("IT SEEMS YOU AREN'T LUCCKY THIS TIME "
              "BETTER LUCK NEXT TIME")
    print("The number is ",y)
x=int(1)
while x==1:
    a = int(input("WANT TO TRY YOUR LUCK"
                  " ENTER ANY NNUMBER BETWEEN 1 AND 10 LET'S CHECK "))

    diceroll(a)
    print("WANT TO TRY  again ...."
          "Enter 1 or the program will terminate")
    x = int(input())