## 题目

请看这里：  http://pan.baidu.com/s/1jGpB8DS

## write up

使用python反编译工具，比如http://tool.lu/pyc/

得到代码实现：

```python
def encrypt(key, seed, string):
    rst = []
    for v in string:
        rst.append((ord(v) + seed ^ ord(key[seed])) % 255)
        seed = (seed + 1) % len(key)
    
    return rst

if __name__ == '__main__':
    print("Welcome to idf's python crackme")
    flag = input('Enter the Flag: ')
    KEY1 = 'Maybe you are good at decryptint Byte Code, have a try!'
    KEY2 = [
        124,
        48,
        52,
        59,
        164,
        50,
        37,
        62,
        67,
        52,
        48,
        6,
        1,
        122,
        3,
        22,
        72,
        1,
        1,
        14,
        46,
        27,
        232]
    en_out = encrypt(KEY1, 5, flag)
    if KEY2 == en_out:
        print('You Win')
    else:
        print('Try Again !')
```

逆向：

```python
def decrypt_each(key, seed, KEY2):
    answer = ""
    for each in KEY2:
        password = each
        for i in range(128):
            result = (i + seed ^ ord(key[seed])) % 255
            if password == result:
                answer += chr(i)
                break
        seed = (seed + 1) % len(key)

    return answer

if __name__ == '__main__':
    KEY1 = 'Maybe you are good at decryptint Byte Code, have a try!'
    KEY2 = [
    124,
    48,
    52,
    59,
    164,
    50,
    37,
    62,
    67,
    52,
    48,
    6,
    1,
    122,
    3,
    22,
    72,
    1,
    1,
    14,
    46,
    27,
    232]
    answer = decrypt_each(KEY1, 5, KEY2)
    print(answer)
```

