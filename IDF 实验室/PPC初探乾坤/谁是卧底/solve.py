"""
基本思路：
统计文件中单词出现的位置
找出这些位置密集的地方

解决思路：
将单词出现的位置全部添加到一个列表中，即列表表现为
List = [ 1,2,3,80,100 ]#每个数字均代表存在单词的位置
先把这个列表搞出来再说
"""

"""
our死循环了
"""
def create_list(data):
#    dictionary_name = "common_English_Word_Dictionary.txt"
#    dictionary_name = "short_common_English_Word_Dictionary.txt"
    dictionary_name = "new_short_common_English_Word_Dictionary.txt"
#    dictionary_name = "temp_dictionary.txt"
#   O(3599)
    with open(dictionary_name, "r") as f:
        dictionary = f.read()
        dictionary = dictionary.split("\n")
        dictionary = set(dictionary)    #字典文件不太好，有重复了，所以就改用集合

#   O(3599 * len(n))
    List = []
    for each in dictionary:
        if len(each) < 4:
            continue
        temp = data
        result = temp.find(each)
        while result != -1:
            List.append(result)
            print("word = ", each, " position = ", result)
            result += len(each)
            temp = data[result:]
            result_new = temp.find(each)
            if result_new == -1:
                break
            else:
                result += result_new

    return List

def get_data():
    filename = "whoiswoldy.txt"
#    filename = "temp.txt"
    with open(filename, "r") as f:
        data = f.read()

    return data

def find_area(List):
    List_count = []
    temp_List = List
    temp_List.sort()
    for i in range(len(temp_List)):
        counts = 0
        number = temp_List[i] + 107
        next_list = temp_List[i:]
        for each in next_list:
            if each > number:
                break
            else:
                counts += 1
        List_count.append(counts)

#    print(temp_List)
#    print(List_count)
    temp = List_count
    temp.sort(reverse = True)
    for i in range(10):
        position = List_count.index(temp[i])
        print(position)
        print(data[position:position+100])
        print("分割线\n\n")
        with open("result.txt", "a+") as f:
            f.write(data[position:position+100])
#    print(max_counts)

    return List_count.index(max_counts)

if __name__ == '__main__':
    data = get_data()
    List = create_list(data)
    with open("list_result.txt", "w") as f:
        for each in List:
            f.write(str(each))
            f.write(" ")
#    find_area(List)
    input()
