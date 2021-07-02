import os
import shutil
import jieba
import pdb


def main():
    path = './keyword' # 需要进行文本分类的文本的文件夹路径
    wei = [] # 空数组
    listdir = os.listdir(path) # 列出文件夹下的文件名
    length = len(listdir) # 长度
    for i in listdir:
        begin_path = path + '/' + i
        # 读取文件并且除去非文本部分，分词
        with open(begin_path) as f:
            word = f.read()
            word = is_ustr(word)
            words = jieba_main(word)
            for i in words:
                wei.append(i)
    print(wei)
    tfs = tf(wei)  # 将文本向量化，TF-IDF和标准化
    print(tfs)
    kms = km(tfs)    # K--means聚类算法聚类  
    for i in range(length):
        fenlei(listdir[i],kms[i])

#除去非中文部分
def is_ustr(in_str):
    out_str=''
    for i in range(len(in_str)):
        if is_uchar(in_str[i]):
            out_str=out_str+in_str[i]
        else:
            out_str=out_str+' '
    return out_str

def is_uchar(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

# jieba中文分词
def jieba_main(out_str):
    cut_str = jieba.cut(out_str)
    # cut_str = ' '.join(cut_str)
    return list(cut_str)


# 进行向量化，TF-IDF处理和标准化一步到位
from sklearn.feature_extraction.text import TfidfVectorizer
# 传入我们上面return的wei数组
def tf(wei):
    vector = TfidfVectorizer(stop_words = yy_stpword()) # 引用停用词
    tfidf = vector.fit_transform(wei) #
    d = tfidf.toarray()
    return d

# 引用停用词
def yy_stpword():
    stpwrdpath = "./stop_words/stop_words.txt" # 停用词文本路径
    with open(stpwrdpath, 'rb') as f:
        stpwrd_content = f.read()
    # 将停用词表转换为list  
        stpwrdlst = stpwrd_content.splitlines()
    return stpwrdlst


# K-means 算法聚类
from sklearn.cluster import KMeans as KM
def km(d):
    k = 10 # 将所有文本分成4类
    clf = KM(k)
    kmns = clf.fit_predict(d)
    return kmns

# 处理分类结果
def fenlei(numb,ga):

    path = '.'
    begin_path = path + '/keyword/' + numb
    paths = './' + str(ga) 
    folder = os.path.exists(paths)
    if folder:
        path_d = paths + '/' + str(numb) 
        shutil.move(begin_path,path_d)
    else:
        os.makedirs(paths)
        path_d = paths + '/' + str(numb) 
        shutil.move(begin_path,path_d)


if __name__ == '__main__':
    main()

