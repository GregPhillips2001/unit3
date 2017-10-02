#Greg Phillips
#10/2/17
#changeComputerLoop.py 

change = int(input("Enter the number of change you need: "))
quarter = 25
dime = 10
nickel = 5
penny = 1

for i in range(1,change+1):
    if i-quarter < 0:
        print("0 quarters")
        if i-dime < 0:
            print
    
