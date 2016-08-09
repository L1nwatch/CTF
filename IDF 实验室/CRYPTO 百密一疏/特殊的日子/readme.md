# 题目
每个人的一生中都会或多或少有那么几个对自己很重要的日子，比如对于我来说，这一天就很重要。

答案格式wctf{日期}  //友情提示，此题需要暴力破解，但只是爆破这段密文，不是爆破这个网站。。 = =！

就是这一天↓

4D1FAE0B

# write up
看了网上的答案，说是用 crc32 编码，然后爆破就行了。所以自己参考了代码，用 Python 解决了

kali 神器啊，`hashid`命令：可以跑出可能的加密算法！！！！

已知是 crc32 算法，Python 的库 binascii 带有 crc32() 函数可以进行计算，参考 py 文件。

Tip：
* 转成 bytes 字节流
* zfill 补 0
* hex 后前缀 0x
* return 跳出多重循环

## Python Script
```python
import binascii

def solve(key):
    for year in range(3000):
        for month in range(1,13):
            for day in range(1,32):
                date = str(year).zfill(4) + \
                       str(month).zfill(2) + \
                       str(day).zfill(2) #记得补0,要不然形式错
                crc32_date = binascii.crc32(bytes(date, "utf-8")) \
                             #3.X版本要像都要这样bytes
                crc32_date = (hex(crc32_date).upper())[2:]  #hex后形式为0x
                if crc32_date == key:
                    print(date)
                    return #跳出多重循环

if __name__ == '__main__':
    crc32_date = "4D1FAE0B"
    solve(crc32_date)
    input("输入任意键结束")
```
