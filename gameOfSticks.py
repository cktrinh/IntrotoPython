def gameOfSticks():
# Input: Number of sticks in pile
    numSticks = input("Choose total number of sticks [10-20]")
    numSticks = int(numSticks)
# In the Loop:
    while numSticks >1:
# Player one chooses 1-3 sticks
# Player one choice (in the loop)
        player1Choice = input ("Player 1, How many sticks are you picking up? 1, 2 or 3?")
        player1Choice = int(player1Choice)
# Check whether they pick a number between 1 and 3
        if player1Choice > 3 or player1Choice < 1:
            player1Choice = int(input ("Player 1, Please re-input number from 1, 2 or 3:"))
            if player1Choice == 1 or player1Choice ==2 or player1Choice ==3:
                numSticks = numSticks - player1Choice
                print(f"Number of sticks left:", numSticks)
        else:
# Subtract player one input from total sticks in pile and save to variable 
            numSticks = numSticks - player1Choice
            print(f"Number of sticks left:", numSticks)
            if numSticks < 1:
                finalMessage = "Player 2 wins, player 1 loses"                
                return finalMessage
            else:
            # Player two chooses 1-3 sticks
            # Player two choice (in the loop)                
                player2Choice = input ("Player 2, How many sticks are you picking up? 1, 2 or 3?")
                player2Choice = int(player2Choice)
                    # Check if they pick a number between 1 and 3
                if player2Choice > 3 or player2Choice < 1:
                    player2Choice = int(input ("Player 2, Please re-input number from 1, 2 or 3:"))
                    if player2Choice == 1 or player2Choice ==2 or player2Choice ==3:
                        numSticks = numSticks - player2Choice
                        print(f"Number of sticks left:", numSticks)
                else:
                # Subtract player two input from total sticks in pile and save to variable 
                    numSticks = numSticks - player2Choice
                    print(f"Number of sticks left:", numSticks)
                    if numSticks < 1:
                        finalMessage = "Player 1 wins, player 2 loses"                            
                        return finalMessage
    return finalMessage

gameOfSticks()