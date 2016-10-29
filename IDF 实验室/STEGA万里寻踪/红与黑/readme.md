## 题目
只给了一张图片:

![题目]()

## write up

看了writeUp后知道只要改变一下图片的曝光度就可以看到字符串了，还有些人用py把图片处理了一下。详看answer.py
自己是用PS把图片搞搞得到的：

![PS 调整得到]()

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