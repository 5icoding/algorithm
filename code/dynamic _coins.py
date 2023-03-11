def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


def rec_coin(target, coins):
    min_coins = target
    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin(target-i, coins)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

