""" Odds & Evens game. Written by Pod 4 (Angelina Wei, Trinh Che) in April 2021.
The game operates the Odd & Evens game between player and computer.
Both player and computer declares if they will be either “odds” or “evens”.
Then both player and computer extend one or more fingers.
If the combined number of fingers is equal to an odd number - the player declaring “odds” wins.
If the combined number is equal to an even number - “evens” wins. """

import random

def OddsandEvens():a
    """play the game (main interaction) and choose "odd" or "even" """
    intro = input("Welcome to Odds and Evens game!You'll play this game with the computer!\n"\
            +"So would you like to choose odds or evens? (And the computer will be the other side.) [odds/evens]")
    #return intro

    playerChoseEvens = True
    if intro == "odds":
        playerChoseEvens = False

    evensWins = addNumber()

    # determine if the player won
    resolveOutcome( playerChoseEvens, evensWins )

def resolveOutcome( playerChoseEvens, totalIsEven ) :
    """ Input: boolean for if player chose evens (True if they did) and
               total number (True if total is even) 
        Output: none
        Will print the outcome of the game """
    if playerChoseEvens:
        # * test if totalIsEven is True --> print outcome 1
        if totalIsEven:
            print( "The outcome is even! You win!:)" )
        #  * otherwise --> print outcome 2
        else:
            print( "The outcome is odd! You lose :(")
    # otherwise
    else:
        #   * test if totalIsEven is True --> print outcome 3
        if totalIsEven:
            print( "The outcome is even! You lose :(")
        #     * otherwise --> print outcome 4
        else:
            print( "The outcome is odd! You win!:)")

def addNumber():
    """ prompts user for a number and generates random for computer. returns True if evens wins and False otherwise."""
    firstPlayerChoice = getPlayerChoice()
    print("Your number is",firstPlayerChoice)
    secondPlayerChoice = generateCompChoice()
    print("The number of computer is", secondPlayerChoice)
    addNum = firstPlayerChoice + secondPlayerChoice
    print("The sum of two number is",addNum)
    #if added Number = even ---> “evens” wins.
    if (addNum % 2) == 0:
        return True
    #if added Number = odd ---> “odds” wins.
    else:
        return False


def getPlayerChoice():
    """enter "firstPlayerNum", 0 <= firstPlayerNum <= 5"""
    PlayerNum = int(input("How many fingers would you like to extend? [from 0-5 fingers]"))
    return PlayerNum

def generateCompChoice():
    """
    randomly choose for the competition (computer)
    enter "secondPlayerNum", 0 <= secondPlayerNum <= 5
    """
    computerNum = random.randint(0,5)
    return computerNum

OddsandEvens()
#addNumber()