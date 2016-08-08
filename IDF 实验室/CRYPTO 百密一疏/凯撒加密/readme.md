# 题目描述
大概就是这样吧，不能告诉你再多了。。

`U8Y]:8KdJHTXRI>XU#?!K_ecJH]kJG*bRH7YJH7YSH]*=93dVZ3^S8*$:8"&:9U]RH;g=8Y!U92'=j*$KH]ZSj&[S#!gU#*dK9\.`

# write up:
就是先移一下位，然后用base64解密试试看能不能解得可读的明文：

最终偏移为15，明文为：`the flag is wctf{kaisa_jiaaaaami},plz flow my weibo,http://weibo.com/woldy`

## Python Script
```Python
# -*- coding: utf-8 -*-
# version: Python3.X
__author__ = '__L1n__w@tch'

# Cipher text: U8Y]:8KdJHTXRI>XU#?!K_ecJH]kJG*bRH7YJH7YSH]*=93dVZ3^S8*$:8"&:9U]RH;g=8Y!U92'=j*$KH]ZSj&[S#!gU#*dK9\.

import base64


def main():
    cipher_text = r"""U8Y]:8KdJHTXRI>XU#?!K_ecJH]kJG*bRH7YJH7YSH]*=93dVZ3^S8*$:8"&:9U]RH;g=8Y!U92'=j*$KH]ZSj&[S#!gU#*dK9\."""
    for shift in range(26):
        print("Shift {0}:".format(shift))
        string = ""
        for each in cipher_text:
            string += chr(ord(each) + shift)
        try:
            print(base64.b64decode(string))
        except:
            pass


if __name__ == "__main__":
    main()
```