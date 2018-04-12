urlpatterns = [
    ('name1', 'GET', '/', 'view.index'),
    # ('name2', 'GET', '/1', 'view.index1'),
    # ('name3', 'GET', '/2/{gid}/', 'view.index2'),
    # ('name4', 'GET', '/3', 'view.index3'),
    # ('name5', 'GET', '/4', 'view.index4'),
    # ('name6', 'GET', '/5', 'view.index5'),
    # ('name7', 'GET', '/6', 'view.index6'),
    # ('name8', 'GET', '/7', 'view.index7'),
    # ('name9', 'GET', '/8', 'view.index8'),
    # ('name10', 'GET', '/90', 'view.index9'),
    # ('name11', 'POST', '/9', 'view.index90'),
    # ('name12', 'GET', '/10', 'view.index10'),
    # ('name13', 'POST', '/api/v1/11', 'view.index11'),
    # ('name14', 'GET', '/2', 'view.index12'),
    ('login', 'GET', '/api/v1/login', 'view.authenticate'),
    ('reg', 'GET', '/api/v1/reg', 'view.api_register_user'),
    ('islogin', 'GET', '/api/v1/userinfo', 'view.islogin'),
    ('metaclasstree', 'GET', '/api/v1/metaclasstree', 'view.metaclasstreeQuery'),
    ('metaclass', 'GET', '/api/v1/metaclass', 'view.metaclassQuery'),
    ('metadata', 'GET', '/api/v1/metadata', 'view.metadatadetailQuery'),
    ('FrontBase', 'GET', '/api/v1/FrontBase', 'view.FrontBaseQuery'),
    ('ResourceBase', 'GET', '/api/v1/ResourceBase', 'view.ResourceBaseQuery'),
    ('DataLayer', 'GET', '/api/v1/DataLayer', 'view.DataLayerQuery'),
    ('dbtabletree', 'GET', '/api/v1/dbtabletree', 'view.dbtabletreeQuery'),
    ('DBTableLayerTree', 'GET', '/api/v1/dbtablelayertree', 'view.DBTableLayerTreeQuery'),
    ('GetTable', 'GET', '/api/v1/GetTable', 'view.GetTableQuery'),
    ('dbtable', 'GET', '/api/v1/dbtable', 'view.dbtableQuery'),
    ('dbtablecolumn', 'GET', '/api/v1/dbtablecolumn', 'view.dbtablecolumnQuery'),
    ('etlclients', 'GET', '/api/v1/etlclients', 'view.etlclientsQuery'),
    ('etljobs', 'GET', '/api/v1/etljobs', 'view.EtlJobsQuery'),
    ('ai', 'GET', '/api/v1/classforecast', 'view.ai'),

    # I U D
    ('FrontBaseInsOrUp', 'POST', '/api/v1/FrontBaseInsOrUp', 'view.FrontBaseInsOrUp'),


    #######


    ('ws', 'GET', '/api/v1/ws', 'view.websocket_handler'),
    ('ws2', 'GET', '/api/v1/ws2', 'view.websocket_handler_test1'),
    ('ws3', 'GET', '/api/v1/ws3', 'view.websocket_handler_test3'),
    ('ws4', 'GET', '/api/v1/ws4', 'view.wshandler'),
]
