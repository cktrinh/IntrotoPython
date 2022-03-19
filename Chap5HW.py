# cafeCompetition

# plays the game (main interaction)

# * input: nothing
# * output: nothing

# How?
# * get user choice --> variable userChoice (boolean that is T if chose $1)
# * generate comp choice --> variable compChoice (boolean that is T if chose $1)
# * give as inputs userChoice and compChoice to resolveOutcome


# getUserChoice

# ask the user what price to set the cookies at and return True if they lower to $1

# * input: nothing
# * output: boolean (T if $1)

# How?
# * ask the user for a price --> variable userPriceStr
# * test if was "$1" --> return T


# generateCompChoice

# randomly choose for the competition (computer)

# * input: nothing
# * output: boolean (T if $1)

# How?
# * randomly generate a 0 or 1
# * if 0 --> return True (otherwise False)


# resolveOutcome

# print one of 4 scenarios that could result from the choices

# * input:
#     choice 1 (boolean T if $1)
#     choice 2 (boolean T if $1)

# * output:
#     nothing

# How?
# * test if choice 1 is True
#     * test if choice 2 is True --> print outcome 1
#     * otherwise --> print outcome 2
# * otherwise
#     * test if choice 2 is True --> print outcome 3
#     * otherwise --> print outcome 4