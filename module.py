import copy
import random

import pymnet
from pymnet import *
import matplotlib
matplotlib.use('TkAgg')


net = pymnet.net.MultilayerNetwork(aspects=1)
dictColor = {}
dictSize = {}
spreadStatus = []
checkeStatus = []

def drawPicture():
    fig = draw(net,
               show=True,
               layout="random",
               layerColorDict={'a': 'black'},
               nodeColorDict=dictColor,
               nodeSizeDict=dictSize,
               nodeSizeRule={"rule": "scaled", "propscale": 0.3},
               nodeLabelRule={},
               edgeColorRule={},
               alignedNodes=0,
               defaultEdgeWidth=0.1,
               edgeColorDict={'b':'red'},
               )

    #fig.savepdf("test.pdf")

def init(upRate,upToDownRate,downConnectRate,amount):
    for i in range(0, amount):
        spreadStatus.append(0)
        checkeStatus.append(0)


    #初始化连接
    for i in range(0,int(amount*upRate)):
        for j in range(0, int(amount*upToDownRate)):
            net[i,'a'][random.randint(1,amount), 'b'] = 1

    for i in range(0,amount):
        for j in range(0,int(amount*downConnectRate)):
            net[i,'b'][random.randint(1,amount),'b'] = 1

    for i in range(0,int(amount*upRate)):
        dictColor.update({(i,'a'):"r"})
        dictSize.update({(i,'a'):0.005})

    for i in range(int(amount*upRate),amount):
        dictSize.update({(i, 'a'): 0})

# 传染模型 Connections为节点连结关系属性矩阵，Infecters为初始感染者，Beta为感染率
def infect(InfectStatus, Beta,spreadFalse):
    spreadFlag = False
    Status1 = copy.deepcopy(InfectStatus)  # 前一状态感染者列表
    Status2 = copy.deepcopy(InfectStatus)  # 当前状态待更新感染者列表
    for i in range(len(Status1)):  # 遍历所有节点，发现感染者
        if Status1[i] == 1:  # 若状态为1，即为感染
            for j in range(len(Status1)):
                if Status1[j] == 0 and net[i,'b'][j,'b'] == 1:  # 若连结关系为1，即为连结
                    if (random.random() <= Beta) and (checkeStatus[i] == 0):  # 若生成的随机数小于Beta则登记为感染
                        Status2[j] = 1  # i感染j
                        checkeStatus[i] = 1
                        dictColor.update({(i, 'b'): "r"})
                        dictSize.update({(i, 'b'): 0.005})
                        spreadFlag = True
    if(spreadFlag == False):
        spreadFalse += 1
    return Status2,spreadFalse  # 返回新的感染者列表


def upToDown(InfectStatus,Beta,spreadFalse):
    spreadFlag = False
    Status1 = copy.deepcopy(InfectStatus)
    Status2 = copy.deepcopy(InfectStatus)
    for i in range(0,4):  # 遍历所有节点，发现感染者
        for j in range(0,len(Status1)):
            if InfectStatus[j] == 0 and net[i,'a'][j,'b'] == 1:  # 若连结关系为1，即为连结
                if (random.random() <= Beta) and (Status1[i] == 0):  # 若生成的随机数小于Beta则登记为感染
                    Status2[j] = 1  # i感染j
                    dictColor.update({(j, 'b'): "r"})
                    dictSize.update({(j, 'b'): 0.005})
                    spreadFlag = True
    if(spreadFlag == False):
        spreadFalse += 1
    return Status2,spreadFalse  # 返回新的感染者列表

init(0.05,0.1,0.02,100)
drawPicture()

spreadStatus,spreadFalse = upToDown(spreadStatus,0.8,0)
drawPicture()

i = 0
while(1):
    if(spreadFalse >= 1):
        spreadStatus, spreadFalse = infect(spreadStatus, 0.8, spreadFalse)
        print("Over!")
        drawPicture()

        break
    i = i + 1
    print("Time:",i)
    spreadStatus, spreadFalse = infect(spreadStatus, 0.1, spreadFalse)
    drawPicture()