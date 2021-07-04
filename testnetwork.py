import json
import random
import time
from network import Network, typeList
from message import Message
import pickle
import os

msg = Message(None, 'sample content',
              random.choices(typeList, k=random.randint(2, 9)))
'''
if os.path.isfile('network'):
    n = pickle.load(open('network', 'rb'))
else:
    n = Network()
    n.generate_network()
    pickle.dump(n, open('network', 'wb'))
'''
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
json.dump(paths, open('paths.json', 'w'))
