# -*- coding: utf-8-*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'purejade'

import requests
import json
import codecs
import re

def write_page(content,filename='index.html'):
    open(filename,'wb').write(content)

def getAllFunds(url):

    url = 'http://fund.eastmoney.com/js/fundcode_search.js'
    funder = codecs.open('fund.txt','wb','utf-8')

    session = requests.session()
    resp = session.get(url)
    if resp:
        print resp.content
        content = resp.content
        content = content[content.find('['):content.rfind(']')+1]
        print content
        fundInfos = json.loads(content)
        for fundInfo in fundInfos:
            for index,ele in enumerate(fundInfo):
                if index < len(fundInfo) - 1:
                    funder.write(ele+'\t')
                else:
                    funder.write(ele)
            funder.write('\n')
    else:
        print "wrong"
    pass

def getAllFundCode(funder):
    codes = []
    with open('fund.txt','rb') as handler:
        for line in handler:
            codes.append(line.split['\t'][0])
    return codecs

def getStocksOfFund(fundcode):
    prefix = 'http://fund.eastmoney.com/'+str(fundcode)+'.html'
    resp = requests.get(prefix)
    parseFundPage(resp.content)
    write_page(resp.content,'index.html')

def parseFundPage(content):

    if not content: return
    # type_start = content.find('类　　型：')
    # type_start = content.find('<td>',type_start)
    # type_end = content.find('</td>',type_start)
    # type_info = content[type_start:type_end]
    # type = re.search(r'<a href="(.*?)">(.*?)</a>',type_info)
    # if type:
    #     print type[1]
    # else:
    #     print 'the type is wrong'
    content = content.replace('zf die','zf zhang')
    stocksInfoList = re.findall(r'<ul><li class="xh">(.*?)</li><li class="mc"><a href="(.*?)">(.*?)</a></li><li class="cc"><span class="ping">(.*?)</span></li><li class="zf zhang">(.*?)</li>',content)
    if stocksInfoList:
        print stocksInfoList

if __name__ == '__main__':
    url = ''
    # getAllFunds(url)
    getStocksOfFund(770001)


