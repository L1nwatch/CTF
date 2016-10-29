def get_data():
    filename = "whoiswoldy.txt"
    with open(filename, "r") as f:
        data = f.read()

    return data

def create_list(data):
    dictionary_name = "new_short_common_English_Word_Dictionary.txt"
    with open(dictionary_name, "r") as f:
        dictionary = f.read()
        dictionary = dictionary.split("\n")
        dictionary = set(dictionary)    #字典文件不太好，有重复了，所以就改用集合

    List = []
    for each in dictionary:
        if len(each) < 2:
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

if __name__ == '__main__':
    data = get_data()
    List = create_list(data)
    print(type(List))
    with open("words_Position.txt", "w") as f:
        for each in List:
            f.write(str(each))
            f.write("\n")
