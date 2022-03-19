def sumToSingleDigit( n ):
    runningTotal = 0
    digitsRemaining = n 
    while digitsRemaining > 0:
        currentDigit = digitsRemaining % 10 
        runningTotal = runningTotal + currentDigit 
        digitsRemaining = digitsRemaining // 10
        while runningTotal >9:
            sumToSingleDigit(runningTotal)
    return runningTotal

print( sumToSingleDigit( 691) )
print( sumToSingleDigit( 152342 ) )


    