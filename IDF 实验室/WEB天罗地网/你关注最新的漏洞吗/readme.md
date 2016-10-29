## 题目
每个人都会梦想手头有一把0day，不过0day可遇不可求，我们还是关注最新的漏洞吧：http://pan.baidu.com/s/1hqf5YZE
答案格式：wctf{***}

## Write Up
下载后得到一个后缀名为pcapng的文件，百度了之后知道使用 WireShark 打开的。打开后得到：

![from_WireShark](https://github.com/L1nwatch/CTF/blob/master/IDF%20%E5%AE%9E%E9%AA%8C%E5%AE%A4/WEB%E5%A4%A9%E7%BD%97%E5%9C%B0%E7%BD%91/%E4%BD%A0%E5%85%B3%E6%B3%A8%E6%9C%80%E6%96%B0%E7%9A%84%E6%BC%8F%E6%B4%9E%E5%90%97/wireshark.png?raw=true)

百度了一下KRB5，知道了是：
Kerberos
再搜索一下kerberos 漏洞，得到文章：
http://science.china.com.cn/2014-11/19/content_34096228.htm
北京时间11月19日凌晨，微软官网发布安全公告MS14-068
题解说漏洞名称就是这个MS14-068，故得解

