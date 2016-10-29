def getWordsDensity():
    filename = "words_den.txt"
    with open(filename, "r") as f:
        words_den = []
        data = f.read()
        data = data.split("\n")
        for each in data:
            words_den.append(int(each))

    return words_den

def getString():
    filename = "whoiswoldy.txt"
    with open(filename, "r") as f:
        data = f.read()

    return data

def getWordsPosition():
    filename = "sort_words_position.txt"
    positions = []
    with open(filename, "r") as f:
        data = f.read()
        data = data.split("\n")
        for each in data:
            positions.append(int(each))

    return positions

def getIndexs(words_den, max_density):
    indexs = []
    try:
        while True:
            index = words_den.index(max_density)
            if len(indexs) < 1:
                indexs.append(index)
            else:
                indexs.append(index + indexs[-1] + 1)
#            print("positions = %d" % positions[index])
#            print(string[positions[index]:positions[index] + 100])
            words_den = words_den[index + 1:]

    except Exception:
        pass

    return indexs

def printSentence(string, indexs):
    positions = getWordsPosition()
    for each in indexs:
        position = positions[each]
        print(string[position:position+100])

    return None

if __name__ == '__main__':
    words_den = getWordsDensity()
    max_density = max(words_den)
    string = getString()
    indexs = getIndexs(words_den, max_density)
    printSentence(string, indexs)
    input("input anykey to quit:")
