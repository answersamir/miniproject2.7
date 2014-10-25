__author__ = 'samirpatil'

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

from game_5x5 import main

c1 = [0, 5, 10, 15, 20]

c2 = [7, 12, 17, 22, 21]

c3 = [2, 1, 6, 11, 16]

c4 = [4, 3, 8, 13, 18]

c5 = [9, 14, 19, 24, 23]

main(c1, c2, c3, c4, c5)
