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

    def getClassification(self):
        MAX_SEQUENCE_LENGTH = 100 # 每条新闻最大长度
        EMBEDDING_DIM = 200 # 词向量空间维度
        TEST_SPLIT = 0.2 # 测试集比例

        train_texts = open('train_contents.txt').read().split('\n')
        train_labels = open('train_labels.txt').read().split('\n')
        test_texts = open('test_contents.txt').read().split('\n')
        test_labels = open('test_labels.txt').read().split('\n')
        all_text = train_texts + test_texts

        from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
        count_v0= CountVectorizer()
        counts_all = count_v0.fit_transform(all_text)
        count_v1= CountVectorizer(vocabulary=count_v0.vocabulary_)
        counts_train = count_v1.fit_transform(train_texts)
        count_v2 = CountVectorizer(vocabulary=count_v0.vocabulary_)
  
        tfidftransformer = TfidfTransformer()
        train_data = tfidftransformer.fit(counts_train).transform(counts_train)

        x_train = train_data
        y_train = train_labels

        from sklearn.naive_bayes import MultinomialNB
        from sklearn import metrics
        clf = MultinomialNB(alpha = 0.01)
        clf.fit(x_train, y_train)
        
        wei = []
        word = is_ustr(self.content)
        words = jieba_main(word)
        for i in words:
            wei.append(i)
        garbage = yy_stpword()
        wei = list(filter(lambda x: x not in garbage and x != ' ', wei))
        preds = clf.predict(wei)

        return preds
