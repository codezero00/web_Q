'''
url
'''

urlpatterns = [('GET', '/',  'view.index'),
               ('GET', '/1', 'view.index1'),
               ('GET', '/2/{gid}/', 'view.index2'),
               ('GET', '/3', 'view.index3'),
               ('GET', '/4', 'view.index4'),
               ('GET', '/5', 'view.index5'),
               ('GET', '/6', 'view.index6'),
               ('GET', '/7', 'view.index7')
               ]
