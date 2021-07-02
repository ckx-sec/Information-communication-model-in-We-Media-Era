from __future__ import annotations
from typing import Tuple
from node import *
from message import *
import copy
import numpy as np
import random


class Network:
    def __init__(self):
        self.nodes:list[Node] = []
        self.edges:list[Tuple[Node,Node]] = []
        self.adjMatrix = np.zeros(
            [len(self.nodes), len(self.nodes)], dtype=int)
        self.type:list = []

    def generate_network(self):

        pass

    def addNode(self, node: Node):
        pass

    def removeNode(self):
        pass

    def topic_input(self, message: Message, initialNode: Node):
        infectStatus = np.zeros(len(self.adjMatrix), dtype=int)
        # topicList:list=message.getClassification
        if(isinstance(initialNode, Blogger)):
            infectors = copy.deepcopy(initialNode.follower)
        if(isinstance(initialNode, Viewer)):
            infectors = copy.deepcopy(initialNode.following)
        for i in infectors:
            infectStatus[i] = 1

        return infectStatus


class DownNetwork(Network):
    def __init__(self):
        super().__init__()

    def topic_spread(self, message: Message):
        #找到关注这个话题的博主节点
        infectStatus = self.topic_input(message,initialNode)
        status1 = copy.deepcopy(infectStatus)
        status2 = copy.deepcopy(infectStatus)
        connection = copy.deepcopy(self.adjMatrix)
        nodes = len(connection)
        if sum(infectStatus) < nodes/2:  # 当感染节点数小于总数的一半时
            for i in range(len(status1)):  # 遍历所有节点，发现感染者
                if status1[i] == 1:  # 若状态为1，即为感染
                    for j in range(len(connection[i])):
                        if status1[j] == 0 and connection[i][j] == 1:  # 若连结关系为1，即为连结
                            if random.random() <= 0.1:  # 若生成的随机数小于Beta则登记为感染
                                status2[j] = 1  # i感染j

        else:
            for i in range(len(status1)):
                if status1[i] == 0:
                    for j in range(len(connection[i])):
                        if status1[j] == 1 and connection[i][j] == 1:
                            if random.random() <= 0.1:
                                status2[i] = 1
        return status2  # 返回新的感染者列表

    def update_nodeList(self):
        for i in self.nodes:
            i.calculate_influence()
            

class UpNetwork(Network):
    def __init__(self):
        super().__init__()

    def cooperate(self):
        pass

    pass
