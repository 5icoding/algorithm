#国王给骑士发金币
money = 0
print('骑士的金币数:',money)
days = int(input("请输入天数"))

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

print('骑士的金币数:',money)