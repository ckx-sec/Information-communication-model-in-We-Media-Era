from __future__ import annotations
import itertools
import os
import json
import random
import numpy as np
from message import *
from node import *
from typing import Tuple, List, Union
from itertools import repeat

nodes: dict = {}


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

    if not os.path.isfile('crap.json'):

        f = open("nodes", "r", encoding="utf-8").readlines()
        node_ids = map(lambda x: int(x.split(',')[-1]), f)
        f1 = open("edges", "r", encoding="utf-8").readlines()
        edges = list(map(
            lambda x: tuple(
                map(lambda y: int(y), x.split(','))),
            f1))

        ret: list[tuple[int, list[int]]] = []
        for id in node_ids:
            relation_ids = []
            i = 0
            edges_len = len(edges)
            while i < edges_len:
                edge = edges[i]
                i += 1
                if edge[0] == id:
                    relation_ids.append(edge[1])
                elif edge[1] == id:
                    relation_ids.append(edge[0])
                else:
                    continue
                edges.pop(i-1)
                edges_len -= 1
            ret.append((id, list(relation_ids)))

        open('crap.json', 'w').write(json.dumps(ret))

    else:
        ret = json.loads(open('crap.json').read())

    ids = list(map(lambda x: x[0], ret))  # 所有id
    for i in range(len(ret)):
        to_remove = []
        # 遍历每个id的关系列表，剔除不存在的id
        for j in range(len(ret[i][1])):
            if ret[i][1][j] not in ids:
                to_remove.append(ret[i][1][j])
        for r in to_remove:
            ret[i][1].remove(r)

    ss = sorted(ret, key=lambda x: len(x[1]))
    json.dump(ss, open('crap_filtered.json', 'w'))
    up = ss[-34:]
    down = ss[:-34]
    # 返回(nodeid,(与node相连的节点id))
    return up, down


class Network:
    nodes = nodes

    def __init__(self):
        # self.nodes: dict = {}

        self.edges: List[Tuple[Node, Node]] = []
        self.adjMatrix = np.zeros(
            [len(self.nodes), len(self.nodes)], dtype=int)
        self.type: list = []
        self.paths: list[tuple[int, tuple[int]]] = []
        self.cur_message: Message = None

    def generate_network(self):

        # TODO 分开上下层的节点
        self.up, self.down = get_adj_matrix()

        # 初始化两类节点
        for id, _ in self.up:
            node = Blogger(id)
            node.interest = dict(map(lambda x: (x, random.random()), typeList))
            self.nodes[id] = node

        for id, _ in self.down:
            node = Viewer(id)
            node.interest = dict(map(lambda x: (x, random.random()), typeList))
            self.nodes[id] = node

        # 建立关系

        for id, relation in self.up+self.down:
            n: Node = self.nodes[id]
            n.relationList = relation
        '''
        for id, edges in self.up:
            s: Blogger = self.nodes[id]
            for eid in edges:
                u: Union[Viewer, Blogger] = self.nodes[eid]
                if isinstance(u, Blogger):
                    s.relationList.append(eid)
                else:
                    u.follow(s)

        for id, edges in self.down:
            s: Viewer = self.nodes[id]
            for eid in edges:
                u: Union[Viewer, Blogger] = self.nodes[eid]
                if isinstance(u, Blogger):
                    s.follow(u)
                else:
                    s.relationList.append(eid)
        '''

        i = 0
        # 建立关注与被关注的关系
        for d_id in map(lambda x: x[0], self.down):
            for u_id in map(lambda x: x[0], self.up):
                d: Viewer = self.nodes[d_id]
                u: Blogger = self.nodes[u_id]
                if d.interested_in_blogger(u):
                    d.follow(u)
                    i += 1

        return

        '''
        # TODO 改成不用influence区分上下层
        for id, edge in self.adjMatrix:
            tempnode = Node(id)
            node: Union[Viewer, Blogger] = None
            for n in edge:
                tempnode.relationList.append(n)

            # TODO? 初始化node的其他属性

            # TODO 找一个合适的阈值
            if tempnode.calculate_influence() < 0.01:
                node = Viewer(id)
            else:
                node = Blogger(id)
            node.relationList = tempnode.relationList
            node.interest = dict(map(lambda x: (x, random.random()), typeList))

            self.nodes[id] = node
        '''

        '''
        i = 0
        values = self.nodes.values()
        node: Union[Viewer, Blogger]
        for node in values:
            i += 1
            for id in node.relationList:
                if not self.nodes.get(id):
                    # 规避数据的坑
                    node.relationList.remove(id)
            if isinstance(node, Viewer):
                for u in random.choices(list(self.nodes.values()), k=random.randint(2, 1000)):
                    if isinstance(u, Blogger):
                        node.follow(u)
            else:
                for u in random.choices(list(self.nodes.values()), k=random.randint(2, 1000)):
                    if isinstance(u, Viewer):
                        u.follow(node)
        '''

    def addNode(self, node: Node):
        self.nodes[node.pid] = node

    def removeNode(self, node: Node):
        self.nodes.pop(node.pid)

    def init_step(self, message: Message):
        '''一个step就是运行一轮传播\n
        这是比较特殊的第一轮'''

        self.cur_message = message
        entry_nodes = list(filter(
            lambda x: x.interested_in(self.cur_message),
            self.nodes.values()))
        entry_nodes = random.choices(entry_nodes, k=random.randint(5, 10))
        message.writer = random.choice(entry_nodes)
        self.paths = [(-1, tuple(map(lambda x: x.pid, entry_nodes)))]
        for n in entry_nodes:
            n.status = NodeStatus.pending

    def step(self):
        '''一个step就是运行一轮传播'''
        node: Union[Viewer, Blogger]
        # pendings = []
        # for i in self.paths:
        #     pendings.extend(i[1])
        self.paths = []
        for node in list(self.nodes.values()):
            if node.status == NodeStatus.pending:
                # 处理状态为pending的节点
                if node.interested_in(self.cur_message):
                    dests = tuple(node.forwardMessage(self.cur_message))
                    self.paths.append((node.pid, dests))
                    node.status = NodeStatus.passed
                else:
                    node.status = NodeStatus.terminated

    def get_pending_nodes(self):
        return tuple(filter(lambda x: x.status == NodeStatus.pending, self.nodes.values()))

    def get_passed_nodes(self):
        return tuple(filter(lambda x: x.status == NodeStatus.passed, self.nodes.values()))

    def get_fresh_nodes(self):
        return tuple(filter(lambda x: x.status == NodeStatus.fresh, self.nodes.values()))

    def get_terminated_nodes(self):
        return tuple(filter(lambda x: x.status == NodeStatus.terminated, self.nodes.values()))

    def get_paths(self):
        return self.paths
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
