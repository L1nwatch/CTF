## 问题
这里这里→ http://ctf.idf.cn/game/web/43/index.php

## Write Up
看完题解解得。

题解说这是个加密函数，让我们自己把解密函数写出来就行了。

把网页保存到本地（浏览器右键保存网页即可），看着加密函数写出解密函数；

```javascript
/**
 * Pseudo md5 hash function
 * @param {string} string
 * @param {string} method The function method, can be 'ENCRYPT' or 'DECRYPT'
 * @return {string}
 */
function pseudoHash(string, method) {
  // Default method is encryption
  if (!('ENCRYPT' == method || 'DECRYPT' == method)) {
    method = 'ENCRYPT';
  }
  // Run algorithm with the right method
  if ('ENCRYPT' == method) {
    // Variable for output string
    var output = '';
    // Algorithm to encrypt
    for (var x = 0, y = string.length, charCode, hexCode; x < y; ++x) {
      charCode = string.charCodeAt(x);
      if (128 > charCode) {
        charCode += 128;
      } else if (127 < charCode) {
        charCode -= 128;
      }
      charCode = 255 - charCode;
      hexCode = charCode.toString(16);
      if (2 > hexCode.length) {
        hexCode = '0' + hexCode;
      }

      output += hexCode;
    }
    // Return output
    return output;
  }
//----------------------------------------以下是解密部分--------------------------------------------
  else if ('DECRYPT' == method) {
    var destring = '';
    for (var i = 0; i < string.length - 1; i=i+2) {
      strCode = string.substring(i,i+2);
      var strInt = parseInt(strCode,16);
      strInt = 255 - strInt;
      if (strInt > 127) {
        strInt -= 128;
      }else if (strInt < 128) {
        strInt += 128;
      }
      destring += String.fromCharCode(strInt);
    }
    return destring;
  }
}
document.write(pseudoHash('4a191b4f4d4b4a19491c461b1b1d1b194c1a19194f194a4f4a46484a1d491e48','DECRYPT'));
// document.getElementById('password').value = pseudoHash('4a191b4f4d4b4a19491c461b1b1d1b194c1a19194f194a4f4a46484a1d491e48', 'DECRYPT');
```

【PS】直接复制的题解的，注意里面的4a啥的不一样了，然后把新的加密后的字符串复制进去，用浏览器打开后得到一串东西，再回到那个正常的界面点个走你，即可得到密码
wctf{jS_decRypt__Eaaasy}

### Python Decode

```python
s = '191a1c1d191e4747194c494b1b194c4b1c4c4d484f4d1d494d194e4e1e481b46'
def decode(s):
    charcode = []
    i = 0
    while i<len(s):
        charcode.append(int(s[i:i+2],16))
        i = i + 2
    charcode = [255-i for i in charcode]

    chars = []
    for i in charcode:
        if 127<i+128<255:
            chars.append(i+128)
        elif 0<i-128<128:
            chars.append(i-128)
        else: chars.append(i)
    result = [chr(i) for i in chars]
    return ''.join(result)

t = decode(s)
print(t)
```

