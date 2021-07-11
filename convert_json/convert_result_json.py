import json
import random
import math


class Point:
    id = 0
    name = ''
    lng = 0
    lat = 0

    def __init__(self, _id, _name='', _lng=0, _lat=0):
        self.id = _id
        self.name = _name
        self.lng = _lng
        self.lat = _lat

    def __str__(self):
        return str(self.id) + " " + self.name + " " + str(self.lng) + " " + str(self.lat)


f_cn_city = open('cities_cn.json', encoding='utf-8')
all_city_cn = json.load(f_cn_city)

f_world_city = open('cities_world.json', encoding='utf-8')
all_city_world = json.load(f_world_city)
all_city_world_list_all = list(all_city_world)
all_city_world_list = []
for i in range(50):
    all_city_world_list.append(random.choice(all_city_world_list_all))


def generate_random_gps(base_log=None, base_lat=None, radius=None):
    # https://blog.csdn.net/weixin_41822224/article/details/91432154
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)
    longitude = y + base_log
    latitude = x + base_lat
    # 这里是想保留4位小数
    re_lng = '%.4f' % longitude
    re_lat = '%.4f' % latitude
    return re_lng, re_lat


def get_random_city_cn():
    # https://www.jianshu.com/p/2a8f965d5dee

    province = random.choice(list(all_city_cn.keys()))  # 随机选取一个省份
    city = random.choice(list(all_city_cn[province]))  # 在该省下随机选取一个城市
    # print(province, city, all_cities[province][city])
    return all_city_cn[province][city]


def get_random_city_world():
    city = random.choice(all_city_world_list)
    return float(city["lng"]), float(city["lat"])


if __name__ == '__main__':
    # 这个Map只作为去重用的，key就是点的id，注意key并不是从0开始连续的值，value就是点的信息
    pointsMapForDeDuplication = {}

    # 做一个 id - 连续值 的 mapper id2idxMapper
    id2idxMapper = {}

    # 做成点的list，方便等会json化
    pointsList = []

    # 做一个真的Map，key是从 0 开始连续的，value是point信息
    pointsMap = {}

    with open('./paths1.json') as f:
        json_str = f.read()
        data = json.loads(json_str)

        cnt = 0
        cnt_turn = 0
        # 遍历一遍，先获取所有的点信息
        for eachTurn in data:
            cnt_turn = cnt_turn + 1
            # print(keys)

            # print(eachTurn)
            # 获取这个turn里面所有的key信息
            keys = list(eachTurn.keys())
            for k in keys:
                # lng, lat = get_random_city_cn()
                lng, lat = get_random_city_world()
                longitude_, latitude_ = generate_random_gps(base_log=lng, base_lat=lat, radius=10000)
                P = (k, '', '', longitude_, latitude_)
                if pointsMapForDeDuplication.get(k) is None:
                    pointsMapForDeDuplication[k] = P
                    pointsList.append(P)
                    id2idxMapper[k] = cnt
                    pointsMap[cnt] = P
                    cnt = cnt + 1

                for e in eachTurn[k]:
                    e = str(e)
                    lng, lat = get_random_city_world()
                    longitude_, latitude_ = generate_random_gps(base_log=lng, base_lat=lat, radius=10000)
                    # print(e)
                    if pointsMapForDeDuplication.get(e) is None:
                        P = (e, '', '', longitude_, latitude_)
                        pointsMapForDeDuplication[e] = P
                        pointsList.append(P)
                        id2idxMapper[e] = cnt
                        pointsMap[cnt] = P
                        cnt = cnt + 1
            # eachTurn = data[0][list(data[0].keys())[0]]  # 起始点的list
            # for e in eachTurn:
            # print(startPointList)

            # pointsList.append(Point(e, '', longitude_, latitude_))

        # get_random_city()

        # for i in
        # pointList.append()
        print("TURNS: " + str(cnt_turn))

        routes = []
        turn_cnt = 0
        for eachTurn in data:
            # 获取这个turn里面所有的key信息
            # 这些key也就是起始点的id
            keys = list(eachTurn.keys())
            for src_id in keys:
                src_index = id2idxMapper.get(str(src_id))
                if src_index is None:
                    print(str(src_index) + ' Wrong')
                else:
                    for dest_id in eachTurn[src_id]:
                        dest_index = id2idxMapper.get(str(dest_id))
                        if dest_index is None:
                            print(str(dest_index) + ' Wrong')
                        else:
                            routes.append([turn_cnt, src_index, dest_index])
            turn_cnt = turn_cnt + 1
        print(len(routes))
        # f = open('routes.json', 'w')
        # f.write(json.dumps(routes))

        print(len(pointsMapForDeDuplication))
        # json_str = json.dumps(pointsMapForDeDuplication)
        # fo = open('pointsMapForDeDuplication.json', 'w')
        # fo.write(json_str)

        # print(pointsMap.popitem())

        # for i in pointsMapForDeDuplication.items():
        #     pointsList.append((str(i[0]), '', '', i[1][2], i[1][3]))
        # pointsList = list(pointsMap)
        print(len(pointsList))
        # json_str = json.dumps(pointsList)
        # fo = open('pointsList.json', 'w')
        # fo.write(json_str)
        print(pointsList[1])

        # cnt = 0
        # for i in pointsList:
        #     pointsMap[cnt] = i
        #     cnt = cnt + 1
        print(len(pointsMap))
        # json_str = json.dumps(pointsMap)
        # fo = open('pointsMap.json', 'w')
        # fo.write(json_str)

        print(len(id2idxMapper))
        # json_str = json.dumps(id2idxMapper)
        # fo = open('id2idxMapper.json', 'w')
        # fo.write(json_str)

        # 构造出轮数
        airlines = []
        for i in range(cnt_turn):
            airlines.append(['第' + str(i + 1) + '轮', ''])

        result = {'airports': pointsList,
                  'routes': routes,
                  'airlines': airlines}
        fo = open('result_v2.json', 'w', encoding='utf-8')
        fo.write(json.dumps(result))

        print(result['airlines'])
