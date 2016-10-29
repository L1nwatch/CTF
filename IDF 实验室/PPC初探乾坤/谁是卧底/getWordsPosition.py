def getWords():
    filename = "words.txt"
    with open(filename, "r") as f:
        data = f.read()
        data = data.split("\n")
        data = set(data)

    return data

def getWordPosition(word, string):
    positions = []
    word_length = len(word)
    if word_length > 2:
        position = string.find(word)
        while position != -1:
            if len(positions) > 0:
                positions.append(position + positions[-1] + word_length)
            else:
                positions.append(position)
            string = string[position + word_length:]
            position = string.find(word)

    return positions

def getString():
    filename = "whoiswoldy.txt"
    with open(filename, "r") as f:
        data = f.read()
    return data

def createPositionList(words, string):
    positions = []
    times = len(words)
    for word in words:
        times -= 1
        print("still working....word = %s;Leave %d words" % \
              (word, times))
        position = getWordPosition(word, string)
        if len(position) > 0:
            positions.extend(position)

    return positions

def saveResult(positions):
    filename = "words_position.txt"
    with open(filename, "w+") as f:
        for each in positions:
            f.write(str(each) + "\n")

    print("Save Result success!")
    return None

if __name__ == '__main__':
    words = getWords()
    string = getString()
    positions = createPositionList(words, string)
    saveResult(positions)
