def happyPanda(coins, candies):
    pcoins = 0
    phappiness = 0

    biggest_happiness = -1
    for coin, candy in zip(coins, candies):
        pcoins += coin
        if pcoins < candy[0]:
            if candy[1] >= biggest_happiness:
                phappiness -= candy[1]
        else:
            pcoins -= candy[0]
            phappiness += candy[1]
            if candy[1] > biggest_happiness:
                biggest_happiness = candy[1]

    return phappiness



"""
Little Panda likes candies very much, so his father gives him coins[i] coins on the ith day to buy some.
There is only one candy store in Panda's home town, and on the ith day they sell only one candy with price
candies[i][0] and tastiness candies[i][1].

Little Panda buys the candy on the ith day if he can afford it and that makes him happier by candies[i][1] points.
He saves all the coins left after the purchase to buy more candies later. If he can't afford the candy,
it doesn't necessarily make him less happy (obviously it doesn't make him happier anyway). It only decreases
his happiness if he hasn't bought any candy tastier than the current one before. In that case, his happiness
decreases by candies[i][1] points.

Your task is to find how happy Panda will be after all the days. Panda has 0 coins before the day number 0.

Example

For coins = [10, 10, 10]and candies = [[10, 20], [9, 10], [11, 50]], the output should be happyPanda(coins, candies) = 80

Panda takes 10 coins on day 0. He has 10 coins now, so he buys the candy.
At the end of the day he has 0 coins and 20 happiness points.
He takes 10 coins on day 1 . He has 10 coins now, so he buys the candy.
At the end of the day he has 1 coin and 30 happiness points.
He takes 10 coins on day 2. He has 11 coins now, so he buys the candy.
At the end of the day he has 0 coins and 80 happiness points.
After all the days Panda has 80 happiness points.

For coins = [10, 10, 10] and candies = [[10, 20], [10, 10], [11, 50]], the output should be happyPanda(coins, candies) = -20

Panda takes 10 coins on day 0. He has 10 coins now, so he buys the candy.
At the end of the day he has 0 coins and 20 happiness points.
He takes 10 coins on day 1 . He has 10 coins now, so he buys the candy.
At the end of the day he has 0 coins and 30 happiness points.
He takes 10 coins on day 2. He has 10 coins now, so he can't afford the candy. As 50 > 20 and 50 > 10,
that makes him less happy by 50 points (since this is tastier than any candy he's bought before).
 At the end of the day he has 0 coins and -20 happiness points.
After all the days Panda has -20 happiness points.

For coins = [10, 10, 10] and candies = [[10, 20], [10, 10], [11, 20]], the output should be happyPanda(coins, candies) = 10

Panda takes 10 coins on day 0. He has 10 coins now, so he buys the candy.
At the end of the day he has 0 coins and 20 happiness points.
He takes 10 coins on day 1. He has 10 coins now, so he buys the candy.
At the end of the day he has 0 coins and 30 happiness points.
He takes 10 coins on day 2. He has 10 coins now, so he can't afford the candy.
As 20 = 20 and 20 > 10, that makes him less happy by 20 points
(since this is as tasty as any candy he's bought before).
At the end of the day he has 10 coins and 10 happiness points.
After all the days Panda has 10 happiness points.
"""