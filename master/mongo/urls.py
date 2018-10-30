urlpatterns = [

    # nosql
    ('helloworld', 'GET', '/', 'view.helloworld'),
    # ('testUploadFile', 'POST', '/api/v1/testUploadFile', 'view.testUploadFile'),
    ('UploadFile', 'POST', '/api/v1/UploadFile', 'view.UploadFile'),
    ('GetImage', 'GET', '/api/v1/GetImage', 'view.GetImage'),
    ('GetFile', 'GET', '/api/v1/GetFile', 'view.GetFile'),
    ('NosqlQuery', 'GET', '/api/v1/NosqlQuery', 'view.NosqlQuery'),
    #######

]
