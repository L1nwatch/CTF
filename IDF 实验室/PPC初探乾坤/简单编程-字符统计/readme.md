## 题目

这里这里 → http://ctf.idf.cn/game/pro/37

请听题：给你2秒钟的时间，告诉我下面这坨字符中有多少个w，多少个o，多少个l，多少个d和多少个y。 把这些数字串成一个字符串提交一下就可以了，很简单吧~

## solve

直接用 Python 代码实现：

```python
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import http.cookiejar
import string
import re

# url
url = "http://ctf.idf.cn/game/pro/37/"

# set cookie
req = urllib.request.Request( url )
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener( urllib.request.HTTPCookieProcessor( cj ) )
res = opener.open( req )

#正则表达式
content = res.read()
check_text = re.findall( r'<hr />(.*)<hr />',str( content ) )[0]

check_text = check_text[ 10:len( check_text ) - 6 ]

count = [ 0,0,0,0,0 ]#0w 1o 2l 3d 4y

for i in check_text :
    if i == 'w' :
        count[0] += 1
    elif i == 'o' :
        count[1] += 1
    elif i == 'l' :
        count[2] += 1
    elif i == 'd' :
        count[3] += 1
    elif i == 'y' :
        count[4] += 1

string = ""
for each in count :
    string += str( each )

print( string )

# 接下来就是提交了
value = { 'anwser':string }
data = urllib.parse.urlencode( value )  #先编码成网络字节序?题解只有这一句话，但是我自己用了报错，所以下面加了一句
data = urllib.parse.unquote_to_bytes( data )    #再转换成二进制？
request = urllib.request.Request( url,data )
response = opener.open( request )
html = response.read().decode( 'utf-8' )
print( html )
```

## write up1

第一眼看这道题很简单，不就是字符统计么，可是题目要求2s内回答，而且每次打开的页面需要统计的字符串内容都会变，这就蛋疼了，于是乎上网学习下如何提交post表单，然后用python写个程序自动提交就ok了（题目地址） 
代码如下：
```python
# -*- coding: utf-8 -*- 

import urllib2
import urllib
import cookielib
import string
import re

#需要提交post的url 
TARGET_URL = "http://ctf.idf.cn/game/pro/37/"

# 设置一个cookie处理器
req = urllib2.Request(TARGET_URL)
cj = cookielib.CookieJar() 
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) 
res = opener.open(req)

# 通过正则匹配抓到需要统计的字符串
content = res.read()
check_text = re.findall(r'<hr />(.*)<hr />',content,re.S)[0]

# 简单的统计
char_count = [0,0,0,0,0]
for txt in check_text:
        if txt == 'w':
            char_count[0] += 1
        elif txt == 'o':
            char_count[1] += 1
        elif txt == 'l':
            char_count[2] += 1
        elif txt == 'd':
            char_count[3] += 1
        elif txt == 'y':
            char_count[4] += 1

#将数字转换成字符串 
result = ""
for nIndex in char_count:
    result += str(nIndex)
print "Result = ", result

# 接下来就是提交了
value = {'anwser': result}
data = urllib.urlencode(value)
request = urllib2.Request(TARGET_URL,data)
response = opener.open(request)
html = response.read()
print html
```

需要注意的地方：你需要保存下来第一次正则匹配时打开页面cookie，构造一个opener，在第二次提交时使用之前的cookie即可。。。否则会提示超时
下面是一个大牛给我的代码，用到了第三方库mechanize:
```python
# coding=utf-8

import re
import urllib2
import mechanize

TARGET_URL = "http://ctf.idf.cn/game/pro/37/"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36 QQBrowser/3.5.3420.400"

# Get target text use regular expression.
def get_text(content):
    return re.findall(r'<hr />(.*)<hr />', content,re.S)[0]

def submit():

    char_count = [0, 0, 0, 0, 0]

    br_controller = mechanize.Browser()

    br_controller.set_handle_equiv(True)
    br_controller.set_handle_redirect(True)
    br_controller.set_handle_referer(True)
    br_controller.set_handle_robots(False)
    
    br_controller.addheaders = [("User-Agent", USER_AGENT)]
    
    br_controller.open(TARGET_URL)
    
    # Get web page cotent
    page_content = br_controller.response().read()
    
    # Get target text
    check_text = get_text(page_content)
    
    # Calculate
    for txt in check_text:
        if txt == 'w':
            char_count[0] += 1
        elif txt == 'o':
            char_count[1] += 1
        elif txt == 'l':
            char_count[2] += 1
        elif txt == 'd':
            char_count[3] += 1
        elif txt == 'y':
            char_count[4] += 1


    # Change value in char_count to string.
    result = ""
    for nIndex in char_count:
        result += str(nIndex)
    
    print "Result = ", result
    
    # Post form.
    br_controller.select_form(nr=0)
    br_controller.form['anwser'] = result
    br_controller.submit()
    
    print br_controller.response().read()

if __name__ == '__main__':
    submit()
```

## write up2

速度要快，用AutoHotKey，语法不太适应

```AutoHotKey
^d::
StringCaseSense, On
w := o := l := d := y := -1
Sleep 100
strArr := StrSplit(ClipBoard)  ; 分离字符
for index, ch in strArr
{
  if ch = w  ; w 是字符串不是变量名
    w := w + 1
  if ch = o
    o := o + 1
  if ch = l
    l := l + 1
  if ch = d
    d := d + 1
  if ch = y
    y := y + 1
}
Send {TAB}
Send %w%%o%%l%%d%%y%
Send {ENTER}
Return
```

## write up3

第一，题目统计时间是靠cookie来统计的，所以得去设置一下cookies

```python
# set cookies
req = urllib.request.Request( url )
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener( urllib.request.HTTPCookieProcessor( cj ) )
res = opener.open( req )
```
以上是如何设置cookies。然后是抓取网页内容，答案用到了正则表达式，这方面我还不是很熟：

`check_text = re.findall( r'<hr />(.*)<hr />',str( content ) )[0]`


第三，提交的问题，看来得把数据转一下格式才能提交的吧：
```python
value = { 'anwser':string }
data = urllib.parse.urlencode( value )  #先编码成网络字节序?题解只有这一句话，但是我自己用了报错，所以下面加了一句
data = urllib.parse.unquote_to_bytes( data )    #再转换成二进制？
request = urllib.request.Request( url,data )
```


