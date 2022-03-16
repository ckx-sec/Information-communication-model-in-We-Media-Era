from __future__ import annotations
import functools
import time
from typing import List
import node
import jieba
import numpy as np


class Message:
    def __init__(self, writer: node.Node, content: str):
        self.likes = 0
        self.forwards = 0
        self.comments = 0
        self.writer = writer
        self.content = content
        self.timestamp = time.time()

    @functools.lru_cache
    def getClassification(self):
        MAX_SEQUENCE_LENGTH = 100 # 每条新闻最大长度
        EMBEDDING_DIM = 200 # 词向量空间维度
        TEST_SPLIT = 0.2 # 测试集比例

        train_texts = open('train_contents.txt',encoding='utf8').read().split('\n') # 17600,xxx
        print(len(train_texts[0]))
        train_labels = open('train_labels.txt',encoding='utf8').read().split('\n')
        test_texts = open('test_contents.txt',encoding='utf8').read().split('\n')
        test_labels = open('test_labels.txt',encoding='utf8').read().split('\n')
        all_text = train_texts + test_texts

        from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
        count_v0= CountVectorizer()
        counts_all = count_v0.fit_transform(all_text)
        count_v1= CountVectorizer(vocabulary=count_v0.vocabulary_)
        # print(type(train_texts[0]))
        counts_train = count_v1.fit_transform(train_texts)#17600,xxx
        count_v2 = CountVectorizer(vocabulary=count_v0.vocabulary_)
  
        tfidftransformer = TfidfTransformer()
        train_data = tfidftransformer.fit(counts_train).transform(counts_train)

        x_train = train_data #(17600, 62418)
        # print("train\n")
        # print(type(train_data[0]))
        y_train = train_labels

        from sklearn.naive_bayes import MultinomialNB
        from sklearn import metrics
        clf = MultinomialNB(alpha = 0.01)
        clf.fit(x_train, y_train)
        
        wei = []
        word = is_ustr(self.content) # 1,xxx
        words = jieba_main(word)
        for i in words:
            wei.append(i)
        garbage = yy_stpword()
        wei = list(filter(lambda x: x not in garbage and x != ' ', wei)) # 49
        
        result = " ".join(wei)
        #print(result)
        counts_test = count_v2.fit_transform([result]) # 1,62418
        tfidftransformer2 = TfidfTransformer()
        test_data = tfidftransformer2.fit(counts_test).transform(counts_test)
        print("test\n")
        print(test_data.shape)
        preds = clf.predict(test_data)
        print(preds[0])
        return preds[0]
# 除去非中文部分
def is_ustr(in_str):
    out_str = ''
    for i in range(len(in_str)):
        if is_uchar(in_str[i]):
            out_str = out_str+in_str[i]
    return out_str


def is_uchar(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

# jieba中文分词
def jieba_main(out_str):
    cut_str = jieba.cut(out_str)
    return list(cut_str)

# 引用停用词
def yy_stpword():
    stpwrdpath = "./stop_words.txt"  # 停用词文本路径
    lines = open(stpwrdpath, encoding='utf-8').readlines()
    return list(map(lambda x: x.strip(), lines))
