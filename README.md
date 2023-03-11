# algorithm
Introduction to algorithm，算法入门（用python实现）

# 什么是算法？
算法，就是用来解决问题的一组规则和指令。

# 基本算法
## 一、分糖果
### 问题描述：
1. 现在有5个小朋友要分糖果，他们按照自己的编号顺序围坐在一张圆桌旁边。他们身上都有一些糖果（通过输入来决定每个小孩糖果的数量）。

2. 从1号小朋友开始，将自己的糖果平均分成最多的3份（多出来的自己吃掉），自己留一份，其余两份分给他相邻的两位小朋友。接着2号，3号，4号，5号小朋友同样这么做。这样进行一轮后，每个小朋友手上分到的糖果有多少？

### 分析目标和过程：
我们来解释一下这个题目的意思：

1. 执行程序后，当我输入8，9，10，11，12就代表5个小朋友的糖果分别是8，9，10，11，12颗。

2. 1号小朋友现在手上是8颗糖果，现在1号小朋友需要将糖果分成3份，因为需要让每份糖果的数量最多且平均，所以只能是2+2+2，剩下的两颗只能自己吃掉。

![image](https://github.com/5icoding/algorithm/blob/main/img/ftg.png)

3. 然后自己拿两颗，剩下的两颗分别给到左边的5号和右边的2号。同学们想一想，剩下的小朋友应该如何去平分糖果。

4. 2号小朋友现在手里的糖果就是9+2 = 11颗糖果了，然后他也需要和1号一样把自己的糖果分成3分，也就是3+3+3，剩下的两颗自己吃掉。

### 程序实现:
第一步是处理糖果的输入:
```python
num_01 = int(input("请输入1号小朋友的糖果数: "))
num_02 = int(input("请输入2号小朋友的糖果数: "))
num_03 = int(input("请输入3号小朋友的糖果数: "))
num_04 = int(input("请输入4号小朋友的糖果数: "))
num_05 = int(input("请输入5号小朋友的糖果数: "))
print(num_01,num_02,num_03,num_04,num_05)
```
第二步开始分糖果:
```python
#一号小朋友分为糖果后，每位小朋友糖果的变化情况
num_01 = int(num_01/3)
num_05 = num_01 + num_05
num_02 = num_01 + num_02

#二号小朋友分为糖果后，每位小朋友糖果的变化情况
num_02 = int(num_02/3)
num_01 = num_02 + num_01
num_03 = num_02 + num_03

#三号小朋友分为糖果后，每位小朋友糖果的变化情况
num_03 = int(num_03/3)
num_02 = num_02 + num_03
num_04 = num_04 + num_03

#四号小朋友分为糖果后，每位小朋友糖果的变化情况
num_04 = int(num_04/3)
num_03 = num_04 + num_03
num_05 = num_04 + num_05

#五号小朋友分为糖果后，每位小朋友糖果的变化情况
num_05 = int(num_05/3)
num_04 = num_04 + num_05
num_01 = num_01 + num_05
```
第三步输出结果:
```python
print(num_01,num_02,num_03,num_04,num_05)
```
## 二、国王发金币

### 问题描述：
国王将金币作为工资，发放给忠诚的骑士。

第一天，骑士收到一枚金币；

之后两天（第2天和第3天）里，每天收到两枚金币；

之后三天（第4，5，6天）里，每天收到三枚金币；

之后四天（第7，8，9，10天）里，每天收到四枚金币......

这种工资发放模式会一直这样延续下去：当连续n天每天收到n枚金币后，骑士会在之后的连续n+1天里，每天收到n+1枚金币（n为任意正整数）。

你需要编写一个程序，确定从第一天开始到给定天数内，骑士一共获得了多少金币。
### 分析目标和过程：
这个题目的目标很明确，需要计算骑士的工资。

第1天：1个金币

第2天：2个金币

第3天：2个金币

第4天：3个金币

第5天：3个金币

第6天：3个金币

。。。

如果我输入的是4，那么骑士从第一天到第四天一共获得了：1+2+2+3 = 8枚金币；

如果输入的是6，那么骑士获得的金币是：1+2+2+3+3+3 = 14枚金币。

我们需要找到骑士获得金币的规律：

第1个周期（第1天）：获得1金币

第2个周期（第2，3天）：获得2次2金币

第3个周期（第4，5，6天）：获得3次3金币
。。。

可以看出，周期数和金币数是同步增长的，在第1个周期里，循环增长1次；第2个周期里，循环增长2次2个金币；第3个周期里，循环增长3次3个金币…

这里要注意，金币并不是无限增长下去的，边界条件就是你输入要领金币的天数。比如输入4，只能领到第3个周期的第1天。
### 程序实现:
1. 设置好初始值，包括要计算的天数，以及累计的天数。
```python
money = 0
print('骑士的金币数:',money)
days = int(input("请输入天数"))
```
2. 是遍历周期，从第一个周期开始，最多到第days个周期结束。
```python
count = 0
#i代表的是周期数，第一次循环的时候i表示的是第一个周期
for i in range(1,days+1):
    #在第i个周期内，每天领到的金币数量就是i，比如第2个周期内
    #（第2，3天）领到的金币数量就是2
    for j in range(0,i):
        count += 1
        #累计获得的天数还没有达到要计算的天数
        if count <= days:
            money += i
```
3. 输出金币数
```python
print('骑士的金币数:',money)
```

# 高级算法
## Python中如何求阶乘
* 阶乘是基斯顿·卡曼（Christian Kramp，1760～1826）于 1808 年发明的运算符号，是数学术语。
* 一个正整数的阶乘（factorial）是所有小于及等于该数的正整数的积，并且0的阶乘为1。自然数n的阶乘写作n!。1808年，基斯顿·卡曼引进这个表示法。
* 即n!=1×2×3×...×(n-1)×n。
阶乘亦可以递归方式定义：
0!=1，
n!=(n-1)!×n。
### 第一种：普通的for循环
```python
a = int(input('please inputer a integer:'))
num = 1
if a < 0:
    print('负数没有阶乘！')
elif a == 0:
    print('0的阶乘为1！')
else :
    for i in range(1,a + 1):
        num *= i
    print(num)
```
### 第二种：递归调用
```python
def num(n):
    if n == 0:
        return 1
    else:
        return n * num(n - 1)
print(num(6))
```
### 第四种：factorial()函数
```python
import math
value = math.factorial(6)
print(value)
```
## 贪心算法与动态规划
### 以谈恋爱举例：很多人来追求你。 
* 贪心算法就是你根据你现在对他们的了解，你喜欢漂亮的，你挑一个最漂亮的，你喜欢有钱的，你挑一个最有钱的，只在意当前的最佳选择； 
* 动态规划算法就是你对他们进行了一番深入的调查和了解之后，谁家未来可能会拆迁，谁又可能是未来十年的潜力股，最终和可能走的更长久的人在一起！
### 贪心与动态规划的相同点与区别
* 相同点：要求原问题必须有最优子结构。
* 不同点：贪心法的计算方式“自顶向下”，但并不等待子问题求解完毕后再选择使用哪一个，而是通过一种策略直接选择一个子问题去求解，没被选择的子问题直接抛弃。这种所谓“最优选择”的正确性需要用归纳法证明。
* 贪心算法：壮士断腕的决策，只要选择，绝不后悔。
* 动态规划不管是采用自底向上还是自顶向下的计算方式，都是从边界开始向上得到目标问题的解（即考虑所有子问题）。
### 怎样判断是贪心还是动态规划
* 就看你能否判断出贪心是否有bug，如果能证明贪心不可行，可能就是动归求解了。
* 关键点在于：1.证明贪心的可行性  2.多刷题，凭经验判断
# 贪心算法
### 硬币找零
### 假设某国硬币面值有1,5,10,25,100元五种面额，若店员为顾客找零时，需要给顾客找零a=36元，求硬币数最少的情况。
![image](https://github.com/5icoding/algorithm/blob/main/img/coins.png)
1. for循环版本
```python
coins = [1,5,10,25,100]
a = 36

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
``` 
说明：
* [::-1]的作用是对列表进行翻转
* “//”是一个算术运算符，表示整数除法，它可以返回商的整数部分（向下取整）。具体用法如：【a = 10 b = 5 c = a//b 】，结果输出整数2。
2. 递归调用版本
```python
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
```
### 硬币找零复杂版
### 问题描述
假设某国有1元、2元、5元、10元、20元、50元、
100元 的纸币，纸币分别有c0, c1, c2, c3, c4, c5, c6张。现在要用这些钱来支付K元，至少要用多少张纸币？
### 分析目标和过程：
要解决该问题，一般也有两个数组，一个表示面额的大小，一个表示不同面额钱币对应的数量，并且表示面额的数组是有序的。

由于该题目求的是最少的纸币数，所以理所应当要先使用大额纸币，然后依次递减，用较小额的纸币，直到表示完所有钱币。

所以该题的解决思路是：优先使用大额钱币，待大额钱币使用完后，再使用次大额的钱币，直到完全表示了K元。同样，该问题也有迭代和递归两种解法。
![image](https://github.com/5icoding/algorithm/blob/main/img/coins2.png)
1. for循环版本
```python
import pandas as pd
import numpy as np

#钱币找零问题的迭代解法
def Coin_Greedy(file, money=235):
    #读取file文件中的数据
    countmoney = pd.read_csv(file)
    #将读取到的数据转为numpy数组
    countmoney = np.array(countmoney)
    #将numpy数组转为list列表数组
    date = countmoney.tolist()
    #对list列表数组进行排序
    date.sort()
    #结果数组，用来存放每种面额对应的钱币的数量
    list = []
    #先用大额钱币，所以从后向前遍历date[i][0]数组
    for i in range(len(date)-1, -1, -1):
        #使用当前面额钱币时，用到的数量
        num = min(date[i][1], money//date[i][0])
        #将结果存储到结果数组
        list.append(num)
        #钱币总额需要减掉已表示的钱币额度
        money = money - num*date[i][0]
    bool = False
    if money>0:
        bool = True
    return list, date, bool

file = r"test.csv"
#钱币找零问题的迭代解法
#result结果数组，用来存放每种面额对应的钱币的数量
#date人民币面额和各种面额对应数量二维数组集合
#bool用于判断钱币是否过大

result, date, bool = Coin_Greedy(file, 235)
#对result数组进行反序
result = result[::-1]
for i in range(len(result)):
    if bool:
        print("金额过大!!!")
        break
    #当对应面额的钱币数量为0时，没必要打印
    elif result[i]!=0:
        print("需要用面额{:.2f}元的钱币{}张".format(date[i][0],result[i]))
```
2. 递归调用版本
```python
#钱币找零问题的递归解法
def Coin_Greedy2(values, counts, money, position, result):
    if money>0:
        num = min(counts[position], money//values[position])
        result.append(num)
        Coin_Greedy2(values, counts, money-num*values[position], position-1, result)

#钱币找零问题的递归解法
countmoney = pd.read_csv(file)
countmoney = np.array(countmoney)
date = countmoney.tolist()
date.sort()
values, counts, result1 = [], [], []
for i in range(len(date)):
    values.append(date[i][0])
    counts.append(date[i][1])
Coin_Greedy2(values, counts, 235, len(values)-1, result1)
result1 = result1[::-1]
for i in range(len(result1)):
    if result1[i]!=0:
        print("需要用面额{:.2f}元的钱币{}张".format(values[i],result1[i]))
```
# 动态规划
## 硬币找零
### for循环实现
```python
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```
### 递归实现
```python
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
```

