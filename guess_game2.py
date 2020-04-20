import random


def guess_game(level):
    if level == 'e':
        num = random.randint(1,10)
        chances = 5
    elif level == 'm':
        num = random.randint(1,20)
        chances = 3
    elif level == 'h':
        num = random.randint(1,50)
        chances = 2
    try:
        guess = int(input("Make a guess: "))
        
        if guess == num:
            print('You got it right!')
        else:
            while guess != num and chances :  #Checks the guess and if the player still has chances to try.
                print('That was wrong!')
                if guess < num:
                    print('You have',chances,'guess remaining\n')                    
                    guess = int(input('Guess is less than the actual number make another guess: '))

                elif guess > num:
                    print('You have',chances,'guess remaining\n')                    
                    guess =int(input("Your guess is greater than the actual number, make another guess: "))

                
                chances-= 1
                if guess == num:
                    print('You got it right!')
                    break
                if chances ==0:
                    print('Game over!\nThe number is', num)
    except ValueError:
        print("This version only supports guessing Numbers! Try again later.")


if __name__ == "__main__":
    str = "Welcome Please Select a Level"
    print(str.center(100,"*"))
    level = input('''
Choose Either: e, m or h.
e ===> EASY 
m ===> MEDIUM 
h ===> HARD 
>''').lower().strip()
    

    while level not in ('e','m','h'):
        level = input('Enter a valid response [e/m/h]> ')

    guess_game(level)