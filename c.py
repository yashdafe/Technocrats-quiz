import random, math

def random_noise():
    random_characters = ['$', '!', 'p', '-_-', ':D', '~', '@', '#']
    random_index = [random_characters[random.randint(0, len(random_characters) - 1)] for i in range(4)]

    temp = ""
    for i in random_index:
        temp = temp + i

    return temp
    print("TRY TO STOP THIS FROM BEING PRINTED IN FILE a.py WITHOUT DELETING THIS PRINT STATEMENT")


def hypotenuse(x, b):
    return math.sqrt(x**2 + b**2)

