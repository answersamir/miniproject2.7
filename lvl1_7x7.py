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

from game_7x7 import main

c1 = [22, 21, 14, 7, 0, 1, 2, 3, 4, 5, 12, 19, 26]

c2 = [8, 9,10, 11, 18]

c3 = [15, 16, 17, 24, 25]

c4 = [29, 28, 35, 42, 43, 44]

c5 = [6, 13, 20, 27, 34, 33]

c6 = [23, 30, 31, 32, 39, 40]

c7 = [36, 37, 38, 45, 46, 47, 48, 41]


main(c1, c2, c3, c4, c5, c6, c7)
