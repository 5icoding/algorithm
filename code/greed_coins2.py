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

file = r"coin2.csv"
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
