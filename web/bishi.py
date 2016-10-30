from tornado import httpserver,ioloop,web,gen,httpclient
from datetime import datetime
from base_handler import BaseHandler
from tools import *
import conf
import tornado_mysql
import urllib.parse
from urllib.parse import urljoin,urlencode
import json
import random
import pymysql
import time
import random


class BishiHandler(BaseHandler):

    @gen.coroutine
    def get(self):
        f=open('bishi.txt','r')
        test=f.readlines()
        timu=[]
        for i in range(0,len(test),5):
            a=[[test[i+1],1],[test[i+2],0],[test[i+3],0],[test[i+4],0]]
            random.shuffle(a)
            timu.append([test[i],a])
        
        timu=random.sample(timu,20)

        print('get '+str(datetime.now()))
        msg = self.get_argument('msg',None)
        
        self.render('bishi.html',msg=msg,page_type='contest',page_title='笔试测试 -XOJ',timu=timu)

