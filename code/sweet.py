#分糖果算法

num_01 = int(input("请输入1号小朋友的糖果数: "))
num_02 = int(input("请输入2号小朋友的糖果数: "))
num_03 = int(input("请输入3号小朋友的糖果数: "))
num_04 = int(input("请输入4号小朋友的糖果数: "))
num_05 = int(input("请输入5号小朋友的糖果数: "))
print(num_01,num_02,num_03,num_04,num_05)

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

print(num_01,num_02,num_03,num_04,num_05)

