## 题目
题目太长, 放在了 `problem.txt` 里了, 或者可以直接去 IDF 实验室网站查看, 以下只列出一部分:

```javascript
[][(![]+[])[!![]+!![]+!![]]+({}+[])[+!![]]+(!![]+[])[+!![]]+(!![]+[])[+[]]][({}+[])[!![]+!![]+!![]+!![]+!![]]+({}+[])
```

## write up
网上题解的几个编码，感觉都怪怪的。
自己百度了一下，搜索了能用[]()+!转换成任意js代码的文章：
http://www.cnblogs.com/pandora/archive/2010/02/27/1674833.html

找到了翻译工具：
http://discogscounter.getfreehosting.co.uk/js-noalnum.php?txt=alert%28%22hi+there%22%29
将题目的一大堆[](![]复制进去，点击
alert( eval( --v ) )得到密码：

![解密结果](https://github.com/L1nwatch/CTF/blob/master/IDF%20%E5%AE%9E%E9%AA%8C%E5%AE%A4/WEB%E5%A4%A9%E7%BD%97%E5%9C%B0%E7%BD%91/%E4%B8%80%E7%A7%8D%E7%BC%96%E7%A0%81%E8%80%8C%E5%B7%B2/after_decrypt.png?raw=true)

