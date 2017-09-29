#Greg Phillips
#9/29/17
#divisors.py

num = int(input("enter a number: "))

for i in range(1,num+1):
    if num%i == 0 and i != num:
        print(i)
