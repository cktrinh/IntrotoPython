import random
### READ WORDS FUNCTION ###
def readWords( inputFile ):
    """Given the path to an input file (string) that contains one word
    per line, return a list containing those words, with all the words
    converted to lower case. """
    allWords = []
    with open(inputFile,'r') as reader:
        for line in reader:
            lineContent = line.strip()
            lineContent = lineContent.lower()
            allWords.append(lineContent)
        return allWords

initial = ['-----', '-----', '-----']
allWords = readWords('scrabble5.txt')
print(allWords)

### FIND HIDDEN WORD FUNCTION ###
def findHiddenWord():
    allWords = readWords('scrabble5.txt')
    randomWord = random.randint(0, len(allWords)-1)
    hiddenWord = allWords[randomWord]
    print(f'Hidden word is:{hiddenWord}')
    return hiddenWord

### FIND USER CHOICE ###
def findUserChoice():
    userWord = input('Your guess:')
    userWord = str(userWord)
    userWord = userWord.lower()
    return userWord

### DISPLAY INITIAL SANDWICH ###
def displaySandwich (sandwich) :
    ''' 
    Displays the sandwich.  
    The sandwich is represented as a list of 3 strings. The first entry in the list is the top piece of bread, 
    the second is what should display for the filling, and the third is the bottom piece of bread.'''
    print(sandwich)
    return sandwich

### UPDATE BREAD FUNCTION ###
def updateBread(hiddenWord, userWord, sandwich):
    isInTheList = False
    while isInTheList == False:
        
        
        if userWord.lower() == 'q':
            return True
        elif(userWord not in allWords):
            print('This word is not in the list. Try again')
            return True
        else: 
            isInTheList = True
    userWordIndex = allWords.index(userWord)
    hiddenWordIndex = allWords.index(hiddenWord)

    if userWordIndex < hiddenWordIndex:
        sandwich[0] = userWord
        print(sandwich)
        return True
    elif userWordIndex > hiddenWordIndex:
        sandwich[2] = userWord
        print(sandwich)
        return True
    else:
        sandwich[1] = userWord
        print(sandwich)
        return False
        
hiddenWord = str(findHiddenWord())
displayedSandwich = displaySandwich(initial)

### PLAY GAME FUNCTION ###
def playGame(hiddenWord, validWordList):
    isInTheList = False
    while isInTheList == False:
        
        userWord = str(findUserChoice())
        if userWord.lower() == 'q':
            return False
        elif(userWord not in validWordList):
            print('This word is not in the list. Try again')
        else: 
            isInTheList = True

    isContinued = updateBread(hiddenWord,userWord, displayedSandwich)
    while isContinued == True:
        anotherUserWord = str(findUserChoice())
        if(anotherUserWord.lower() == 'q'):
            isContinued = False
            return False
        else:
            isContinued = updateBread(hiddenWord,anotherUserWord,displayedSandwich)
    return True

if(playGame(hiddenWord, allWords)):
    print('You win!')
else:
    print('The hidden word is', hiddenWord)
    print('You lose!')

### TESTREADWORDS FUNCTION ###
def testReadWords():
    test0 = "scrabble5.txt"
    readWords(test0)
    test1 = "common5.txt"
    readWords(test1)
testReadWords()

### TESTUPDATEDBREAD FUNCTION ###
def testUpdateBread():
    test1="aahed"
    updateBread(hiddenWord,test1,displayedSandwich)
    test2= "abamp"
    updateBread(hiddenWord,test2,displayedSandwich)
    test3= "aali"
    updateBread(hiddenWord,test3,displayedSandwich)

testUpdateBread()

### TESTDISPLAYSANDWICH FUNCTION ### 
def testDisplaySandwich():
    sandwich1 = displaySandwich(initial)
    expectedResult = ["-----", "-----", "-----"]
    print("Expected: {}".format(expectedResult), "Actual: {}".format(sandwich1))
testDisplaySandwich()

### TESTPLAYGAME FUNCTION ### 
def testPlayGame():
    test0 = ["aaa","bbb","ccc",hiddenWord]
    playGame(hiddenWord,test0)
testPlayGame()