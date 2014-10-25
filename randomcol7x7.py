__author__ = 'samirpatil'

from random import *
"""
We create arrays of different colours for our level and then pass it to the main function
    (here we have overloaded main function with 5 or 7 or 8 arguments)
    colours have there specific order as follows
    c1 = Red
    c2 = Green
    c3 = Blue
    c4 = Purple
    c5 = Orange
    c6 = Turquois
    c7 = Light Yellow
    c8 = Gold
"""

""" now  we are trying to randomize levels
    creating random levels form the predefined level"""

n = 7

from temporary_testing import main

c1 = [0, 7, 14, 21, 28, 35, 42]

c2 = [1, 8, 15, 22, 29, 36, 43]

c3 = [2, 9, 16, 23, 30, 37, 44]

c4 = [3, 10, 17, 24, 31, 38, 45]

c5 = [4, 11, 18, 25, 32, 39, 46]

c6 = [5, 12, 19, 26, 33, 40, 47]

c7 = [6, 13, 20, 27, 34, 41, 48]




tot_array = [c1, c2, c3, c4, c5, c6, c7]
turns = randint(20, 34)
# now we choose any random array to work on
for i in range(0, 6):
    print i
    mainCol = randint(0, 6)
    if tot_array[mainCol].__len__() > 3:


        if mainCol == 0:
            b = [mainCol+1]
        elif mainCol == 6:
            b = [mainCol-1]
        else:
            b = [mainCol-1, mainCol+1]

        sideCol = choice(b)


        d = [True, False]
        first_Notlast = choice(d)

        if first_Notlast:
            switchBit = tot_array[mainCol][0]
            checkbit = tot_array[sideCol][0]
            if switchBit == checkbit + 1 or switchBit == checkbit - 1 or switchBit == checkbit + n or switchBit == checkbit - n:
                tot_array[mainCol].remove(switchBit)
                tot_array[sideCol].insert(0, switchBit)
        else:
            switchBit = tot_array[mainCol][tot_array[mainCol].__len__() - 1]
            checkbit = tot_array[sideCol][tot_array[sideCol].__len__() - 1]
            if switchBit == checkbit + 1 or switchBit == checkbit - 1 or switchBit == checkbit + n or switchBit == checkbit - n:

                tot_array[mainCol].remove(switchBit)
                tot_array[sideCol].append(switchBit)
    print c1
    print c2
    print c3
    print c4
    print c5
    print c6
    print c7


from game_7x7 import main

main(c1, c2, c3, c4, c5, c6, c7)