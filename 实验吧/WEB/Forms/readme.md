# 题目

似乎有人觉得PIN码是不可破解的，让我们证明他是错的。

格式：ctf{}

解题链接： [http://ctf5.shiyanbar.com/10/main.php](http://ctf5.shiyanbar.com/10/main.php)

# WriteUp

学一下sqlmap怎么post注入：

http://www.myhack58.com/Article/html/3/8/2012/35821.htm

参考WriteUp：

http://www.shiyanbar.com/ctf/writeup/413

主要是一开始想着进行POST注入，但是用 `sqlmap -u url --data PIN=test` 说是非注入点，所以就没思路了。

看了WriteUP之后意识到先利用隐藏字段获取源码先，利用Firefox的hackbar：

```php
$a = $_POST["PIN"];

if ($a == -19827747736161128312837161661727773716166727272616149001823847) {

    echo "Congratulations! The flag is $flag";

} else {

    echo "User with provided PIN not found."; 

}
```

额，直接复制那一串数字回车就得到FLAG了，这算啥算啥算啥！！！