#Greg Phillips
#9/27/17
#hitchhiker.py - asks question and answers 42 or quits

for i in range(1,100):
    question = input("Enter a question or type quit: ")
    if "quit" not in question:
        print("42")
        
