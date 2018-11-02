'''
learning web spider
'''
import urllib.request
import urllib.parse
import hashlib
import time
import random
import json

def get_content(url):
    ''' get_content url '''
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    print(response.info())
    print(response.getcode())

def get_md(value):
    '''md5加密'''
    m = hashlib.md5()
    # m.update(value)
    m.update(value.encode('utf-8'))
    return m.hexdigest()

def get_salt():
    '''根据当前时间戳获取salt参数'''
    s = int(time.time() * 1000) + random.randint(0, 10)
    return str(s)

def get_sign(msg,salt):
    '''使用md5函数和其他参数，得到sign参数'''
    D = "ebSeFb%=XZ%T[KZ)c(sy!"
    s = "fanyideskweb" + msg + salt + D
    return get_md(s)

def translation(docs):
    '''  using youdao translation '''
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    datayoudao = {}
    salt = get_salt()
    datayoudao['i']           = docs
    datayoudao['from']        = 'AUTO'
    datayoudao['to']          = 'AUTO'
    datayoudao['smartresult'] = 'dict'
    datayoudao['client']      = 'fanyideskweb'
    datayoudao['salt']        = salt
    datayoudao['sign']        = get_sign(docs, salt)
    datayoudao['doctype']     = 'json'
    datayoudao['version']     = '2.1'
    datayoudao['keyfrom']     = 'fanyi.web'
    datayoudao['action']      = 'FY_BY_CLICKBUTTION'
    datayoudao['typoResult']  = 'true'

    data = datayoudao 
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0')
    req.add_header('Cookie', 'OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;')
    req.add_header('Referer', 'http://fanyi.youdao.com/')
    response = urllib.request.urlopen(req)
    html = response.read()
    print(html)
    infos = json.loads(html)
    if 'translateResult' in infos:
        try:
            result = infos['translateResult'][0][0]['tgt']
            print(result)
        except:
            pass

if __name__ == "__main__":
    #get_content("http://placekitten.com/200/300")
    translation('苹果在桌子上')
