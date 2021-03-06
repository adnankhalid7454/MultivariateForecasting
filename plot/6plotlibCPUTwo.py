#coding:utf-8
import pandas as pd
import numpy as np
import  os
from pylab import *
from matplotlib.ticker import  MultipleLocator

from matplotlib.ticker import  FormatStrFormatter

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#最坏的
xWorst = []
yWorst = []

#线性
xLinear = []
yLinear = []

#lstm的
xLSTM = []
yLSTM = []

#lstmQ-learning的
xLSTMQL = []
yLSTMQL = []

for num in(range(288)):
    xWorst.append(num)
    xLSTM.append(num)
    xLSTMQL.append(num)
    xLinear.append(num)
#从文件读取虚拟机个数
yTxt = open('6plotlibCPU.txt')  #worst
yRead=yTxt.read()
yList = yRead.split(' ')

yTxt4 = open('6plotlibCPULinear.txt')  #线性
yRead4=yTxt4.read()
yList4 = yRead4.split(' ')

yTxt2 = open('6plotlibCPULSTM.txt')  #lstm
yRead2=yTxt2.read()
yList2 = yRead2.split(' ')

yTxt3 = open('6plotlibCPULSTMQL.txt')  #lstmQl
yRead3=yTxt3.read()
yList3 = yRead3.split(' ')

yWorstMean = 0;
yLSTMMean = 0;
yLSTMQLMean = 0;
yLinearMean = 0;

for str1 in yList:
    yWorst.append(float(str1))
    yWorstMean = yWorstMean + float(str1)
for str2 in yList2:
    yLSTM.append(float(str2))
    yLSTMMean = yLSTMMean + float(str2)
for str3 in yList3:
    yLSTMQL.append(float(str3))
    yLSTMQLMean = yLSTMQLMean + float(str3)
for str4 in yList4:
    yLinear.append(float(str4))
    yLinearMean = yLinearMean + float(str4)

yWorstMean = yWorstMean/288
yLSTMMean = yLSTMMean/288
yLSTMQLMean = yLSTMQLMean/288
yLinearMean = yLinearMean/288
print(yWorstMean)
print(yLSTMMean)
print(yLSTMQLMean)
print(yLinearMean)


############################
#最坏的
xCWorst = []
yCWorst = []

#线性
xCLinear = []
yCLinear = []

#lstm的
xCLSTM = []
yCLSTM = []

#lstmQ-learning的
xCLSTMQL = []
yCLSTMQL = []

for num in(range(288)):
    xCWorst.append(num)
    xCLSTM.append(num)
    xCLSTMQL.append(num)
    xCLinear.append(num)
#从文件读取虚拟机个数
yCTxt = open('6plotlibCPUTwo.txt')  #worst
yCRead=yCTxt.read()
yCList = yCRead.split(' ')

yCTxt4 = open('6plotlibCPUTwo.txt')  #线性
yCRead4=yCTxt4.read()
yCList4 = yCRead4.split(' ')

yCTxt2 = open('6plotlibCPULSTMTwo.txt')  #lstm
yCRead2=yCTxt2.read()
yCList2 = yCRead2.split(' ')

yCTxt3 = open('6plotlibCPULSTMQLTwo.txt')  #lstmQl
yCRead3=yCTxt3.read()
yCList3 = yCRead3.split(' ')


yWorstMean = 0;
yLSTMMean = 0;
yLSTMQLMean = 0;
yLinearMean = 0;
for str1 in yCList:
    yCWorst.append(float(str1))
    yWorstMean = yWorstMean + float(str1)
for str2 in yCList2:
    yCLSTM.append(float(str2))
    yLSTMMean = yLSTMMean + float(str2)
for str3 in yCList3:
    yCLSTMQL.append(float(str3))
    yLSTMQLMean = yLSTMQLMean + float(str3)
for str4 in yCList4:
    yCLinear.append(float(str4))
    yLinearMean = yLinearMean + float(str4)

yWorstMean = yWorstMean/288
yLSTMMean = yLSTMMean/288
yLSTMQLMean = yLSTMQLMean/288
yLinearMean = yLinearMean/288
print(yWorstMean)
print(yLSTMMean)
print(yLSTMQLMean)
print(yLinearMean)

plt.subplot(211)
plt.tick_params(labelsize=15)
plt.plot(xWorst, yWorst, color='skyblue', linestyle='-', label="Worst",marker="*")
plt.plot(xWorst, yLinear, color='green', linestyle='-', label="Linear",marker="*")
plt.plot(xLSTM, yLSTM, color='orangered', linestyle='-', label="LSTM",marker="x")
plt.plot(xLSTMQL, yLSTMQL, color='black', linestyle='-', label="LSTMQL",marker="x")
plt.legend() # 显示图例
plt.xlabel('Time interval(5min)', fontsize=15)
plt.ylabel('CPU Utilization of NASA(%)', fontsize=15)


plt.subplot(212)
plt.tick_params(labelsize=15)
plt.plot(xCWorst, yCWorst, color='skyblue', linestyle='-', label="Worst",marker="*")
plt.plot(xCWorst, yCLinear, color='green', linestyle='-', label="Linear",marker="*")
plt.plot(xCLSTM, yCLSTM, color='orangered', linestyle='-', label="LSTM",marker="x")
plt.plot(xCLSTMQL, yCLSTMQL, color='black', linestyle='-', label="LSTMQL",marker="x")
plt.legend() # 显示图例
plt.xlabel('Time interval(5min)', fontsize=15)
plt.ylabel('CPU Utilization of ClarkNet(%)', fontsize=15)
plt.show()


#
#
#
#
# jiaodu = ['0', '15', '30', '15', '60', '75', '90', '105', '120']
# x = range(len(jiaodu))
#
# y = [85.6801, 7.64586, 86.0956, 159.229, 179.534, 163.238, 96.4436, 10.1619, 90.9262, ]
#
# # plt.figure(figsize=(10, 6))
#
# plt.plot(x, y, 'b-', label="1", marker='*', markersize=7, linewidth=3)  # b代表blue颜色  -代表直线
#
# plt.title('vm个数')
# plt.legend(loc='upper left',bbox_to_anchor=(1.0,1.0))
# # plt.xticks((0,1,2,3,4,5,6,7,8),('0', '15', '30', '15', '60', '75', '90', '105', '120'))
# plt.xlabel('角度')
# plt.ylabel('亮度')
# #plt.grid(x1)
# plt.show()
