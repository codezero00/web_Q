from pprint import pprint
#
# list2 = [
#     # {'ID': 0, 'PID': -1, 'NAME': 'name0', 'LEVEL': 0},
#     {'ID': 1, 'PID': -1, 'NAME': 'name1', 'LEVEL': 1},
#     {'ID': 2, 'PID': -1, 'NAME': 'name2', 'LEVEL': 1},
#     {'ID': 3, 'PID': -1, 'NAME': 'name3', 'LEVEL': 1},
#     {'ID': 4, 'PID': 1, 'NAME': 'name4', 'LEVEL': 2},
#     {'ID': 5, 'PID': 1, 'NAME': 'name5', 'LEVEL': 2},
#     {'ID': 6, 'PID': 1, 'NAME': 'name6', 'LEVEL': 2},
#     {'ID': 7, 'PID': 2, 'NAME': 'name7', 'LEVEL': 2},
#     {'ID': 8, 'PID': 2, 'NAME': 'name8', 'LEVEL': 2},
#     {'ID': 9, 'PID': 3, 'NAME': 'name9', 'LEVEL': 2},
#     {'ID': 10, 'PID': 3, 'NAME': 'name10', 'LEVEL': 2},
#     {'ID': 11, 'PID': 3, 'NAME': 'name11', 'LEVEL': 2},
#     {'ID': 12, 'PID': 4, 'NAME': 'name12', 'LEVEL': 3},
#     {'ID': 13, 'PID': 8, 'NAME': 'name12', 'LEVEL': 3},
# ]

# list2 = [{'ID': '1', 'PID': '-1', 'NAME': '运管局'}, {'ID': '2', 'PID': '-1', 'NAME': '港航局'}, {'ID': '3', 'PID': '-1', 'NAME': '公路局'}, {'ID': '4', 'PID': '2', 'NAME': '水运'}, {'ID': '5', 'PID': '4', 'NAME': '企业'}, {'ID': '6', 'PID': '5', 'NAME': '水运企业信息'}]


def parestree(lis):
    l = []
    entities = {d['ID']: {'id': d['ID'], 'pid': d['PID'], 'label': d['NAME'], 'isresource': d.get('ISRESOURCE'),'metaclsno': d.get('METACLSNO'),'columnname': d.get('COLUMNNAME')} for d in lis}
    # pprint(entities)
    for e_id in entities:
        #print(e_id)
        entitiy = entities[e_id]
        #print(entitiy)
        fid = entitiy['pid']
        if fid == '-1':
            l.append(entitiy)
        else:
            entities[fid].setdefault('children', []).append(entitiy)
    return l

# x = parestree(list2)
# #
# pprint(x)


def parescolumntree(lis):
    l = []
    entities = {d['ID']: {'id': d['ID'], 'pid': d['PID'], 'label': d['NAME'], 'isresource': d.get('ISRESOURCE'),'columnname': d.get('COLUMNNAME'),'columntype': d.get('COLUMNTYPE'),'columnlen': d.get('COLUMNLEN')} for d in lis}
    # pprint(entities)
    for e_id in entities:
        #print(e_id)
        entitiy = entities[e_id]
        #print(entitiy)
        fid = entitiy['pid']
        if fid == '-1':
            l.append(entitiy)
        else:
            entities[fid].setdefault('children', []).append(entitiy)
    return l


def parescasetypetree(lis):
    l = []
    entities = {d['id']: {'id': d['id'], 'pid': d['pid'], 'label': d['dictname'], 'dictcode': d.get('dictcode'), 'accuracy': d.get('accuracy')} for d in lis}
    for e_id in entities:
        entitiy = entities[e_id]
        fid = entitiy['pid']
        if fid == '-1':
            l.append(entitiy)
        else:
            entities[fid].setdefault('children', []).append(entitiy)
    return l