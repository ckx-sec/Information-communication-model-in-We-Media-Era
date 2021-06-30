import numpy as np
import random
import copy
import matplotlib.pyplot as plt
import networkx as nx


# 传染模型 Connections为节点连结关系属性矩阵，Infecters为初始感染者，Beta为感染率
def infect(Connections, InfectStatus, Beta):
    Status1 = copy.deepcopy(InfectStatus)  # 前一状态感染者列表
    Status2 = copy.deepcopy(InfectStatus)  # 当前状态待更新感染者列表
    C = copy.deepcopy(Connections)
    Nodes = len(C)
    if sum(InfectStatus) < Nodes/2:  # 当感染节点数小于总数的一半时
        for i in range(len(Status1)):  # 遍历所有节点，发现感染者
            if Status1[i] == 1:  # 若状态为1，即为感染
                for j in range(len(C[i])):
                    if Status1[j] == 0 and C[i][j] == 1:  # 若连结关系为1，即为连结
                        if random.random() <= Beta:  # 若生成的随机数小于Beta则登记为感染
                            Status2[j] = 1  # i感染j
    else:
        for a in range(len(Status1)):
            if Status1[a] == 0:
                for b in range(len(C[a])):
                    if Status1[b] == 1 and C[a][b] == 1:
                        if random.random() <= Beta:
                            Status2[a] = 1
    return Status2  # 返回新的感染者列表


def catastrophe(Nodes, Amount):  # 设置初始感染者数量，在随机位置生成
    a = range(Nodes)
    Infecters = random.sample(a, Amount)
    InfectStatus = np.zeros(Nodes, int)  # 感染状态表
    for i in Infecters:
        InfectStatus[i] = 1  # 感染者登记为1
    return InfectStatus  # 返回一个感染者编号列表


# 传染病迭代输出模型        #Connections为网络关系矩阵，Amount为初始（0时期）感染者数量
def show_iteration(Connections, Amount, Beta):
    C = copy.deepcopy(Connections)
    Nodes = len(C)
    InfecterStatus = catastrophe(Nodes, Amount)  # 根据设定的初始感染数，在随机位置生成感染者
    g = nx.Graph()  # 新建画布
    for n in range(Nodes):  # 在画布上设置节点
        g.add_node(n)
    for ed in range(Nodes):  # 在画布上设置边（连结关系）
        for lin in range(ed+1, Nodes):
            if C[ed][lin] == 1:
                g.add_edge(ed, lin)
    pos = nx.kamada_kawai_layout(g)  # kamada-kawai路径长度成本函数计算
    Status = {}
    times = 0
    while sum(InfecterStatus) <= Nodes:  # 当感染数大于等于节点数时停止迭代
        # plt.imshow(InfecterStatus)
        # plt.pause(3)#帧数
        for s in range(len(InfecterStatus)):  # 把感染状态写入字典
            SI = InfecterStatus[s]
            Status[s] = SI
        colors = []
        for c in g:  # 分配各节点颜色表示感染状态
            sta = Status[c]
            if sta == 1:
                clr = 'r'
            if sta == 0:
                clr = 'g'
            colors.append(clr)
        nodesize = []
        for ns in g:
            de = ((sum(C[ns])*10)+50)  # 节点大小(节点度数越大，节点越大)
            nodesize.append(de)
        plt.figure(figsize=(12, 8))
        nx.draw_networkx_nodes(g, pos=pos,
                               node_color=colors, node_size=nodesize, alpha=0.6)
        nx.draw_networkx_edges(
            g, pos=pos, width=0.3, alpha=0.3)
        print(
            f'迭代第 {times} 次 ---- 感染者数量：{sum(InfecterStatus)} ---- 占比：{(sum(InfecterStatus)/Nodes)}')
        plt.show()
        if sum(InfecterStatus) == Nodes:
            Nodes = Nodes - 1
        InfecterStatus = infect(C, InfecterStatus, Beta)  # 传染模型
        times += 1
    print('---------- 迭代完成 ----------')
