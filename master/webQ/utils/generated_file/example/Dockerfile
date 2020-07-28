FROM python
MAINTAINER akeec
RUN pip install aiohttp
RUN pip install aiohttp_cors
RUN pip install aiomysql
RUN pip install jinja2
RUN pip install mysql-connector-python
RUN pip install pymongo==3.7.1
RUN pip install motor==2.0.0
RUN pip install aiohttp_swagger
RUN mkdir /app
COPY . /app
RUN cd /app && python setup.py install
RUN echo 'Hi, I am in your container'
EXPOSE 7000
CMD ["python","/app/app.py"]