## 题目
就在这里，很简单的~虽然我不会。。= =！  http://pan.baidu.com/s/1dDzUL0X

## write up
下载完打开后发现缺少组件，网上下载：http://www.jb51.net/dll/msvcr100d.dll.html#down

用PEiD查看过了，VS2008的，没有加壳。

自己猜测是，14+17的那几个数字全都转成ascii码就是了，看下write_up。看完懂了，

![1](https://github.com/L1nwatch/CTF/blob/master/IDF%20%E5%AE%9E%E9%AA%8C%E5%AE%A4/REVERSE%E5%80%92%E8%A1%8C%E9%80%86%E6%96%BD/%E7%AE%80%E5%8D%95%E7%9A%84PE%E6%96%87%E4%BB%B6%E9%80%86%E5%90%91/1.png?raw=true)

的意思不是取变量 14 开始的值，而是从数组 `byte_415768` 中取索引值（变量14所表示的值）的字符出来。
该数组就是：`swfxc{gdv}fwfctslydRddoepsckaNDMSRITPNsmr1_=2cdsef66246087138`
用python取得：

```python
List = [1,4,14,10,5,36,23,42,13,19,28,13,27,39,48,41,42]
string="swfxc{gdv}fwfctslydRddoepsckaNDMSRITPNsmr1_=2cdsef66246087138"
for each in List:
	print(string[each],end="")
```

前半部分：
`wctf{Pe_cRackme1_`

后半部分为：

![2](https://github.com/L1nwatch/CTF/blob/master/IDF%20%E5%AE%9E%E9%AA%8C%E5%AE%A4/REVERSE%E5%80%92%E8%A1%8C%E9%80%86%E6%96%BD/%E7%AE%80%E5%8D%95%E7%9A%84PE%E6%96%87%E4%BB%B6%E9%80%86%E5%90%91/2.png?raw=true)

把这后面依次转为ascii：
```python
>>> List = [49,48,50,52,125]
>>> for each in List:
	print(chr(each), end="")
1024}
```

综上，flag为 `wctf{Pe_cRackme1_1024}`

【总结】

这种题不是为了爆破（话说我一开始强制让jmp到判断正确的地方），结果，不是这样干啊。

还有要求输入的flag并不就等于flag，得去用ida分析程序逻辑才行。

