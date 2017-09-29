#Greg Phillips
#9/29/17
#perfectNumber.py 

num = int(input("enter a number: "))
total = 0
for i in range(1,num):
    total += i
if num%i == 0 and total == num:
    print("Perfect")
else:
    print("Not Perfect")

