import time
from __future__ import annotations
from node import Node
from typing import List


class Message:
    def __init__(self, writer: Node, content: str, topicList: List[str]):
        self.likes = 0
        self.forwards = 0
        self.comments = 0
        self.writer = writer
        self.content = content
        self.topicList = topicList
        self.timestamp = time.time()

    def getClassification(self) -> List[str]:

        return self.topicList
