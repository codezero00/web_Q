mongodb gridfs 静态文件存储接口

('UploadFile', 'POST', '/api/v1/UploadFile', 'view.UploadFile'), # 上传文件
('GetImage', 'GET', '/api/v1/GetImage', 'view.GetImage'), # 获取图片
('GetFile', 'GET', '/api/v1/GetFile', 'view.GetFile'), # 获取文件
('NosqlQuery', 'GET', '/api/v1/NosqlQuery', 'view.NosqlQuery'), # 查询记录


motor == 2.0.0
pymongo == 3.7.1