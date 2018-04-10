import carteapi

username = "cluster"
password = "cluster"
# client = carteapi.Client("http://127.0.0.1:9999/kettle/", username, password)
# status = client.status()
# jobs = client.jobs()
# transformations = client.transformations()
# print(f'status {status}'.format(status))
# print(f'jobs {jobs}'.format(jobs))
# print(f'transformations {transformations}'.format(transformations))
#
# rjob = client.stop_job(id='c543cb4c-7591-478e-8c07-3a498c527c87')
# print(rjob)



class ETLCarte(object):
    def __init__(self, clienturl):
        self.clienturl = clienturl
        self.client = carteapi.Client(self.clienturl, username, password)

    def get_status(self):
        """
        获取 子服务器运行状态
        :return: online offline
        """
        return self.client.status()

    def get_jobs(self):
        """
        获取 子服务器的作业列表
        :return: online offline
        """
        return self.client.jobs()