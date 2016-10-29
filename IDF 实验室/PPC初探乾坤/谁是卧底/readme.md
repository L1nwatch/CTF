## 题目
武林中某知名杀手在一次任务中失败，然后逃窜到了人群中，当时那个社会并没有我们现在这么发达，满地都是文盲，而这些文盲甚至连一句完整的英文都说不出来，所以其实只要用心去发现，就会很容易发现这个稍微有些文化的杀手是谁哦~答案wctf{杀手的英文名}

人群→ http://pan.baidu.com/s/1bnq6nmR

密码: 988u

## 网上 write up
### 1. 初步分析
下载文件，得到whoiswoldy.txt，5.6MB大小，用wc命令统计一下：`wc whoiswoldy.txt`，输出为：

```shell
0       1 5586640 whoiswoldy.txt
```

0行，1个词，55586640个字符，也就说文件里只有一个大字符串，字符数是千万级。

和小伙伴商量解体思路，观察到文件名有woldy这个词，首先找一下它吧。

vim打开之，/woldy 之，找是找到了，无奈文件太大，这个词出现过几十次，而且上下文里没有一个完整的单词，全是乱序字母。搜flag结果一样。

继续观察文件，发现文件里零零落落地分散着许多单词，但周围全是无序字母，不成句子。然后小伙伴做了常用词的词频统计：

```shell
not:   497
kill:  184
iam:   292
whois: 1
you:   415
name:  68
my:    7510
woldy: 50
we:    9841
are:   1855
```

结合题目——而这些文盲甚至连一句完整的英文都说不出来。懂了：

* 这是一个由英文单词和随机字母拼合而成的文件
* 文件中应该存在完整的英文句子，flag就在那儿

接下来需要在文件中寻找整句的英文。

### 2. 编写程序

用肉眼在5000多万字符里找一句话无疑是大海捞针，需要编程解决，接下来要考虑编程的思路了。一个直接的想法是：句子由单词组成，只要能够找到文件里所有的单词，其中单词密度最大的地方就是完整英文句子所在的地方。于是问题分为两步：

* 统计汇总文件中所有单词的位置（单词首字母在字符串中的位置）
* 找到单词分布最为密集的位置

首先第一步，需要找一个txt格式的字典文件，英文常用3000词应该足够，每行一个单词，文件名为words.txt，然后跑程序记录每个单词出现过的位置就可以了。

```python
#定义寻找字串位置的函数
#subString:子串
#fullString:完整字符串
#indexs:字串出现的所有位置
#即接受子串和完整字符串，返回子串在完整字符串里出现的所有位置
#例如findSubStr('hi','hiworldhiworld')得到[0,7]
def findSubStr(subString,fullString):
    indexs = []
    fullLength = len(fullString)
    subLength = len(subString)
    for i in range(fullLength-subLength):
        if fullString[i:i+subLength] == subString:
            indexs.append(i)
    return indexs

#读取题目文件内的字符串
with open('whoiswoldy.txt','r') as f:
    s = f.read()

#逐行读取字典words.txt内的单词，寻找其在s内的所有位置
#places为单词出现过的所有位置
places = []
with open('words.txt','r') as f: 
    while 1:
        line = f.readline()
        line=line.strip('\n')
        if not line:
            break
        places += findSubStr(line,s)
#用pickle库将得到的位置数组places保存到result.txt中
import pickle
with open('result.txt','w') as f:
    pickle.dump(places,f)
```

运行此段程序，即可得到单词的位置统计，是一个list，每一项为一整数，即出现过单词的位置，保存在result.txt中。

上一段程序存在性能问题，直接用python运行的时间目测要上小时，不想费时间优化，改用PyPy解释器，2分钟跑完。由此发现对于纯python代码，尤其是循环较多的情况下，PyPy比CPython真的要快上好多倍。

***

然后第二步，统计单词密度。由第一步得到的位置数据，每个位置附近出现单词数的多少即可反映单词的密度。比如假设得到的位置数据是这样的：

`[1,8,13,15,20,25,28,100,220,33000...]`

显然在1～28单词分布密集，极有可能这里就是一句话。

一句话的长度大概几十词左右，长一点的会上百，简单的取100这个参数，统计[position,position+100]这一范围内出现了多少个单词。

比如对于上一个列表，对于位置'1'，在[1,101]范围内，有1,8,13,15,20,25,28,100共8个位置出现过单词，即1往后100的范围内有8个单词。所以对1这个位置的密度记为8。同理位置8的密度记为7。而对于100这个位置，在[100,201]范围内除了100本身没有其他位置出现过单词。因此对于位置100的密度记为1。需要注意的是进行统计之前首先要对位置数据进行去重复处理。
第二步程序：

```python
#读取题目字符串
with open('whoiswoldy.txt','r') as f:
    s = f.read()
#加载前一步得到的位置数据
import pickle
with open('result.txt','r') as f:
    b = pickle.load(f)
#将位置数据b，一个list转化为集合set，即可实现去重复处理
#同时查找元素的时间由list的O(n)变为set的O(1)，因为set是hashable的
setb = set(b)

#den为密度统计，每个元素的形式为(int位置，int密度)
den = []
for number in setb:
    k = 1 
    for i in range(number,number+100):
        if i in setb:
            k += 1
    den.append((number,k))

#根据密度进行排序
sortedDen = sorted(den,key=lambda x:x[1],reverse=True)
#输出密度排名前10的位置
print sortedDen[0:10]
index = sortedDen[0][0]
print s[index:index+150]
```

其中 `print sortedDen[0:10]` 的输出为
```python
[
 (3197571, 34), (3197573, 33), (3197581, 32),
 (3197583, 31), (3197586, 31), (3197600, 31),
 (4738813, 31), (4738831, 31), (3197603, 30),
 (3197618, 30)
]
```

几乎可以肯定319757x～31976xx存在完整句子了。

```python
index = sortedDen[0][0] = 3197571
print s[index:index+150]
```
将3197571及其往后150个字符打印出来，结果为

```python
ananjpywlqclassifyubcjesqtqyjhazbornndomhfchvlc(手打分隔线)--whatwillyouseeifyouthrowthebutteroutthewindow--(手打分隔线)wzqmtwmyjutipvqetrsshyosypzydevelopponaxoezspdespairkuoqignice
```

看到了这么一句：`what will you see if you throw the butter out the window`，用眼睛看就知道这是个谜语，搜之，谜底：`butterfly`

### 3. flag

wctf{butterfly}

## 自己的代码

### 文件清单

* 【countWordsDensity.py】
* 【findSentence.py】
* 【getWordsPosition.py】
* 【testify.py】
* 【英语中最常用到的500个热点单词.txt】
* 【count_position.py】
* 【solve.py】
* 【words_Position.py】

### 链接

直接放 [GitHub]() 上吧。