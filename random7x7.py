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

c1 = [22, 21, 14, 7, 0, 1, 2, 3, 4, 5, 12, 19, 26]

c2 = [8, 9, 10, 11, 18]

c3 = [15, 16, 17, 24, 25]

c4 = [29, 28, 35, 42, 43, 44]

c5 = [6, 13, 20, 27, 34, 33]

c6 = [23, 30, 31, 32, 39, 40]

c7 = [36, 37, 38, 45, 46, 47, 48, 41]



tot_array = [c1, c2, c3, c4, c5, c6, c7]
turns = randint(6, 16)

changed = False
# now we choose any random array to work on


def changer()

for i in range(0, turns):

    mainCol = randint(0, 6)
    if tot_array[mainCol].__len__() > 3:




        d = [True, False]
        first_Notlast = choice(d)

        if first_Notlast:
            switchBit = int(tot_array[mainCol][0])
            switch = tot_array[mainCol][0]
            tot_array[mainCol].remove(switch)
            if not changed:
                end = c1.__len__() - 1
                if c1[0] == switchBit + 1 or c1[0] == switchBit - 1 or c1[0] == switchBit + n or c1[0] == switchBit - n:
                    c1.insert(0, switch)
                    changed = True

                elif c1[end] == switchBit + 1 or c1[end] == switchBit - 1 or c1[end] == switchBit + n or c1[end] == switchBit - n:
                    c1.append(switch)
                    changed = True


            if not changed:
                end = c2.__len__() - 1
                if c2[0] == switchBit + 1 or c2[0] == switchBit - 1 or c2[0] == switchBit + n or c2[0] == switchBit - n:
                    c2.insert(0, switch)
                    changed = True

                elif c2[end] == switchBit + 1 or c2[end] == switchBit - 1 or c2[end] == switchBit + n or c2[end] == switchBit - n:
                    c2.append(switch)
                    changed = True
            if not changed:
                end = c3.__len__() - 1
                if c3[0] == switchBit + 1 or c3[0] == switchBit - 1 or c3[0] == switchBit + n or c3[0] == switchBit - n:
                    c3.insert(0, switch)
                    changed = True

                elif c3[end] == switchBit + 1 or c3[end] == switchBit - 1 or c3[end] == switchBit + n or c3[end] == switchBit - n:
                    c3.append(switch)
                    changed = True
            if not changed:
                end = c4.__len__() - 1
                if c4[0] == switchBit + 1 or c4[0] == switchBit - 1 or c4[0] == switchBit + n or c4[0] == switchBit - n:
                    c4.insert(0, switch)
                    changed = True

                elif c4[end] == switchBit + 1 or c4[end] == switchBit - 1 or c4[end] == switchBit + n or c4[end] == switchBit - n:
                    c4.append(switch)
                    changed = True
            if not changed:
                end = c5.__len__() - 1
                if c5[0] == switchBit + 1 or c5[0] == switchBit - 1 or c5[0] == switchBit + n or c5[0] == switchBit - n:
                    c5.insert(0, switch)
                    changed = True

                elif c5[end] == switchBit + 1 or c5[end] == switchBit - 1 or c5[end] == switchBit + n or c5[end] == switchBit - n:
                    c5.append(switch)
                    changed = True
            if not changed:
                end = c6.__len__() - 1
                if c6[0] == switchBit + 1 or c6[0] == switchBit - 1 or c6[0] == switchBit + n or c6[0] == switchBit - n:
                    c6.insert(0, switch)
                    changed = True

                elif c6[end] == switchBit + 1 or c6[end] == switchBit - 1 or c6[end] == switchBit + n or c6[end] == switchBit - n:
                    c6.append(switch)
                    changed = True
            if not changed:
                end = c7.__len__() - 1
                if c7[0] == switchBit + 1 or c7[0] == switchBit - 1 or c7[0] == switchBit + n or c7[0] == switchBit - n:
                    c7.insert(0, switch)
                    changed = True

                elif c7[end] == switchBit + 1 or c7[end] == switchBit - 1 or c7[end] == switchBit + n or c7[end] == switchBit - n:
                    c7.append(switch)
                    changed = True



        else:
            switchBit = int(tot_array[mainCol][tot_array[mainCol].__len__() - 1])
            switch = tot_array[mainCol][tot_array[mainCol].__len__() - 1]
            tot_array[mainCol].remove(switch)
            if not changed:
                end = c1.__len__() - 1
                if c1[0] == switchBit + 1 or c1[0] == switchBit - 1 or c1[0] == switchBit + n or c1[0] == switchBit - n:
                    c1.insert(0, switch)
                    changed = True

                elif c1[end] == switchBit + 1 or c1[end] == switchBit - 1 or c1[end] == switchBit + n or c1[end] == switchBit - n:
                    c1.append(switch)
                    changed = True


            if not changed:
                end = c2.__len__() - 1
                if c2[0] == switchBit + 1 or c2[0] == switchBit - 1 or c2[0] == switchBit + n or c2[0] == switchBit - n:
                    c2.insert(0, switch)
                    changed = True

                elif c2[end] == switchBit + 1 or c2[end] == switchBit - 1 or c2[end] == switchBit + n or c2[end] == switchBit - n:
                    c2.append(switch)
                    changed = True
            if not changed:
                end = c3.__len__() - 1
                if c3[0] == switchBit + 1 or c3[0] == switchBit - 1 or c3[0] == switchBit + n or c3[0] == switchBit - n:
                    c3.insert(0, switch)
                    changed = True

                elif c3[end] == switchBit + 1 or c3[end] == switchBit - 1 or c3[end] == switchBit + n or c3[end] == switchBit - n:
                    c3.append(switch)
                    changed = True
            if not changed:
                end = c4.__len__() - 1
                if c4[0] == switchBit + 1 or c4[0] == switchBit - 1 or c4[0] == switchBit + n or c4[0] == switchBit - n:
                    c4.insert(0, switch)
                    changed = True

                elif c4[end] == switchBit + 1 or c4[end] == switchBit - 1 or c4[end] == switchBit + n or c4[end] == switchBit - n:
                    c4.append(switch)
                    changed = True
            if not changed:
                end = c5.__len__() - 1
                if c5[0] == switchBit + 1 or c5[0] == switchBit - 1 or c5[0] == switchBit + n or c5[0] == switchBit - n:
                    c5.insert(0, switch)
                    changed = True

                elif c5[end] == switchBit + 1 or c5[end] == switchBit - 1 or c5[end] == switchBit + n or c5[end] == switchBit - n:
                    c5.append(switch)
                    changed = True
            if not changed:
                end = c6.__len__() - 1
                if c6[0] == switchBit + 1 or c6[0] == switchBit - 1 or c6[0] == switchBit + n or c6[0] == switchBit - n:
                    c6.insert(0, switch)
                    changed = True

                elif c6[end] == switchBit + 1 or c6[end] == switchBit - 1 or c6[end] == switchBit + n or c6[end] == switchBit - n:
                    c6.append(switch)
                    changed = True
            if not changed:
                end = c7.__len__() - 1
                if c7[0] == switchBit + 1 or c7[0] == switchBit - 1 or c7[0] == switchBit + n or c7[0] == switchBit - n:
                    c7.insert(0, switch)
                    changed = True

                elif c7[end] == switchBit + 1 or c7[end] == switchBit - 1 or c7[end] == switchBit + n or c7[end] == switchBit - n:
                    c7.append(switch)
                    changed = True



            """checkbit = tot_array[sideCol][tot_array[sideCol].__len__() - 1]
            if switchBit == checkbit + 1 or switchBit == checkbit - 1 or switchBit == checkbit + n or switchBit == checkbit - n:

                tot_array[mainCol].remove(switchBit)
                tot_array[sideCol].append(switchBit)"""
    changed = False




from game_7x7 import main

main(c1, c2, c3, c4, c5, c6, c7)