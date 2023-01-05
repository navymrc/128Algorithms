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
        elem += 1 << item

    return int(math.log(-elem & elem)/math.log(2))


# minimum example
#r = min_((103, 91, 14))
#print(f"{r}\n{[0]* (1<<2)}")


def three_partition(x):
    """

    :param x:
    :return:
    """
    f = [0] * (1 << len(x))
    for i, _ in enumerate(x):
        for S in range(1 << i):
            f[S | (1 << i)] = f[S] + x[i]
    for A in range(1 << len(x)):
        for B in range(1 << len(x)):
            if A & B == 0 and f[A] == f[B] and 3 * f[A] == f[-1]:
                return A, B, ((1 << len(x)) - 1) ^ A ^ B
    return None


x = three_partition([2, 2, 2, 2, 2, 2])
print(f"{x}")
