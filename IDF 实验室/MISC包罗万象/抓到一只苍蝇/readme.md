## 题目

报告首长！发现一只苍蝇。。

在哪？

here!

卧槽？！好大一坨苍蝇。。

文件地址： http://pan.baidu.com/s/1bnGWbqJ

提取码：oe6w

PS：flag写错了，太麻烦也懒得改了，格式还是wctf{...}，大家明白就好，不要在意这些细节。。

## write up

下载下来是一个抓包得到的文件 `misc_fly.pcapng`，用 wireshark 打开，看到提示说找到第13个包 POST 包。打开内容得到

![1]()

可以知道这里是上传（提示说是上传，其实也有可能是下载不是么。。。）了一个 `fly.rar`，以及该文件的md5 还有 sha 码

继续在包里搜内容，利用过滤语句：`http.request.method == "POST"`

得到结果：

![2]()

查看这几个包的内容，发现倒数第二个包（其实我看了提示之后直接去看倒数第二个包的内容了）

![3]()

仔细浏览包的内容，可以知道这是数据包的内容：一封带附件的邮件

```json
发件人：81101652@qq.com
收件人：king@woldy.net
附件：fly.rar
附件大小：525701 Bytes
```

***

【PS】这里如果没对wireshark安装过解析插件的话会很难看，我找到了网上的一个：http://blog.csdn.net/jasonhwang/article/details/5525700。用Wireshark lua编写的协议解析器查看Content-Type为application/x-www-form-urlencoded的HTTP抓包，才变成了上面那样的显示。

***

在 POST 结果中继续搜，发现这5个包：

![4]()

`/ftn_hander` 表示这可能就是上传的包的内容，自己把这5个包的内容的拷贝出来

***

【PS】http://www.2cto.com/Article/201201/115879.html

Export > Selected Packet Bytes…	 	导出当前在Packet byte面版选择的字节为二进制文件。	 

***

按照提示得将内容导出成二进制文件，自己之前试过右键包copy十六进制流，无奈怎么搞都觉得字节数大小不对。所以就按照网上的方法成功导出了5个二进制文件。

提示说，这5个二进制文件的前面有部分内容都一样的，提示给了个公式来计算多余的内容：

### 还原附件数据

观察5个包 Media Type 域的内容，前面很大一部分内容是相同的，那么这一部分是通信时所需的头部的内容，不是附件本身的内容，通过计算将多余的数据去除。
已知： 

* 附件被分成5个部分 
* 5个子部分合计大小为527521 
* 附件原大小为525701 

求： 

* 每个子部分头部多余的数据

容易求出，头部多余的部分：`527521−5257015=364Bytes`

遂写了 media_type2clear.py 来实现这个功能，生成了 sum.rar，然后放到 kali 下用 md5sum 验证一下 md5，发现一致，说明成功了。

```python
# media_type2clear.py
import os

def file2clear():
    for i in range(1, 6):
        filename = str(i) + "b"
        with open(filename, "rb") as f:
            data = f.read()
            data = data[ 364: ]

            filename = str(i) + "b_clear"
            with open(filename, "wb") as f2:
                f2.write(data)

def clear2sum():
    with open("sum.rar", "wb") as f:
        for i in range(1, 6):
            filename = str(i) + "b_clear"
            with open(filename, "rb") as f2:
                f.write(f2.read())
            os.remove(filename)
    
if __name__ == '__main__':
    file2clear()
    clear2sum()
```

但是 sum.rar 没法进行解压，看题解说是伪加密（题解用的 winrar 打开后说是压缩文件的加密或者文件头损坏）

**以下是题解原话：即这是一个未加密过的rar文件，但是却将加密位置为了1，具体可参考 [rar文件格式描述](http://www.cnblogs.com/javawebsoa/archive/2013/05/10/3072132.html)。**

***

只需将文件开头处0x74位后面的0x84位置改为0x80即可

![5]()

修改后顺利解压，得到 `flag.txt`。

看 rar 文件格式描述中的 File header (File in archive)，有 `HEAD_FLAGS 2 bytes Bit flags` 这一项，其中的`0x04 - file encrypted with password` 加密标志。【注：此位若被置1，则文件使用了基于密钥的加密】

先跳过 `MAIN_HEAD`，来到 `File header`，`HEAD_FLAGS` 的定义为 0x04 为加密文件

`MARK_HEAD` 共7个字节，`MAIN_HEAD` 共13个字节，`HEAD_CRC` 和 `HEAD_TYPE` 共3个字节，数下来第24个字节刚好就是图片中的84（十六进制）。

其实也可以直接定位：`HEAD_TYPE  1 byte  Header type: 0x74` 找到接下来就是加密的位置了。

***

【其实这里不太看得懂，反正用 winHEX 改完之后确实可以解压缩了，得到flag.txt】

直接改后缀名 `flag.exe`,变成一个苍蝇满屏幕跑的程序，看上去没什么用。。。

所以改回来成txt，然后作为十六进制文件打开看一下，题解说是搜索：

文件内搜PNG、Rar、JFIF，文件尾有一个PNG，提取出来，是个二维码。于是利用 `ExtractX` 提取出来 `PNG` 得到二维码，扫一下确实得到了 flag。

***

### wireshark 导出 `Media_type` 内容

Wireshark使用方法（学习笔记一）http://www.2cto.com/Article/201201/115879.html

Export > Selected Packet Bytes…	 	导出当前在Packet byte面版选择的字节为二进制文件。	 

### wireshark 分析包内容

用Wireshark lua编写的协议解析器查看Content-Type为application/x-www-form-urlencoded的HTTP抓包

http://blog.csdn.net/jasonhwang/article/details/5525700

