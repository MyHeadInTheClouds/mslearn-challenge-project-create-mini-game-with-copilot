import random

#main function for the python app
def main():
    
    #array of user options for rock, paper, scissors
    game_options = ["rock", "paper", "scissors"]
    wins = 0
    losses = 0

    #loop until user quits
    while True:

        #get user guess
        user_input = input("Enter a guess (or 'q' to quit): ")
        if user_input not in game_options and user_input != 'q':
            print("Invalid input. Try again.")
            continue

        elif user_input == 'q':
                print("Goodbye!")
                break

        else:
            #get computer guess
            computer_guess = random.choice(game_options)
            print("Computer guess: " + computer_guess)

            #determine winner
            if user_input == computer_guess:
                print("You tied!")
            elif user_input == "rock" and computer_guess == "scissors":
                print("You win!")
                wins += 1
            elif user_input == "paper" and computer_guess == "rock":
                print("You win!")
                wins += 1
            elif user_input == "scissors" and computer_guess == "paper":
                print("You win!")
                wins += 1
            else:
                print("You lose!")
                losses += 1

            #print win/loss record
            print("Wins: " + str(wins))
            print("Losses: " + str(losses))
             

if __name__ == "__main__":
    main()

