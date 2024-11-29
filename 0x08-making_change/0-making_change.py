#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Generate changes needed to reach total

    Args:
        coins ([List]): [List of Coins available]
        total ([int]): [total amount needed]
    """
    if total <= 0:
        return 0
    checking = 0
    tmp = 0
    coins.sort(reverse=True)
    for i in coins:
        while checking < total:
            checking += i
            tmp += 1
        if checking == total:
            return tmp
        checking -= i
        tmp -= 1
    return -1