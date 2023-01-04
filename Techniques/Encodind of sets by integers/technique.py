import math


def min_(sets):
    """
    Extraction of the minimum of a set.
    
    :param sets
    :type sets: tuple
    :rtype: int
    """
    elem = 0
    for item in sets:
        elem += 2 ** item

    return int(math.log(-elem & elem)/math.log(2))


r = min_((103, 91, 14))

print(f"{r}\n{[0]* (1<<2)}")
