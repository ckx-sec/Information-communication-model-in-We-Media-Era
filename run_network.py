import json
import random
import time
from network import Network, typeList
from message import Message
import pickle
import os

msg = Message(None, '''当地时间15日，俄罗斯国家杜马副主席彼得·托尔斯泰在社交媒体表示，俄罗斯决定退出欧洲委员会，俄外长拉夫罗夫的有关信件已交给该组织秘书长。
托尔斯泰说，破坏与欧洲委员会对话的全部责任在于北约国家，他们一直以人权为主题来实现自己的地缘政治利益和对俄罗斯的攻击。鉴于俄罗斯面临前所未有的政治和制裁压力，故不打算继续向该组织缴纳会费。
托尔斯泰强调，俄罗斯是自愿离开欧洲委员会的，这是一个平衡和深思熟虑的决定。''',
              random.choices(typeList, k=random.randint(2, 9)))

n = Network()
n.generate_network()
n.init_step(msg)
paths = []
for _ in range(5):
    paths.append(dict(n.get_paths()))
    print(len(tuple(map(lambda x: x.pid, n.get_fresh_nodes()))), end=' ')
    print(len(tuple(map(lambda x: x.pid, n.get_pending_nodes()))), end=' ')
    print(len(tuple(map(lambda x: x.pid, n.get_passed_nodes()))), end=' ')
    print(len(tuple(map(lambda x: x.pid, n.get_terminated_nodes()))), end=' ')
    print()
    n.step()
    # print(dict(n.get_paths()))

paths.append(dict(n.get_paths()))
json.dump(paths, open('paths_v2.json', 'w'))
