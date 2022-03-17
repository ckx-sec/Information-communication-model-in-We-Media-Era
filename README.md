# social_network_model

basic one is already done

## 使用方法
运行`run_network.py`，得到`paths_v2.json`  
其中包含消息的传播路径信息  
然后使用`convert_json.py`转换之，得到`result.json`  
将`result.json` 重命名为`result_v2.json`，然后放进 /web/social-network-web/public 目录

## 关于 web 文件夹

这个文件夹为系统的web端运行部分

- 如果仅打算运行一个可视化部分的网页，那么直接在 /web/social-network-web/public 目录下启动一个 live-server，然后浏览器地址栏访问  `http://ip:port/lines.html`  即可（ip，port 视运行环境而定）
- 如果打算完整运行系统，则需要将前端，后端，MySQL 三个部分均运行起来
  - MySQL 端：新建 schema，命名为 `social_network` ，然后将 /web/social_network.sql 文件恢复到这个 schema 中即可
  - 后端：位于 /web/social-network-web-backend 路径下，是一个 SpringBoot 项目，注意将 `/web/social-network-web-backend/src/main/resources/application.yml`  配置文件中的数据源配置改为自己的（如用户名，密码等）
  - 前端：位于 /web/social-network-web 路径下，是一个 vue 项目，可参照其目录下的 README 来启动

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
