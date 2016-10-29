## 题目
只给了一张图片:

![题目](https://github.com/L1nwatch/CTF/blob/master/IDF%20%E5%AE%9E%E9%AA%8C%E5%AE%A4/STEGA%E4%B8%87%E9%87%8C%E5%AF%BB%E8%B8%AA/%E7%BA%A2%E4%B8%8E%E9%BB%91/problem.jpg?raw=true)

## write up

看了writeUp后知道只要改变一下图片的曝光度就可以看到字符串了，还有些人用py把图片处理了一下。详看answer.py
自己是用PS把图片搞搞得到的：

![PS 调整得到](https://github.com/L1nwatch/CTF/blob/master/IDF%20%E5%AE%9E%E9%AA%8C%E5%AE%A4/STEGA%E4%B8%87%E9%87%8C%E5%AF%BB%E8%B8%AA/%E7%BA%A2%E4%B8%8E%E9%BB%91/after_ps.png?raw=true)

wctf{h0w_Can_Make_A_Steg}

### 代码实现

```python
#!/usr/bin/env python
#coding:utf-8

import Image

def ima(url):
	img=Image.open(url)
	sizes=img.size
	new=Image.new("RGB",sizes)
	for i in range(sizes[0]):
		for j in range(sizes[1]):
			r,g,b=img.getpixel((i,j))	#遍历每个像素点
			if r>0:						#去掉红色值
				r=0
			if (r==0)&(g==0)&(b==0):	#让黑色其填充成纯白色
				r=255
				g=255
				b=255
			new.putpixel((i,j),(r,g,b))
	new.save('new.jpg')		#生成新图

if __name__ == '__main__':
	url=raw_input('please input pic url ：')
	ima(url)
```