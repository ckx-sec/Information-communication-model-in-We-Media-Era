# social_network_model

basic one is already done

## 使用方法
运行`run_network.py`,得到`paths_v2.json`  
其中包含消息的传播路径信息  
然后使用`convert_json.py`转换之，得到`result.json`  
将`result.json`放进web目录

## 关于 web 文件夹

这个文件夹为前端部分，目前直接运行一个简单的 live-server 打开 `lines.html` 即可

## 关于 convert_json 文件夹

这个文件夹里面的 `convert_result_json.py` 文件是用来把 `path1.json` 这种模型结果转换为前端可直接读取的 json 文件：`result.json`

## cache.json

处理过后的原始数据  
这个文件存在是因为直接用原始数据太慢了

## paths_v2.json

消息传播路径

## viewers.json bloggers.json

层间关系与跨层的关注关系


1 汽车
2 财经
3 IT
4 健康
5 体育
6 旅游
7 教育
8 军事
9 文化
10娱乐
11时尚
