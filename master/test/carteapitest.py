import carteapi
from webQ.q_helpers import Page

# username = "cluster"
# password = "cluster"
# client = carteapi.Client("http://127.0.0.1:9999/kettle/", username, password)
# status = client.status()
# jobs = client.jobs()
# transformations = client.transformations()
# print(f'status {status}'.format(status))
# print(f'jobs {jobs}'.format(jobs))
# print(f'transformations {transformations}'.format(transformations))

# rjob = client.stop_job(id='c543cb4c-7591-478e-8c07-3a498c527c87')
# print(rjob)

# for x in jobs:
#     print(x)
#     print(x.jobname)
#     print(x.status_desc)
    # print(x.log_date)
    # img = client.job_image(id=x)
    # print(img)
    # with open('x.jpg', 'wb') as f:
    #     f.write(img)
# for y in transformations:
#     print(y)

# y = [{'name': x.jobname, 'satus': x.status_desc, 'jobnum': x.id} for x in jobs]
# print(y)
#
# import pandas as pd
#
# z = pd.DataFrame(y)
# print(z)

x = Page(15000, 4, 100)  # totalcount  # currentpage  # pagesize
# y = dict(page=dict(x), data=dict(a1=100, a2=201))
# y=dict(x)
# print(y)
# print(type(y))

print(x.GetDict)
print(type(x.GetDict))