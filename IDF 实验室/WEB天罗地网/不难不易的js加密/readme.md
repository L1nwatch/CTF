## 问题
就是这里 → http://ctf.idf.cn/game/web/28

## write up
首先查看源码，是一堆看不懂的js代码（其实也不是完全看不懂），放进 http://tool.lu/js/ 解密一下，得到下面这堆：

```javascript
var a = prompt("输入你的flag吧，少年！", "");
var b = "f3373e36c677750779f5d04ff7885b3e";
var c = /.+_.+_.+/gi;
var d = 0x0;
var e = a.substr(0x8, 0x5);
if ($.md5(e) == b.replace(/7/ig, ++d).replace(/8/ig, d * 0x2)) {
	var f = a.substr(0x0 / d, 0x7);
	if (f.substr(0x5, 0x2) == "js" && $.md5(f.substr(0x0 / d, d + 0x3)) == "d0154d5048b5a5eb10ef1646400719f1") {
		r = a.substr(0xd);
		if (r.charCodeAt(d) - 0x19 == r.charCodeAt(++d) - 0x19 && r.charCodeAt(--d) - 0x19 == r.charCodeAt(--d)) {
			var g = String.fromCharCode(0x4f);
			g = g.toLowerCase() + g.toLowerCase();
			if (r.substr((++d) * 0x3, 0x6) == g.concat("easy") && c.test(a)) {
				d = String(0x1) + String(a.length)
			}
		}
	}
};
if (a.substr(0x4, 0x1) != String.fromCharCode(d) || a.substr(0x4, 0x1) == "z") {
	alert("额，再去想想。。")
} else {
	alert("恭喜恭喜！")
}
```

排版后是上面这个样子，用 http://jsfiddle.net/ 一步一步跑下来看懂程序：

```javascript
var b = "f3373e36c677750779f5d04ff7885b3e";
var d = 0;
b = b.replace(/7/ig, ++d).replace(/8/ig, d * 0x2);
document.write(b)
```

得到：

`f3313e36c611150119f5d04ff1225b3e`

一行一行分析代码，最终解密：

```javascript
var a = prompt("输入你的flag吧，少年！", "");
var b = "f3373e36c677750779f5d04ff7885b3e";
var c = /.+_.+_.+/gi;	//.是通配符，妹的！表明格式是???_???_???

/*
var str = "a_b_c";
var patt1 = /.+_.+_.+/gi;
var result = patt1.test(str);
document.write("Result: " + result);
*/

var d = 0x0;
var e = a.substr(8, 5);
if ($.md5(e) == b.replace(7, 1).replace(8, 2) {
	//md5(e) = f3313e36c611150119f5d04ff1225b3e
	//e = “jiami” == a[8:8+5-1]
	var f = a.substr(0, 7);
	if (f.substr(5, 2) == "js" && $.md5(f.substr(0, 4)) == "d0154d5048b5a5eb10ef1646400719f1") {
	//a[5:6] = “js”
	//a[0:3] = “wctf”
	r = a.substr(0xd);
	//r = “ctf???????”，错了这里，应该是r=a[13:],注意d是十六进制
	//charCodeAt() 方法可返回指定位置的字符的 Unicode 编码。这个返回值是 0 - 65535 之间的整数。		//unicode编码格式:\u0001
    //a[13] = ?
    //下面&&前，表示第14位和第15位是相等的，且这里++d了，使d变成2
	//&&后：14位-19 = 第13位，然而第13位已经知道是_了，所以?加19（0x19，更准确的说）得到14位和15位都是_+0x19
	//js打印一下：
    /*
    var tmp = "_".charCodeAt(0);
    var g = String.fromCharCode(tmp+0x19);
    document.write(g);
    */
	if (r.charCodeAt(d) - 0x19 == r.charCodeAt(++d) - 0x19 && r.charCodeAt(--d) - 0x19 == r.charCodeAt(--d)) {
		//执行完上面这句d变成了0
		var g = String.fromCharCode(0x4f);//g = O	//是字母O不是0

      /* 用 Python 看一下 \u004f 是什么
      >>> print("\u004f")
      >>> O
	  */
		g = g.toLowerCase() + g.toLowerCase();// g = oo
		if (r.substr((++d) * 0x3, 0x6) == g.concat("easy") && c.test(a)) {
			//d变成了1，
			//r.substr(3,6) == ooeasy == a[15:15 + 6 - 1]
			//c.test(a)?	表明a中含有c,现在看来c
			//test() 方法用于检测一个字符串是否匹配某个模式.
			d = String(0x1) + String(a.length)
			//d = “1”+“23”
			}
		}
	}
};
if (a.substr(0x4, 0x1) != String.fromCharCode(d) || a.substr(0x4, 0x1) == "z") {
//||后的那句表明string.fromCharcode(d) == 122?
//其实应该知道标准格式wctf{，所以应该直到a[4] = {,故此时d=123，推得len(a)=23
	alert("额，再去想想。。")
} else {
	alert("恭喜恭喜！")
}
```

综上，字符依次为：
0 w
1 c
2 t
3 f
4 {
5 j
6 s
7 _
8 j
9 i
10 a
11 m
12 i
13 _
14 x
15 x
16 o
17 o
18 e
19 a
20 s
21 y
22 }


