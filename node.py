from __future__ import annotations
from abc import abstractmethod
from message import Message
from enum import Enum


class NodeStatus(Enum):
    '''fresh:还没有接收到消息\n
    pending:刚接收到消息，还没决定传不传出去\n
    passed:接收到消息，感兴趣，将其传了出去\n
    terminated:接收到了消息，不感兴趣，不继续传播\n'''
    fresh = 0  # 还没有接收到消息
    pending = 1  # 刚接收到消息，还没看
    passed = 2  # 接收到消息，感兴趣，将其传了出去
    terminated = 3  # 接收到了消息，不感兴趣，不继续传播


class Node:
    def __init__(self, pid):
        self.pid = pid
        self.relationList = []  # 社会关系列表

        self.totalThumb = 0  # 总点赞数
        self.totalComments = 0  # 总评论数
        self.totalForwarding = 0  # 总转发数

        self.influence = 0  # 影响力
        self.receiveList = []  # 接收的文章列表
        self.articles = []  # 自己发布的原创性文章
        self.interest: dict = {}
        self.status: NodeStatus = NodeStatus.fresh

    # unused
    def build_relation(self, node: Node):
        self.relationList.append(node.pid)

    # TODO 完善这个或初始化Node的几个值
    def calculate_influence(self) -> float:
        self.influence = self.totalForwarding + \
            pow(self.totalComments, 1/2) + pow(self.totalThumb, 1/3)
        return self.influence

    @abstractmethod
    def follow(self, node: Blogger):
        pass

    def interested_in(self, message: Message) -> bool:
        topicList = message.getClassification()

        # 爱好程度
        hobby_degree = sum(
            map(lambda x: self.interest[x], topicList))/len(topicList)
        if hobby_degree > 0.5:
            if hobby_degree > 0.8:
                self.follow(message.writer)
            return True
        else:
            return False

    def sendMessage(self, message: Message, node: Node):
        self.status = NodeStatus.passed
        node.receiveList.append(message)
        if node.status == NodeStatus.fresh:
            # 收到消息的节点留到下一轮处理
            node.status = NodeStatus.pending
        # 不处理接受过消息的节点

    def forwardMessage(self, message: Message):
        message.forwards += 1
        message.writer.totalForwarding += 1
        for i in self.relationList:
            self.sendMessage(message, i)

    # unused
    def likeMessage(self, message: Message):
        message.likes += 1
        message.writer.totalThumb += 1

    # unused
    def commentMessage(self, message: Message):
        message.comments += 1
        message.writer.totalComments += 1


class Viewer(Node):
    def __init__(self):
        super().__init__()
        self.following: list[Node] = []  # 关注了谁

    def follow(self, node: Blogger):
        self.following.append(node)
        node.follower.append(self)

    def forwardMessage(self, message: Message):
        message.forwards += 1
        for i in self.relationList:
            self.sendMessage(message, i)

    """
    @classmethod
    def from_node(cls, node: Node) -> Viewer:
        viewer=Viewer()
        viewer.pid = node.pid
        viewer.relationList = []  # 社会关系列表

        viewer.totalThumb = 0  # 总点赞数
        viewer.totalComments = 0  # 总评论数
        viewer.totalForwarding = 0  # 总转发数

        viewer.influence = 0  # 影响力
        viewer.receiveList = []  # 接收的文章列表
        viewer.articles = []  # 自己发布的原创性文章
        viewer.interest: dict = {}
        viewer.status: NodeStatus = NodeStatus.fresh

        pass
    """
    # unused

    def releaseMessage(self, content: str):

        message = Message(self, content)
        self.articles.append(message)
        for i in self.relationList:
            self.sendMessage(message, i)


class Blogger(Viewer):
    def __init__(self):
        super().__init__()
        self.follower: list[Node] = []  # 谁关注了我

    def forwardMessage(self, message: Message):
        message.forwards += 1
        for i in self.relationList:
            self.sendMessage(message, i)
        for i in self.follower:
            self.sendMessage(message, i)

    # unused
    def releaseMessage(self, content: str):
        message = Message(self, content)
        self.articles.append(message)
        for i in self.relationList:
            self.sendMessage(message, i)
        for i in self.follower:
            self.sendMessage(message, i)
