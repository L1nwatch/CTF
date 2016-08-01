### 题目描述
一只小羊跳过了栅栏，两只小样跳过了栅栏，一坨小羊跳过了栅栏...

tn c0afsiwal kes,hwit1r  g,npt  ttessfu}ua u  hmqik e {m,  n huiouosarwCniibecesnren.

### write up
栅栏密码, 题目说得很清楚了, 自己用 Python 写个脚本解决, 栅栏数为 5, 解密后得到明文:

`the anwser is wctf{C01umnar},if u is a big new,u can help us think more question,tks.`

```python
from itertools import zip_longest

__author__ = '__L1n__w@tch'


class RailFence:
    """
    栅栏密码, 初始化需要一个栏数, 内含加密操作与解密操作, 以及内置使用的分组操作
    """

    def __init__(self, number):
        self.num = number  # 规定几个一组

    def encrypt(self, text_decrypted):
        """
        栅栏密码的加密操作
        :param text_decrypted: "WoShiZhongWenBuShiYingWen"
        :return: 栅栏数为 5 时的加密结果, "WZWSnohehgSoniWhnBYeiguin"
        """
        if len(text_decrypted) % self.num != 0:
            raise RuntimeError("待加密的长度需要是栏数的倍数")
        text_encrypted = str()
        groups = RailFence.__divide_group(text_decrypted, self.num)

        for order in range(self.num):
            for each_group in groups:
                text_encrypted += each_group[order]

        return text_encrypted

    def decrypt(self, text_encrypted):
        """
        栅栏密码的解密操作
        :param text_encrypted: "WZWSnohehgSoniWhnBYeiguin"
        :return: 栅栏数为 5 时的解密结果, "WoShiZhongWenBuShiYingWen"
        """
        if len(text_encrypted) % self.num != 0:
            raise RuntimeError("待解密的密文应该是栅栏数的倍数")
        text_decrypted = str()
        groups = RailFence.__divide_group(text_encrypted, len(text_encrypted) // self.num)

        for order in range(len(text_encrypted) // self.num):
            for each_group in groups:
                text_decrypted += each_group[order]

        return text_decrypted

    @staticmethod
    def __divide_group(text, size):
        """
        对字符串进行分组操作
        :param text: "abcdefghi"
        :param size: 3
        :return: ["abc", "def", "ghi"]
        """
        args = [iter(text)] * size
        blocks = list()
        for block in zip_longest(*args):
            blocks.append("".join(block))

        return blocks


if __name__ == "__main__":
    num = 5
    rail_fence = RailFence(num)
    cipher_text = "tn c0afsiwal kes,hwit1r  g,npt  ttessfu}ua u  hmqik e {m,  n huiouosarwCniibecesnren."
    plaintext = rail_fence.decrypt(cipher_text)
    print("plaintext = {0}\n{num}-cipher_text = {1}".format(plaintext, cipher_text, num=num))
```
