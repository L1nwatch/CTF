# 题目描述
子曰：“自行束修以上，吾未尝无诲焉。”

ABAAAABABBABAAAABABAAABAAAAAABAAAAAAAABAABBBAABBAB

# write up
培根密码, 写个对应表就行了.

```python
dictionary_1 = {
    "A":"aaaaa",
    "B":"aaaab",
    "C":"aaaba",
    "D":"aaabb",
    "E":"aabaa",
    "F":"aabab",
    "G":"aabba",
    "H":"aabbb",
    "I":"abaaa",
    "J":"abaab",
    "K":"ababa",
    "L":"ababb",
    "M":"abbaa",
    "N":"abbab",
    "O":"abbba",
    "P":"abbbb",
    "Q":"baaaa",
    "R":"baaab",
    "S":"baaba",
    "T":"baabb",
    "U":"babaa",
    "V":"babab",
    "W":"babba",
    "X":"babbb",
    "Y":"bbaaa",
    "Z":"bbaab"
    }
dictionary_2 = {
    "a":"AAAAA",
    "g":"AABBA",
    "n":"ABBAA",
    "t":"BAABA",
    "b":"AAAAB",
    "h":"AABBB",
    "o":"ABBAB",
    "u":"BAABB",
    "v":"BAABB",
    "c":"AAABA",
    "i":"ABAAA",
    "j":"ABAAA",
    "p":"ABBBA",
    "w":"BABAA",
    "d":"AAABB",
    "k":"ABAAB",
    "q":"ABBBB",
    "x":"BABAB",
    "e":"AABAA",
    "l":"ABABA",
    "r":"BAAAA",
    "y":"BABBA",
    "f":"AABAB",
    "m":"ABABB",
    "s":"BAAAB",
    "z":"BABBB"
    }

#反转键值
bacon_dict1 = dict(zip(dictionary_1.values(), dictionary_1.keys()))
bacon_dict2 = dict(zip(dictionary_2.values(), dictionary_2.keys()))

string = "ABAAAABABBABAAAABABAAABAAAAAABAAAAAAAABAABBBAABBAB"

print("dictionary1:")
for i in range(10):
    tmp = string[i * 5 : ( i + 1 ) * 5]
    print(bacon_dict1[tmp.lower()], end = "")

print("\n")
print("dictionary2:")
for i in range(10):
    tmp = string[i * 5 : ( i + 1 ) * 5]
    print(bacon_dict2[tmp], end = "")
```