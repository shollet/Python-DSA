def coinChange(total, coins):
    n = total
    coins.sort()
    index = len(coins) - 1 
    while True:
        coinValue = coins[index]
        if n >= coinValue:
            print(coinValue)
            n -= coinValue
        if n < coinValue:
            index -= 1
        if n == 0:
            break       

coins = [1,2,5,20,50,100]
coinChange(201, coins)