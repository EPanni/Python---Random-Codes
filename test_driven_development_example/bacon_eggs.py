""" Bacon and Eggs example
1 - It must receive an Int as input
2 - I need to know if the number is a multiple of 3 and 5:
    Bacon and Eggs
3 - I need to know if the number is only a multiple of 3 and not 5:
    Bacon
4 - I need to know if the number is a multiple of 5 and not 3:
    Eggs
4 - I need to know if the number is NOT multiple a of 5 nor 3:
    Starving
"""


def bacon_and_eggs(n):
    """Function to be tested"""
    assert isinstance(n, int), "'n' must be int"
    if n % 3 == 0 and n % 5 == 0:
        return "Bacon and Eggs"

    if n % 3 != 0 and n % 5 != 0:
        return "Starving"

    if n % 3 == 0 and n % 5 != 0:
        return "Bacon"

    if n % 3 != 0 and n % 5 == 0:
        return "Eggs"
