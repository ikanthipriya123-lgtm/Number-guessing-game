# Number-guessing-game
import random
import time
print("*" * 10)
print("÷" * 7)
print("Number Guessing game")
print("÷" * 7)
user_opt = int(input(" please enter one number(1-9): "))
opt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pc = random.choice(opt)
print("PC turn")
time.sleep(2)
print(pc)
if pc == user_opt:
    print("^" * 7)
    print("You are win")
    print("^" * 7)
    
else:
    print("You are lose")    
print("*" * 10)
