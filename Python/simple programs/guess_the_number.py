#Guesses useers number
import random

valid = False
lst = [i for i in range(1,51)]



guess_right = False
while not valid:
    try:
        num = int(input("Enter a number for me to guess: (between 1 and 50) "))
        if num < 51 and num > 0:
            valid = True
        else:
            valid = False
    except:
        valid = False
print("I have 10 guesses to get to your number")

for i in range(10):
    print(lst)
    num_guess = random.randint(lst[0],lst[-1])
    ask = input(f"Is your number {num_guess}(y), higher(h) or lower (l) ")
    if ask == 'y':
        print("Yay! I go it right")
        break
    elif ask == 'h':
        index = lst.index(num_guess)
        del lst[:index+1]
    elif ask == 'l':
        index = lst.index(num_guess)
        del lst[index:]
    else:
        print("Um... What? Well you just lost a guess I suppose")

        
