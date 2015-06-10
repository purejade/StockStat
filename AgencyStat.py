# -*- coding: utf-8-*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'purejade'
import requests

AgencyDir = 'C:\\Users\\purejade\\Desktop\\INSHOLD\\201503'

#海康威视

import  chardet
import os

if __name__ == '__main__':

    files = os.listdir(AgencyDir)

    stockAgency = {}
    for file in files:
        filename = os.path.join(AgencyDir,file)
        filehandler = open(filename,'rb')
        for line in filehandler:
            stockInfo = line.strip().split('\t')
            # print stockInfo
            try:
                if not stockAgency.has_key(stockInfo[1]):
                    stockAgency[stockInfo[1]] = 1
                else:
                    stockAgency[stockInfo[1]] = stockAgency[stockInfo[1]] + 1
            except Exception as e:
                print stockInfo
                print '----'+str(e)


    stocks = sorted(stockAgency.iteritems(),key=lambda d:int(d[1]),reverse=True)

    code = ['sh','sz']
    for stock in stocks:
        print stock[0],"===>",stock[1]
        if stock[0][0:2] == '60':
            print '沪市A股'
        elif stock[0][0:3] == '000':
            print '深市A股'
        elif stock[0][0:3] == '002':
            print '中小板'
        elif stock[0][0:3] == '300':
            print '创业板'
        elif stock[0][0:3] == '900':
            print '沪市B股'
        elif stock[0][0:3] == '200':
            print '深市B股'

        response = requests.get('http://hq.sinajs.cn/list=sh'+stock[0])
        content = response.content
        if 'FAIL' in response.content or 'var hq_str_sh'+str(stock[0])+'="";' in content:
            response = requests.get('http://hq.sinajs.cn/list=sz'+stock[0])
        # print response.content.decode('gb2312')
        content = response.content.decode('gb2312')
        if 'var hq_str_sh'+str(stock[0])+'="";' in content or 'FAIL' in content:
            print '------------' + stock[0]
        print content
        # print chardet.detect(response.content)


