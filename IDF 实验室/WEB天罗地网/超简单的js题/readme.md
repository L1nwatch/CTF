## 题目
这里这里→ http://ctf.idf.cn/game/web/42/index.php

## Write up
二话不说，查看网页源代码。发现变量用url加密过。使用unescape解码并输出，可以看到简单逻辑。由此可知，密码为4a33f9960a70cf7f947b249fea845d0c，输入后得到flag。

## 自己的解法
利用firebug，打开网页后刷新一下，在脚本那里，选择 `index.php line 12 > eval`，然后可以看到这段代码：

```javascript
function checkSubmit() {
    var a = document.getElementById("password");
    if ("undefined" != typeof a) {
        if ("89ba9e2016d70d356b7d55c42e0a7e91" == a.value) return ! 0;
        alert("Error");
        a.focus();
        return ! 1
    }
}
document.getElementById("levelQuest").onsubmit = checkSubmit;
```

然后复制粘贴 89ba9e2016d70d356b7d55c42e0a7e91 即可得到。。。
wctf{webclieNt_c0py}