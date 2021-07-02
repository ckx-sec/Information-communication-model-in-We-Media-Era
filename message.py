import time
from __future__ import annotations
from node import Node


class Message:
    def __init__(self, writer: Node, content):
        self.likes = 0
        self.forwards = 0
        self.comments = 0
        self.writer = writer
        self.content = content
        self.topicList: list = []
        self.timestamp = time.time()

    def getClassification(self):

        return self.topicList
