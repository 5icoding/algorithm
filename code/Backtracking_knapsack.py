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