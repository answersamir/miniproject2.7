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

n = 5

from temporary_testing import main

"""c1 = [0, 5, 10, 15, 20]

c2 = [1, 6, 11, 16, 21]

c3 = [2, 7, 12, 17, 22]

c4 = [3, 8, 13, 18, 23]

c5 = [4, 9, 14, 19, 24]
"""

c1 = [0, 5, 10, 15, 20]

c2 = [7, 12, 17, 22, 21]

c3 = [2, 1, 6, 11, 16]

c4 = [4, 3, 8, 13, 18]

c5 = [9, 14, 19, 24, 23]

tot_array = [c1, c2, c3, c4, c5]
turns = randint(6, 16)
# now we choose any random array to work on
for i in range(0, turns):
    print i
    mainCol = randint(0, 4)
    if tot_array[mainCol].__len__() > 3:


        if mainCol == 0:
            b = [mainCol+1]
        elif mainCol == 4:
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


from game_5x5 import main

main(c1, c2, c3, c4, c5)