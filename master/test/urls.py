urlpatterns = [
    ('name1', 'GET', '/', 'view.index'),
    # ('name2', 'GET', '/1', 'view.index1'),
    ('name3', 'GET', '/2/{gid}/', 'view.index2'),
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
    ('dbtablecolumn2', 'GET', '/api/v1/dbtablecolumn2', 'view.dbtablecolumn2Query'),
    ('etlclients', 'GET', '/api/v1/etlclients', 'view.etlclientsQuery'),
    ('etljobs', 'GET', '/api/v1/etljobs', 'view.EtlJobsQuery'),
    ('EtlJobImage', 'GET', '/api/v1/EtlJobImage', 'view.EtlJobImage'),
    ('EtlJobLog', 'GET', '/api/v1/EtlJobLog', 'view.EtlJobLog'),

    ('BloodRelationQuery', 'GET', '/api/v1/BloodRelationQuery', 'view.BloodRelationQuery'),
    ('DBTableColumnTreeQuery', 'GET', '/api/v1/DBTableColumnTreeQuery', 'view.DBTableColumnTreeQuery'),
    ('BloodVertexEdgeQuery', 'GET', '/api/v1/BloodVertexEdgeQuery', 'view.BloodVertexEdgeQuery'),

    ('NosqlDatabaseQuery', 'GET', '/api/v1/NosqlDatabaseQuery', 'view.NosqlDatabaseQuery'),
    ('NosqlBaseTreeQuery', 'GET', '/api/v1/NosqlBaseTreeQuery', 'view.NosqlBaseTreeQuery'),

    ('MetaDataTreeQuery', 'GET', '/api/v1/MetaDataTreeQuery', 'view.MetaDataTreeQuery'),


    # AI
    ('ai', 'GET', '/api/v1/classforecast', 'view.ai'),
    ('Word2vecKeywords', 'GET', '/api/v1/Word2vecKeywords', 'view.Word2vecKeywords'),
    ('AIFaceCompare', 'GET', '/api/v1/AIFaceCompare', 'view.AIFaceCompare'),
    ('SourceUpload', 'POST', '/api/v1/SourceUpload', 'view.SourceUpload'),
    ('TargetUpload', 'POST', '/api/v1/TargetUpload', 'view.TargetUpload'),

    # I U D
    ('FrontBaseInsOrUp', 'POST', '/api/v1/FrontBaseInsOrUp', 'view.FrontBaseInsOrUp'),
    ('ResourceBaseInsOrUp', 'POST', '/api/v1/ResourceBaseInsOrUp', 'view.ResourceBaseInsOrUp'),
    ('DataLayerInsOrUp', 'POST', '/api/v1/DataLayerInsOrUp', 'view.DataLayerInsOrUp'),
    ('DBTableInsOrUp', 'POST', '/api/v1/DBTableInsOrUp', 'view.DBTableInsOrUp'),
    ('ETLClientsInsOrUp', 'POST', '/api/v1/ETLClientsInsOrUp', 'view.ETLClientsInsOrUp'),
    ('BloodRrlationInsOrUp', 'POST', '/api/v1/BloodRrlationInsOrUp', 'view.BloodRrlationInsOrUp'),
    ('MetaDataClassInsOrUp', 'POST', '/api/v1/MetaDataClassInsOrUp', 'view.MetaDataClassInsOrUp'),
    ('MetaDataInsOrUp', 'POST', '/api/v1/MetaDataInsOrUp', 'view.MetaDataInsOrUp'),
    ('MetaDataDelete', 'POST', '/api/v1/MetaDataDelete', 'view.MetaDataDelete'),
    ('NosqlDatabaseInsOrUp', 'POST', '/api/v1/NosqlDatabaseInsOrUp', 'view.NosqlDatabaseInsOrUp'),
    ('DBTableColumnInsOrUp', 'POST', '/api/v1/DBTableColumnInsOrUp', 'view.DBTableColumnInsOrUp'),
    ('DBTableColumnBatchDel', 'POST', '/api/v1/DBTableColumnBatchDel', 'view.DBTableColumnBatchDel'),

    # nosql
    ('testUploadFile', 'POST', '/api/v1/testUploadFile', 'view.testUploadFile'),
    ('UploadFile', 'POST', '/api/v1/UploadFile', 'view.UploadFile'),
    ('GetImage', 'GET', '/api/v1/GetImage', 'view.GetImage'),
    ('NosqlQuery', 'GET', '/api/v1/NosqlQuery', 'view.NosqlQuery'),
    #######


    ('ws', 'GET', '/api/v1/ws', 'view.websocket_handler'),
    ('ws2', 'GET', '/api/v1/ws2', 'view.websocket_handler_test1'),
    ('ws3', 'GET', '/api/v1/ws3', 'view.websocket_handler_test3'),
    ('ws4', 'GET', '/api/v1/ws4', 'view.wshandler'),
]
