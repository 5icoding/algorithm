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

# 背包问题
## 问题描述
⼀个⼩偷在某个商店发现有n个商品，第i个商品价值vi元，重wi千克。他希望拿⾛的价值尽量⾼，但他的背包最多只能容纳W千克的东⻄。他应该拿⾛哪些商品？

## 分析目标和过程：
假如一个小偷有一个可以容纳4千克的背包，但是发现面前只有有3样物品可以偷：台灯（30元，4千克）、音响（20元，3千克）、充电宝（15元，1千克）（价格和重量可能有点奇怪 ）。问，小偷能够偷到的物品的最大价格是多少（物品的重量不得超过背包的重量）？
![image](https://github.com/5icoding/algorithm/blob/main/img/Backtrack.png)


## 程序实现:

### 回溯算法
### 
1. 回溯法核心：能进则进，进不了则换，换不了则退。（按照条件深度优先搜索，搜到某一步时，发现不是最优或者达不到目标，则退一步重新选择）
* 注：理论上，回溯法是在一棵树上进行全局搜索，但是并非每种情况都需要全局考虑，毕竟那样效率太低，且通过约束+限界可以减少好多不必要的搜索。
2. 解决本问题思路：使用0/1序列表示物品的放入情况。将搜索看做一棵二叉树，二叉树的第 i 层代表第 i 个物品，若剩余空间允许物品 i 放入背包，扩展左子树。若不可放入背包，判断限界条件，若后续继续扩展有可能取得最优价值，则扩展右子树（即此 i 物品不放入，但是考虑后续的物品）。在层数达到物品的个数时，停止继续扩展，开始回溯。

* 注：如何回溯呢？怎样得到的，怎样恢复。放入背包中的重量取出，加在bagV上的价值减去。

3. 约束条件：放入背包中物品的总质量小于等于背包容量

4. 限界条件：当前放入背包中物品的总价值（i及之前） + i 之后的物品总价值 < 已知的最优值     这种情况下就没有必要再进行搜索 

5. 数据结构： 用一个变量记录当前放入背包的总价值 bagV（已扩展），一个变量记录后续物品的总价值 remainV（未扩展），当前已得到的一种最优值 bestV（全局情况），一个用0/1表示的数组bestArr[]记录哪些物品放入了背包。

6. 核心结构：递归思路进行解决。层层递归，递归到尽头，保留最优值，恢复递归中，层层回溯，即将原来加上去的重量与价值恢复。
```python
# -*- coding:utf-8 -*-
def Backtrack(t):
    global bestV, bagW, bagV,arr, bestArr, cntV

    if t > n: #某次深度优先搜索完成
        if bestV < bagV:
            for i in range(1, n+1):
                bestArr[i] = arr[i]
            bestV = bagV
    else:   #深度优先搜索未完成
        if bagW + listWV[t][0] <= w:    #第t个物品可以放入到背包中，扩展左子树
            arr[t] = True
            bagW += listWV[t][0]
            bagV += listWV[t][1]
            Backtrack(t+1)
            bagW -= listWV[t][0]
            bagV -= listWV[t][1]
        if cntV[t] + bagV > bestV:    #有搜索下去的必要
            arr[t] = False
            Backtrack(t+1)

w = int(input())    #背包大小
n = int(input())    #物品个数

listWV = [[0,0]]
listTemp = []
sumW = 0
sumV = 0

for i in range(n):
    listTemp = list(map(int, input().split()))  #借助临时list每次新增物品对应的list加入到listWV中
    sumW += listTemp[0]
    sumV += listTemp[1]
    listWV.append(listTemp) #依次输入每个物品的重量与价值

bestV = 0
bagW = 0
bagV = 0
remainV = sumV
arr = [False for i in range(n+1)]
bestArr = [False for i in range(n+1)]

cntV = [0 for i in range(n+1)]  #求得剩余物品的总价值,cnt[i]表示i+1~n的总价值
cntV[0] = sumV
for i in range(1, n+1):
    cntV[i] = cntV[i-1] - listWV[i][1]

if sumW <= w:
    print(sumV)
else:
    Backtrack(1)
    print(bestV)
    print(bestArr)
    print(cntV)
```
### 动态规划
* 动态规划的问题，一般是先解决子问题，然后由子问题推导，逐步解决大问题.
* 我们可以先解决1千克的背包能够获得的最大价值，2千克的背包能够获得的最大价值，直到4千克的背包能够获得的最大价值。
* 首先我们先搞定状态以及转移方程。我们这里定义状态f[i][v]，表示前i件物品恰好放入一个容量为v的背包可以获得的最大价值。
* 我现在获得的最大价值可以建立在第 i 个物品我不偷，那重量是v；也可以是第 i 个物品我偷了，那么前 i-1 个物品的总重量是 v-c[i] ，再加上我现在准备偷的第 i 个物品的价值 v[i]，取两者的最大值即可。
* 转移方程就是： 
* f [ i [ [ v ] = m a x ( f [ i − 1 ] [ v ] , f [ i − 1 ] [ v − c [ i ] ] + v [ i ] ) 
* f[i[[v] = max(f[i-1][v],f[i-1][v-c[i]]+v[i]) 
* f[i[[v]=max(f[i−1][v],f[i−1][v−c[i]]+v[i])

我们可以用一个网格来描述（每一个单元格都包含当前可装入背包的所有物品）：
![image](https://github.com/5icoding/algorithm/blob/main/img/Backtrack2.png)

1. 然后我们开始遍历这个网格，一开始我们填充台灯这一行。发现，当背包的容量为1千克的时候，由于台灯的重量是4千克，所以偷不了，所以此时获得的最大价值为0元。

![image](https://github.com/5icoding/algorithm/blob/main/img/Backtrack3.png)

2. 直到背包的容量为4千克的时候，我们才可以偷台灯，此时获得的最大价值为30元。

![image](https://github.com/5icoding/algorithm/blob/main/img/Backtrack4.png)

3. * 接下来我们开始遍历音响这一行，现在可以偷的物品有台灯和音响（每一行可以偷的物品只有当前行以及前一行的物品），同样的，发现直到背包的容量是3千克的时候才能装的下音响

![image](https://github.com/5icoding/algorithm/blob/main/img/Backtrack5.png)

* * 当背包的重量是4千克的时候，我们要么只能偷台灯，要么只能偷音响，发现偷台灯的价值会更大一点，所以我们选择偷台灯。

4. 最后我们来遍历充电宝这一行，发现当背包重量为1千克和2千克的时候，我们只能容纳充电宝，所以获得的最大价值为15元。

![image](https://github.com/5icoding/algorithm/blob/main/img/Backtrack6.png)
* * 当背包容量为3千克时候，我们可以获得的最大价值就是偷了音响，20元。

![image](https://github.com/5icoding/algorithm/blob/main/img/Backtrack7.png)

* * 当背包容量为4千克的时候，我们可以不偷充电宝，那么直接由上一行获得的最大价值传递过来，就是30元；我们也可以偷充电宝，那么要偷充电宝的话就只剩下3千克的背包容量了，在3千克的背包容量时能够获得的最大价值是20元，所以最后获得的最大价值为35元。两种情况比较，取最大值，所以最后小偷获得的最大价值为35元。
![image](https://github.com/5icoding/algorithm/blob/main/img/Backtrack8.png)

### 贪心算法
贪婪算法（不适用！！！）
* 0-1背包：对于⼀个商品，⼩偷要么把它完整拿⾛，要么留下。不能只拿⾛⼀部分，或把⼀个商品拿⾛多次。（商品为⾦条）
* 分数背包：对于⼀个商品，⼩偷可以拿⾛其中任意⼀部分。（商品为⾦砂）
举例：

商品1：v1=60 w1=10

商品2：v2=100 w2=20

商品3：v3=120 w3=30

背包容量：W=50
```python
goods = [(60, 10),(100, 20),(120, 30)]  # 每个商品元组表示(价格, 重量)
goods.sort(key=lambda x: x[0]/x[1], reverse=True)

# 分数背包的for实现
def fractional_backpack(goods, w):
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            total_v += prize
            w -= weight
        else:
            m[i] = w / weight
            total_v += m[i] * prize
            w = 0
            break
    return total_v, m
```
### 分支限界法
基本思想

* 分支限界法常以广度优先或以最小耗费（最大效益）优先的方式搜索问题的解空间树。在分支限界法中，每一个活结点只有一次机会成为扩展结点。活结点一旦成为扩展结点，就一次性产生其所有儿子结点。

* 在这些儿子结点中，导致不可行解或导致非最优解的儿子结点被舍弃，其余儿子结点被加入活结点表中。此后，从活结点表中取下一结点成为当前扩展结点，并重复上述结点扩展过程。这个过程一直持续到找到所需的解或活结点表为空时为止。

与回溯法的区别
1. 求解目标：
回溯法的求解目标是找出解空间树中满足约束条件的所有解，而分支限界法的求解目标则是找出满足约束条件的一个解，或是在满足约束条件的解中找出在某种意义下的最优解。
2. 搜索方式的不同：
回溯法以深度优先的方式搜索解空间树，而分支限界法则以广度优先或以最小耗费优先的方式搜索解空间树。

代码实现

```python
import heapq

# 物品信息
weight=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
value=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

print("物品信息如下：")
print("重量：")
print(weight)
print("价值：")
print(value)
# 背包容量
maxcap=35
print("最大背包容量为：%d\n"%maxcap)
n=len(weight)
# 当前重量与当前价值
cweight=0
cvalue=0
# 最优价值
bestv=0
bests=[]
num=0
heap=[]
heapq.heapify

# 上界函数：计算当前结点下的价值上界
def maxbound(i):
	global cweight
	global cvalue
	global n
	global weight
	global value
	global maxcap
	left = maxcap-cweight
	b=cvalue
	while i<n and weight[i]<=left:
		left-=weight[i]
		b+=value[i]
		i+=1
	if i<n:
		b+=(value[i]/weight[i])*left
	return b


# 分支限界算法求解01背包
i=0
upper=maxbound(i)
str=''

while(1):
	wt=cweight+weight[i]
	#print("wt:")
	#print(wt)
	if wt<=maxcap:
		if cvalue+value[i]>bestv:
			#print("i=%d"%i)
			bestv=cvalue+value[i]
			#print("bestv=%d"%bestv)
			
			# 存储当前最优值的最优路径
			bests=str+'1'
			bests=bests+'0'*(n-len(bests))
		# 入堆： 由于python只有小根堆，因此通过对上界值取倒，实现上界值大，优先级高                         
		if i+1<n:
			heapq.heappush(heap,[1/upper,cweight+weight[i],cvalue+value[i],i+1,str+'1'])

	upper=maxbound(i+1)
	if upper>=bestv:
		if i+1<n:
			heapq.heappush(heap,[1/upper,cweight,cvalue,i+1,str+'0'])

	if len(heap)==0:
		print("%d个物品的状态（1为被装入背包，0为未被装入背包）：%s"%(n,bests))
		print("最优价值为： %d"%bestv)
		break

	#print("heap:")
	#print(heap)
	node=heapq.heappop(heap)
	upper=1/node[0]
	cweight=node[1]
	cvalue=node[2]
	i=node[3]
	str=node[4]
	#print('node:')
	#print(node)

```
### 附
1. https://blog.csdn.net/weixin_46540009/article/details/116468540
2. https://zhuanlan.zhihu.com/p/485786077
3. https://www.cnblogs.com/chenleideblog/p/11255965.html
4. https://blog.csdn.net/qq_42939527/article/details/104043900

![image](https://github.com/5icoding/algorithm/blob/main/img/coins.png)