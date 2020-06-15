import json, time, hashlib, logging, model
from webQ.q_response import Response, render_json, render_image, render_file
from webQ.q_login import _COOKIE_NAME, encode_cookie
from webQ.q_helpers import _RE_EMAIL, _RE_SHA1, APIValueError, APIError, next_id, Page, ToMysqlDateTimeNow

from aiogfs import GFS


async def helloworld(request):
    return "helloworld!!"


# region login

async def authenticate(request):
    '''
    登陆模块
    :param request:
    :return:
    '''
    # data = await request.json()
    # email = data['email']
    # passwd = data['passwd']
    email = request.query.get('email')
    passwd = request.query.get('passwd')
    if not email:
        raise Exception('email', 'Invalid email.')
    if not passwd:
        raise Exception('passwd', 'Invalid password.')
    users = await User.findAll('email=?', [email])
    if len(users) == 0:
        raise Exception('email', 'Email not exist.')
    user = users[0]
    # check passwd:
    sha1 = hashlib.sha1()
    sha1.update(user.id.encode('utf-8'))
    sha1.update(b':')
    sha1.update(passwd.encode('utf-8'))
    print(sha1.hexdigest())
    print('passwd: {}'.format(user.passwd))

    # if user.passwd != sha1.hexdigest():
    #     raise Exception('passwd', 'Invalid password.')

    # authenticate ok, set cookie:
    r = Response()
    r.content_type = 'application/json'
    data = dict()

    if user.passwd == sha1.hexdigest():
        r.set_cookie(_COOKIE_NAME, encode_cookie(user, 86400), max_age=86400)
        user.passwd = '******'
        data['success'] = True
        data['data'] = user
        r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        return r
    else:
        data['failure'] = 'Invalid password.'
        r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        return r


async def api_register_user(request):
    # def api_register_user(*, email, name, passwd):
    '''
    用户注册模块
    :param email:
    :param name:
    :param passwd:
    :return:
    '''
    email = request.query.get('email')
    name = request.query.get('name')
    passwd = request.query.get('passwd')
    print('e: {} n: {} p: {}'.format(email, name, passwd))
    if not name or not name.strip():
        raise APIValueError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    # if not passwd or not _RE_SHA1.match(passwd):
    if not passwd:
        raise APIValueError('passwd')
    users = await User.findAll('email=?', [email])
    if len(users) > 0:
        raise APIError('register:failed', 'email', 'Email is already in use.')
    uid = next_id()
    sha1_passwd = '%s:%s' % (uid, passwd)
    user = User(id=uid, name=name.strip(), email=email, passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(),
                image='http://xxx/qq?d=mm&s=120')
    await user.save()
    # make session cookie:
    r = Response()
    # r.set_cookie(_COOKIE_NAME, encode_cookie(user, 86400), max_age=86400, httponly=True)
    r.set_cookie(_COOKIE_NAME, encode_cookie(user, 86400), max_age=86400)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r


async def islogin(request):
    # if request.__user__:
    if True:  # 暂时修改 登陆权限取消
        ##
        data = dict()
        data['success'] = True
        # data4['failure'] = None
        users = await User.findAll('email=?', ["258607438@qq.com"])
        data['data'] = users[0]
        ##
        r = Response()
        # request.__user__.passwd = '******'
        r.content_type = 'application/json'
        r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        # r.body = json.dumps(request.__user__, ensure_ascii=False).encode('utf-8')
        return r
    else:
        raise APIError('do not login! plase login!')


# endregion


# region nosql mongodb

async def testUploadFile(request):
    print(request)
    form = await request.post()
    form = dict(**form)
    img = form.get('file').file
    image = img.read()
    print(image)
    print(img)
    print(form)

    Url = request.message
    content = request.content
    x = request.query_string
    y = await content.read()
    # z = await request.post()
    # m = await request.json()
    print(Url)
    print(y)
    print(x)
    with open('test.png', 'wb') as f:
        f.write(image)


