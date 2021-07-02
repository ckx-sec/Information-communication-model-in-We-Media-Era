import jieba
import jieba.analyse
import tqdm
import os

topK = 30

files = os.listdir()
dir = os.getcwd()
# for file in tqdm.tqdm(files):
for file in files:
    try:
        if file.endswith(".txt"):
            name = dir + "\\" + file

            content = open(name, 'rb')
            tags = jieba.analyse.extract_tags(content.read(), topK=topK)
            content.close()
            s = "".join(tags)

            f = open(dir+"\\keyword\\"+file, 'w')
            print(dir+"\\keyword\\"+file)
            f.write(s)
            f.close()

    except Exception as e:
        print(e)
