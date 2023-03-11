coins = [1,5,10,25,100]
a = 63

def shortNum(c,a):  
  out = []
  coins2 = c[::-1] 
  for i in coins2:
    num = a//i
    out=out+[i,]*num
    a = a-num*i
    if a<=0:
      break
  return out

print(shortNum(a))

# 定义一个硬币数组 coins 和需要找零的金额 amount
coins = [1, 5, 10, 25]
amount = 63

# 定义递归函数，返回找零所需的最小硬币数
def coinChange(amount, coins):
    if amount == 0:
        return 0
    minCoins = float('inf')
    for coin in coins:
        if coin <= amount:
            numCoins = coinChange(amount - coin, coins) + 1
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

# 输出结果：5
print(coinChange(amount, coins))
