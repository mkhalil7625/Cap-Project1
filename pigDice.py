#
import random

def dice_roll():
    total=0
    while True:
        num1 = random.randint(1,6)
        print ("Your number is: " + str(num1))
        if num1 == 1:
            total=0
            print("your turn is over")
            print("Your total is: " + str(total))
            break
        else:
            total=total+num1
            print("Your total is: " + str(total))
            if total >= 10:
                print("you Win!!!")
                break
            elif total<10:
                play_again = input("Would you like to play again? ").lower()
                while  play_again != 'y':
                    if play_again == 'no':
                        return print("Game Over")
                    else:
                        print("Input not recognized")
                        play_again = input("Would you like to play again? ")

def main():
    # Explain the rules for the game
    print()
    print("             W E L C O M E  T O  P I G  D I C E !")
    print()
    print()
    print("The rules are simple, roll the die and pray to god that it is a")
    print("higher than one.")
    print()
    print("     If you roll a one, your score will be zero. ")
    print("     If you roll any other number, it will be added to your total.")
    print("     If you scored a total of 10, you will be the winner")
    print()
    print("                L E T ' S  B E G I N !")
    # game_start = input(
    #     "                 press ENTER to start")  # all "wait" variables, are just there to wait for the player to input something



    game_start = input("Would you like to roll the dice? Y/N").lower()
    if game_start == 'yes' or game_start == 'y':
        dice_roll()
    elif game_start =='no' or game_start == 'n':
        print('too bad')
    else:
        print("Input not recognized")

if __name__ == '__main__':
    main()
