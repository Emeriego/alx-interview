#!/usr/bin/python3
"""
Making Change - interview
"""


def makeChange(coins, sum):
    """
    Given a list of coin denominations and a sum amount, return the fewest
    number of coins needed to make up that amount. If that amount of money
    cannot be made up by any combination of the coins, return -1.

    coins is a list of the values of the coins in your possession
    sum is the sum amount of money you need to make up
    Return the fewest number of coins needed to make up the sum amount
    If that amount of money cannot be made up by the coins, return -1

    """
    if sum <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        x = coins.index(sum)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coin_count = 0
    for i in coins:
        if sum % i == 0:
            coin_count += int(sum / i)
            return coin_count
        if sum - i >= 0:
            if int(sum / i) > 1:
                coin_count += int(sum / i)
                sum = sum % i
            else:
                coin_count += 1
                sum -= i
                if sum == 0:
                    break
    if sum > 0:
        return -1
    return coin_count
