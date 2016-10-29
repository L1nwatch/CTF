## 题目
每个人都会梦想手头有一把0day，不过0day可遇不可求，我们还是关注最新的漏洞吧：http://pan.baidu.com/s/1hqf5YZE
答案格式：wctf{***}

## Write Up
下载后得到一个后缀名为pcapng的文件，百度了之后知道使用 WireShark 打开的。打开后得到：

![from_WireShark]()

百度了一下KRB5，知道了是：
Kerberos
再搜索一下kerberos 漏洞，得到文章：
http://science.china.com.cn/2014-11/19/content_34096228.htm
北京时间11月19日凌晨，微软官网发布安全公告MS14-068
题解说漏洞名称就是这个MS14-068，故得解

