'''
TEST
'''

LISTA = [
    [0, -1, 'name0', 0],
    [1, 0, 'name1', 1],
    [2, 0, 'name2', 1],
    [3, 0, 'name3', 1],
    [4, 1, 'name4', 2],
    [5, 1, 'name5', 2],
    [6, 1, 'name6', 2],
    [7, 2, 'name7', 2],
    [8, 2, 'name8', 2],
    [9, 3, 'name9', 2],
    [10, 3, 'name10', 2],
    [11, 3, 'name11', 2],
    [12, 4, 'name12', 3],
    [13, 8, 'name12', 3]
]


def df1(list1):
    n = 0
    y = []
    res = [{'id': x[0], 'label': x[1], 'children': y.append(x)} for x in list1 if x[1] in list]
    n += 1
    print(res)
    return df1


def df2(list1):
    n = -1
    while True:
        res = [{'id': x[0], 'label': x[1]} for x in list1 if x[3] == n]
        n += 1
        print(res)
        if n > 3:
            break


def df3(list1):
    res = map(lambda x: x[2], list1)
    print(list(res))


def dfok(x, y, n):
    '''
    id 不为 pid的则是叶子节点
    :param x: id
    :param y: pid
    :return:
    '''
    n += 1
    print(n)
    if x not in y:
        return None
    return dfok(x[n - 1], y, n)


def df4(list1):
    res = map(lambda x: x[1], list1)
    # print(list(res))
    res1 = list(res)
    print(res1)
    mm = []
    for x in list1:
        if x[0] not in res1:
            break
        mm.append({'id': x[0], 'label': x[2]})
        print('mm:{}'.format(mm))
        df4(list1)


LISTb = [
    [0, -1, 'name0', 0],
    [1, 0, 'name1', 1],
    [2, 0, 'name2', 1],
    [3, 0, 'name3', 1],
    [4, 1, 'name4', 2],
    [5, 1, 'name5', 2],
    [6, 1, 'name6', 2],
    [7, 2, 'name7', 2],
    [8, 2, 'name8', 2],
    [9, 3, 'name9', 2],
    [10, 3, 'name10', 2],
    [11, 3, 'name11', 2],
    [12, 4, 'name12', 3],
    [13, 8, 'name12', 3]
]
res = map(lambda x: x[1], LISTb)
res1 = list(res)


def df5(list1, res1):
    for x in list1:
        if x[0] in res1:
            df5()


# import json
# jsons = {
#     "b":{
#         "a":[
#             {
#                 "n1":"WIFI",
#                 "lo":116.30744414106923,
#                 "t2":"1387873418.195T+08:00",
#                 "t3":"target_首页-海报视频点击",
#                 "p1":"com.tudou.ui.activity.HomeActivity",
#                 "n2":840,
#                 "la":39.98049465154441
#             },
#             {
#                 "n1":"WIFI",
#                 "lo":116.30744414106923,
#                 "t2":"1387873415.880T+08:00",
#                 "t1":"A1005",
#                 "s1":"5da19f89080af666bc2cb8d8775706df",
#                 "p1":"com.tudou.ui.activity.HomeActivity"
#             }
#         ]
#     },
#     "h":{
#         "i":{
#             "o2":"4.3",
#             "o1":"Android",
#             "b2":"Nexus 7",
#             "m":"10:bf:48:c2:81:f5",
#             "h":1205,
#             "w":800,
#             "u":"f835c7f8-c331-4b47-a6a3-772021544aa9",
#             "b1":"google"
#         }
#     }
# }
#
# js2 = {
#         "i":{
#             "o2":"4.3",
#             "o1":"Android",
#             "b2":"Nexus 7",
#             "m":"10:bf:48:c2:81:f5",
#             "h":1205,
#             "w":800,
#             "u":"f835c7f8-c331-4b47-a6a3-772021544aa9",
#             "b1":"google"
#         }
#     }
#
# def parse(js):
#     for key in js.keys():
#         if isinstance(js.get(key),dict):
#             parse(js.get(key))
#         elif isinstance(js.get(key),list):
#             parse(js.get(key))
#         else:
#             print('key:%s->value:%s'%(key,js.get(key)))
#
#
#
# parse(js2)

list = [
    {'id': 1, 'title': 't1', 'parent_id': 0},
    {'id': 2, 'title': 't2', 'parent_id': 0},
    {'id': 3, 'title': 't1_1', 'parent_id': 1},
    {'id': 4, 'title': 't1_2', 'parent_id': 1},
    {'id': 5, 'title': 't1_2_1', 'parent_id': 4},
    {'id': 6, 'title': 't2_1', 'parent_id': 2},
]


def printList(parentId, tree, spaceStr=''):
    for x in tree:
        if x['parent_id'] == parentId:
            print(spaceStr, x['title'], sep='')
            printList(x['id'], tree, spaceStr + '@')


# printList(0, list)

list2 = [
    {'ID': 0, 'PID': -1, 'NAME': 'name0', 'LEVEL': 0},
    {'ID': 1, 'PID': 0, 'NAME': 'name1', 'LEVEL': 1},
    {'ID': 2, 'PID': 0, 'NAME': 'name2', 'LEVEL': 1},
    {'ID': 3, 'PID': 0, 'NAME': 'name3', 'LEVEL': 1},
    {'ID': 4, 'PID': 1, 'NAME': 'name4', 'LEVEL': 2},
    {'ID': 5, 'PID': 1, 'NAME': 'name5', 'LEVEL': 2},
    {'ID': 6, 'PID': 1, 'NAME': 'name6', 'LEVEL': 2},
    {'ID': 7, 'PID': 2, 'NAME': 'name7', 'LEVEL': 2},
    {'ID': 8, 'PID': 2, 'NAME': 'name8', 'LEVEL': 2},
    {'ID': 9, 'PID': 3, 'NAME': 'name9', 'LEVEL': 2},
    {'ID': 10, 'PID': 3, 'NAME': 'name10', 'LEVEL': 2},
    {'ID': 11, 'PID': 3, 'NAME': 'name11', 'LEVEL': 2},
    {'ID': 12, 'PID': 4, 'NAME': 'name12', 'LEVEL': 3},
    {'ID': 13, 'PID': 8, 'NAME': 'name12', 'LEVEL': 3},
]


def printList2(parentId, tree, spaceStr=''):
    y = ''
    for x in tree:
        if x['PID'] == parentId:
            # print(spaceStr, x['NAME'], sep='')
            # y +={'id': x['ID'], 'label': x['NAME'], 'pid': x['PID']})
            y += """id:{},name:{},pid:{}""".format(x['ID'], x['NAME'], x['PID'])
            print(y)
            # print(spaceStr, 'id:{},label:{}'.format(x['ID'], x['NAME']))
            printList2(x['ID'], tree, spaceStr + '@')


# printList2(-1, list2)


class Tree(object):
    def __init__(self):
        # self.treelist = []
        self.res = []
        self.y = ''

    def printList2(self, parentId, tree, spaceStr=''):
        for x in tree:
            if x['PID'] == parentId:
                self.y += """id:{},name:{},pid:{}""".format(x['ID'], x['NAME'], x['PID'])
                printList2(x['ID'], tree, spaceStr + '@')

    def pprint(self):
        print(self.y)


mytree = Tree()
mytree.printList2(-1, list2)
mytree.pprint()