async def UploadFile(request):
    """
    use: action=http://127.0.0.1:9000/api/v1/UploadFile
    :param request:
    :return:
    """
    form = await request.post()
    form = dict(**form)
    DBName = request.query.get('DBName')
    file = form.get('file')
    print(file)
    namelist = file.filename.split('.')
    filename = namelist[:-1][0]
    file = file.file
    # content_type = file.content_type
    image = file.read()
    try:
        gfs = GFS(dbname=DBName)
        effectrows = await gfs.putBytes(bytes=image, name=filename)
        data = dict(success=True, data=effectrows.__str__())
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def UploadFileLarge(request):
    """
    use: action=http://127.0.0.1:9000/api/v1/UploadFileLarge
    :param request:
    :return:
    """
    DBName = request.query.get('DBName')

    reader = await request.multipart()
    field = await reader.next()
    # name = await field.read(decode=True)  # 全读取流

    namelist = field.filename.split('.')
    filename = namelist[:-1][0]

    image = await field.read()  # 全读取流 字节组

    # image = await field.read_chunk()  # 分桶读取流

    try:
        gfs = GFS(dbname=DBName)
        effectrows = await gfs.putBytes(bytes=bytes(image), name=filename)
        data = dict(success=True, data=effectrows.__str__())
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def GetImage(request):
    """
    use: http://127.0.0.1:9000/api/v1/GetImage?FileID=xxxxxxxxxxxxxxx
    :param request:
    :return:
    """
    # form = await request.post()
    DBName = request.query.get('DBName')
    FileID = request.query.get('FileID')
    try:
        gfs = GFS(dbname=DBName)
        # x,y = gfs.get('5ae3d6299f6b8f1714c7fdb5')
        x, y = await gfs.get(FileID)
        # print(x)
        # print(y)
        return render_image(x)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def GetFile(request):
    """
    format: image/jpeg
    use: http://127.0.0.1:9000/api/v1/GetImage?FileID=xxxxxxxxxxxxxxx
    :param request:
    :return:
    """
    DBName = request.query.get('DBName')
    FileID = request.query.get('FileID')
    Format = request.query.get('Format')
    try:
        gfs = GFS(dbname=DBName)
        x, y = await gfs.get(FileID)
        return render_file(data=x, format=Format)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def NosqlQuery(request):
    """
    example x = gfs.find(query={"filename": "1.png"}, projection={"filename":1}).sort([('uploadDate', -1)]).limit(1)
    :param reqest:
    :return:
    """
    DBName = request.query.get('DBName')
    FileName = request.query.get('FileName')
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    print(FileName)
    if FileName:
        query = {"filename": {'$regex': FileName}}  # '$regex' 模糊查询
    else:
        query = {}
    print(query)
    gfs = GFS(dbname=DBName)
    # res = gfs.find(query={"filename": FileName}, projection={"chunkSize": 0}).sort([('uploadDate', -1)]).skip(int(CurrentPage)).limit(int(PageSize))
    # reslist = list(res)
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    else:
        try:
            num = await gfs.count(query=query)

            p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
            if num == 0:
                data1 = dict(page=p.GetDict, res=[])
            else:
                # list = await VDBTable.findAll(limit=(p.offset, p.limit))
                reslist = await gfs.find(query=query, projection={"chunkSize": 0}) \
                    .sort([('uploadDate', -1)]) \
                    .skip(p.offset) \
                    .limit(p.limit) \
                    .to_list(length=100)

                reslistmap = list(map(lambda x: {"_id": str(x['_id']),
                                                 "filename": x['filename'],
                                                 "format": x.get("format", ""),
                                                 "uploadDate": str(x['uploadDate']),
                                                 "length": round(x['length'] / 1024 / 1024, 2)}, reslist))

                data1 = dict(page=p.GetDict, res=reslistmap)
            data = dict(success=True, data=data1)
            return render_json(data)
        except Exception as e:
            data = dict(failure=True, data=e)
            return render_json(data)

# endregion
