from __future__ import annotations
from typing import Tuple, List, Union
from node import *
from message import *
import copy
import numpy as np
import random
import networkx as nx

"""
把话题放进模型
从话题中提取特征点
找出对这几个特征感兴趣的节点，作为开始传播信息的节点

从这几个节点开始
传给与其有关系的节点
对上了兴趣就递归传播
对不上就不传播
"""

typeList: list[str] = ["sport", "fashion", "food", "tourism", "furniture", "history", "vehicle", "anime", "game",
                       "gossip", "geography", "language", "movie", "music", "photography", "finance", "technology", "news"]


def get_adj_matrix():
    f = open("nodes", "r", encoding="utf-8").readlines()
    edge = []
    node = []
    for i in f:
        i = i.split(',')
        node.append(i[-1].strip())
    f1 = open("edges", "r", encoding="utf-8").readlines()
    for i in f1:
        i = i.split(',')
        a = (int(i[0]), int(i[1].strip()))
        edge.append(a)

    G = nx.Graph()
    node_and_dict = []
    for i in node:
        node_and_dict.append(
            (int(i), dict(map(lambda x: (x, random.random()), typeList))))
    G.add_nodes_from(node_and_dict)
    G.add_edges_from(edge)
    return nx.adjacency_matrix(G).todense(out=np.ndarray)


class Network:
    def __init__(self):
        self.nodes: List[Node] = []

        self.edges: List[Tuple[Node, Node]] = []
        self.adjMatrix = np.zeros(
            [len(self.nodes), len(self.nodes)], dtype=int)
        self.type: list = []

        self.cur_message: Message = None

    def generate_network(self):
        self.adjMatrix = get_adj_matrix()
        for id in range(len(self.adjMatrix)):
            tempnode = Node(id)
            node: Union[Viewer, Blogger] = None
            for n in self.adjMatrix[id]:
                tempnode.relationList.append(n)

            # TODO? 初始化node的其他属性

            # TODO 找一个合适的阈值
            if tempnode.calculate_influence() < 0.1:
                node = Viewer()
            else:
                node = Blogger()
            node.relationList = tempnode.relationList
            node.interest = dict(map(lambda x: (x, random.random()), typeList))

            self.nodes.append(node)

        # 初始化关注与被关注的关系
        for node in self.nodes:
            if isinstance(node, Blogger):
                for n in filter(lambda x: x.pid in node.relationList, self.nodes):
                    if isinstance(n, Blogger):
                        node.follow(n)
                    else:
                        n.follow(node)
            else:
                for n in filter(lambda x: x.pid in node.relationList, self.nodes):
                    if isinstance(n, Blogger):
                        node.follow(n)

    def addNode(self, node: Node):
        self.nodes.append(node)

    def removeNode(self, node: Node):
        self.nodes.reverse(node)

    def init_step(self, message: Message):
        '''一个step就是运行一轮传播\n
        这是比较特殊的第一轮'''
        self.cur_message = message
        entry_nodes = filter(
            lambda x: x.interested_in(self.cur_message),
            self.nodes)
        for n in entry_nodes:
            n.status = NodeStatus.pending

    def step(self):
        '''一个step就是运行一轮传播'''
        for node in filter(lambda x: x.status == NodeStatus.pending, self.nodes):
            # 处理状态为pending的节点
            if node.interested_in(self.cur_message):
                node.forwardMessage(self.cur_message)
            else:
                node.status = NodeStatus.terminated

    '''
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
    '''


"""
class DownNetwork(Network):
    def __init__(self):
        super().__init__()
    '''

   def topic_spread(self, message: Message):
        # 找到关注这个话题的博主节点
        infectStatus = self.topic_input(message, initialNode)
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
    '''
    '''

    def update_nodeList(self):
        for i in self.nodes:
            i.calculate_influence()
    '''
"""
"""
class UpNetwork(Network):
    def __init__(self):
        super().__init__()

    def cooperate(self):
        pass

    pass
"""
