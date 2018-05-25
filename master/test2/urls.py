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

    #######


    ('ws', 'GET', '/api/v1/ws', 'view.websocket_handler'),
    ('ws2', 'GET', '/api/v1/ws2', 'view.websocket_handler_test1'),
    ('ws3', 'GET', '/api/v1/ws3', 'view.websocket_handler_test3'),
    ('ws4', 'GET', '/api/v1/ws4', 'view.wshandler'),


    ### ggg
    ('ginfo', 'GET', '/api/v1/ginfo', 'view.GetGInfo'),

]
