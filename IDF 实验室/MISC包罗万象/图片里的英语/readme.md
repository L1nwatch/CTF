## 题目

一恒河沙中有三千世界，一张图里也可以有很多东西。
不多说了，答案是这个图片包含的那句英文的所有单词的首字母。
首字母中的首字母要大写，答案格式是wctf{一坨首字母}
加油吧少年！看好你哦~

![problem](https://github.com/L1nwatch/CTF/blob/master/IDF%20%E5%AE%9E%E9%AA%8C%E5%AE%A4/MISC%E5%8C%85%E7%BD%97%E4%B8%87%E8%B1%A1/%E5%9B%BE%E7%89%87%E9%87%8C%E7%9A%84%E8%8B%B1%E8%AF%AD/problem.png?raw=true)

## write up

图片下下来后，用16进制打开，没发现什么。
（【PS】搜索rar、flag，可以看到，rar中藏了个flag图片）
后缀名改为.rar，解压得到一张图片。【文件夹中有个在图片中附加rar文件的链接，有空可以学下】
同样用16进制打开，没发现什么。
把这张图片放到百度识图，搜索得到是赵本山的一张剧照。
http://shitu.baidu.com/

![solve](https://github.com/L1nwatch/CTF/blob/master/IDF%20%E5%AE%9E%E9%AA%8C%E5%AE%A4/MISC%E5%8C%85%E7%BD%97%E4%B8%87%E8%B1%A1/%E5%9B%BE%E7%89%87%E9%87%8C%E7%9A%84%E8%8B%B1%E8%AF%AD/solve.png?raw=true)

依旧没有英文。
百度这句台词：
咱连个年轻的小雏都没有打过。今后还怎么在江湖上混？
是的，老大，江湖险恶，不行就撤啊。
年轻人，May the force be with you!
得到一句英文
年轻人：May the force be with you!
答案：`wctf{Mtfbwy}`		#注意不是wctf{MTFBWY}害得我扣了0.03分啊!

## 如何在图片中附加rar文件

1. 将图片和要附加的压缩文件放在同一目录下
2. 新建一个文本文档，在里面添加以下内容：`copy /b (原图片名).jpg + (压缩文件名).rar  (附加后的图片名).jpg`


3. 将文本文档后缀名改为 .bat 点击运行。