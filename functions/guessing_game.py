from curses import A_CHARTEXT
import random
def main():
    guess()
    
    while True:
        again = input("Enter Y to play again: ")
        if again.lower() == "y":
            guess()
        else:
            break
            

def guess():
    """
    User guess what the number is, display message 
    if the   guess is higher or lower
    """
    n = random.randint(1,100)
    counter = 0
    
    while True:
        user = int(input("Enter a number: "))
        if user > n:
            print("Too high, Try again")
            counter += 1
        elif user < n:
            print("Too low, try again")
            counter += 1
        else:
            print(f"Congratulations, you got it right after {counter} trials")
            break
            
main()

