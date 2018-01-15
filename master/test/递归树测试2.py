class Tree(object):
    def __init__(self):
        # self.treelist = []
        self.res = []
        self.y = dict()
        # self.lis = list()

    def printList2(self, parentId, tree, spaceStr=''):
        lis = list()
        print(self.y)
        for x in tree:
            if x['PID'] == parentId:
                if x['LEVEL'] == 3:
                    self.y = {'id': x['ID'], 'label': x['NAME'], 'pid': x['PID']}
                else:
                    lis.append({'id': x['ID'], 'label': x['NAME'], 'pid': x['PID']})
                self.y['child'] = lis
                self.printList2(x['ID'], tree, spaceStr + '@')

    def pprint(self):
        print(self.y)


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

# mytree = Tree()
# mytree.printList2(-1, list2)
# mytree.pprint()

from pprint import pprint

t = (
    (1, -1, 'python'),
    (2, -1, 'ruby'),
    (3, -1, 'php'),
    (4, -1, 'lisp'),
    (5, 1, 'flask'),
    (6, 1, 'django'),
    (7, 1, 'webpy'),
    (8, 2, 'rails'),
    (9, 3, 'zend'),
    (10, 6, 'dblog')
)

# l = []
# entries = {}
#
# for id, fid, title in t:
#      entries[id] = entry = {'id': id, 'fid': fid, 'title': title}
#      if fid == -1:
#           l.append(entry)
#      else:
#           parent = entries[fid]
#           parent.setdefault('son', []).append(entry)
#
# pprint(entries)

# e, l = {d[0]: {'id': d[0], 'fid': d[1], 'title': d[2]} for d in t}, []
# pprint(e)
# for i in e:
#     #l.append(e[i]) if e[i]['fid'] == -1 else e[e[i]['fid']].setdefault('son', []).append(e[i])
#     if e[i]['fid'] == -1 :
#         l.append(e[i])
#     else:
#         e[e[i]['fid']].setdefault('son', []).append(e[i])
# pprint(l)


# pprint(l)

l = []
entities= {d[0]:{'id': d[0], 'fid': d[1], 'title': d[2]} for d in t}
pprint(entities)
print('#######################################')
for e_id in entities:
    # print(e_id)
    entitiy = entities[e_id]
    # print(entitiy)
    fid = entitiy['fid']
    if fid == -1:
        l.append(entitiy)
    else:
        entities[fid].setdefault('son',[]).append(entitiy)
pprint(l)
