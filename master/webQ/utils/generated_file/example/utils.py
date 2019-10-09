
def parestree(lis):
    l = []
    entities = {d['id']: {'id': d['id'], 'pid': d['pid'], 'label': d['name'], 'isresource': d.get('isresource'),'metaclsno': d.get('metaclsno'),'columnname': d.get('columnname')} for d in lis}

    for e_id in entities:
        entitiy = entities[e_id]
        fid = entitiy['pid']
        if fid == '-1':
            l.append(entitiy)
        else:
            entities[fid].setdefault('children', []).append(entitiy)
    return l


def parescolumntree(lis):
    l = []
    entities = {d['id']: {'id': d['id'], 'pid': d['pid'], 'label': d['name'], 'isresource': d.get('isresource'),'columnname': d.get('columnname'),'columntype': d.get('columntype'),'columnlen': d.get('columnlen')} for d in lis}
    for e_id in entities:
        entitiy = entities[e_id]
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