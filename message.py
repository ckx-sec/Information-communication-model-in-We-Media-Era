from __future__ import annotations
import time
from typing import List
import node


class Message:
    def __init__(self, writer: node.Node, content: str, topicList: List[str]):
        self.likes = 0
        self.forwards = 0
        self.comments = 0
        self.writer = writer
        self.content = content
        self.topicList = topicList
        self.timestamp = time.time()

    def getClassification(self) -> List[str]:

        return self.topicList
