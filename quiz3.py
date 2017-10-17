#greg phillips
#10/17/17
#quiz3.py

for i in range(-5,6):
    print(i)

i = 18
while i<33:
    print(i)
    i+=2
    
total = 0
for i in range(13,332,2):
    total+=i
print(total)

while True:
    word = input("Enter a word: ")
    if "z" or "Z" in word:
        break