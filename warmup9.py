#Greg Phillips
#10/4/17
#warmup9.py - print vowels as capital letters

word = input("Enter a word: ")

for ch in word:
    if ch == "a" or ch == "e" or ch == "u" or ch == "i" or ch == "o" or ch == "y":
        print(ch.upper())
    else:
        print(ch)
