import hashlib

uid ='258607438@qq.com'
passwd = '123'
sha1_passwd = '%s:%s' % (uid, passwd)
x = hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest()
print(x)