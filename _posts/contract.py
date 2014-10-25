# coding=utf-8
__author__ = 'liuzheng'
import sys
import os
import urllib
import urllib2
import pycurl
import cStringIO
import re
from bs4 import BeautifulSoup

MAIN = 'http://www.64365.com'


def getHTT_Header(url):
    q = re.compile(r'(.*?): (.*)')
    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    header = cStringIO.StringIO()
    body = cStringIO.StringIO()
    c.setopt(pycurl.HEADERFUNCTION, header.write)
    c.setopt(pycurl.WRITEFUNCTION, body.write)
    c.perform()
    header.reset()
    R = {}
    for i in header.readlines():
        r = re.search(q, i)
        if r:
            R[r.group(1)] = r.group(2)
    return R


def main():
    url = 'http://www.64365.com/article/contract/down_283.aspx'
    # opener = urllib2.build_opener()
    # request = urllib2.Request(url)
    # request.get_method = lambda: 'HEAD'
    # try:
    # response = opener.open(request)
    # response.read()
    # except:
    # print '%s,%s' % (url, e)
    # else:
    # print dict(response.headers).get('Content-Disposition', 1)
    # # data = urllib2.urlopen(url)
    # # print data
    # print urllib2.urlopen(url)
    # c= pycurl.Curl(url)
    # c.setopt(pycurl.URL,url)
    # c.setopt(pycurl.HTTPHEADER,["Accept:"])
    import httplib

    conn = httplib.HTTPConnection(url)
    conn.request("GET", "")
    r = conn.getresponse()
    print r.getheader()


def download(filename, url):
    type = sys.getfilesystemencoding()
    urllib.urlretrieve(url, filename.decode('utf-8').encode(type))


def getList():
    response = urllib2.urlopen('http://www.64365.com/contract/tdzyht/')
    soup = BeautifulSoup(response.read())
    leftBar = soup.findAll('ul')[2]
    Chapter = []
    for i in leftBar.findAll('div'):
        Chapter.append(i.a.text)
    t = 0
    contract = {}
    for i in leftBar.findAll('ul'):
        tmp = []
        for j in i.findAll('a'):
            tmp.append({'name': j.text, 'url': j.get('href')})
        contract[Chapter[t]] = tmp
        t += 1
    return contract


def getDownlink(url):
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response.read())
    link = getLink(url)
    for i in soup.select(".page")[0].select("a"):
        if i.get("class") == None:
            link = link + getLink(MAIN + i.get("href"))
    return link


def getLink(url):
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response.read())
    link = []
    for i in soup.select(".comp-list")[0].select(".xia"):
        link.append(i.get('href'))
    return link


def mkdir(path):
    if os.path.exists(path) == False:
        os.makedirs(path)


if __name__ == '__main__':
    # main()
    # url = 'http://www.64365.com/article/contract/down_283.aspx'
    PATH = 'D:/contract'
    q = re.compile(r'filename=(.*)')
    mkdir(PATH)
    list = getList()
    for l in list:
        mkdir(PATH + '/' + l)
        for c in list[l]:
            mkdir(PATH + '/' + l + '/' + c['name'])
            ppath = urllib.unquote((PATH + '/' + l + '/' + c['name'] + '/').encode('utf8'))
            for g in getDownlink(MAIN + c['url']):
                print ppath + urllib.unquote(re.search(q, getHTT_Header(MAIN + g)['Content-Disposition']).group(1)[:-1])
                download(
                    ppath + urllib.unquote(re.search(q, getHTT_Header(MAIN + g)['Content-Disposition']).group(1)[:-1]),
                    MAIN + g)

                # getDownlink('http://www.64365.com/contract/lcht/')
                # p = getHTT_Header(url)
                #
                # filename = 'D:/' + urllib.unquote(re.search(q, p['Content-Disposition']).group(1)[:-1])
                # download(filename, url)