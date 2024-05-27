import random
import inquirer
from pyfiglet import Figlet

#this is the theme dict used to store the info of the theme we are using
themeDict = {
    "Question": {
        "mark_color": "green",
        "brackets_color": "normal",
    },

    "List": {
        "selection_color": "orange",
        "selection_cursor": "->"
    }
}

#this function checks if attempts_list is empty or not, if not, if gives the 
#best score as the lowest no. of tries it took for the player to guess the number
#the best score one can get is that of 1 attempt clear
def show_Score(attempts_list):
    if not attempts_list:
        print('There is currently no best score, it\'s yours for the taking!')
        
    elif min(attempts_list) == 1:
        print("\n   You have reached the highest score of completing the game in 1 attempt, please continue your fight!")

    else:
        print("\n   The current best score is"f" {min(attempts_list)} attempts")

#the welcome message
def welcome():
    welcome = Figlet(font="mini")
    print(welcome.renderText("Hello traveler! Welcome to the game of guesses!"))

#message to display when user refuses to play
def reject_message():
    sayonara = Figlet(font="digital")
    print (sayonara.renderText("Thank you"))
    
#game starts with this function
def start_game():
    attempts = 0
    rand_num = random.randint(1,10)
    attempts_list, answers = [], {}

    welcome()           #greeting

    #information list, the data will be collected in a dict called "answers"
    question = [
        inquirer.Text(
                "name",
                message="What is your name",
                default="Uncrowned"
            ),

        inquirer.List(
                "choice",
                message="Welcome {name}, would you like to play",
                choices=["yes","no"]
            ),
    ]

    answers = inquirer.prompt(question, theme=inquirer.themes.load_theme_from_dict(themeDict))

    if answers["choice"] != 'yes':
        reject_message()
        exit()

    else:
        show_Score(attempts_list)       #this will show the score of nothing, and prompt the player to start

    while answers["choice"] == 'yes':
        try:
            guess = int(input("\nPick a number between 1 and 10: "))
            
            if guess < 1 or guess > 10:
                raise ValueError('Please guess a number within the given range')
                
            attempts += 1

            if guess == rand_num:
                attempts_list.append(attempts)

                print("\nNice! You got it!")
                print(f'\nIt took you {attempts} attempts\n')

                #this variable will ask the question to restart the game
                restart = [inquirer.Confirm("restart", message="Would you like to restart", default=None)]

                #the answers dict is being updated, all the questions and answers
                #will be stored in the answers dictionary
                answers.update(inquirer.prompt(restart))

                if answers["restart"] != True:          #print reject message if the player says no to restart
                    reject_message()

                    break

                else:                                   #the game restarts here
                    print("\nHave a good game!")
                    attempts = 0
                    rand_num = random.randint(1,10)
                    show_Score(attempts_list)

                    continue

            else:
                if guess > rand_num:                #print higher if the input number is higher 
                    print("\n     It\'s higher")    #than the random number

                elif guess < rand_num:              #print lower if the input number is lower
                    print('\n     It\'s lower')     #than the random number

        except ValueError as err:                   #show value error if the input is not valid
            print('\nThat is not a valid value. Try again...')
            print(err)

if __name__ == '__main__':
    start_game()

