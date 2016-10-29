def getWordsPosition():
    filename = "words_position.txt"
    with open(filename, "r") as f:
        positions = []
        data = f.read()
        data = data.split("\n")
        for each in data:
            positions.append(int(each))

    return positions

def getWordDensity(positions, index):
    counts = 0
    for position in positions[index:]:

        if position < positions[index] + 107:
            counts += 1
        else:
            break
    """
        print("position = %d positions[index] = %d\n" % \
        (position, positions[index]))
    """
    return counts

def getWordsDensity(positions):
    words_den = []
    positions_length = len(positions)
    for i in range(positions_length):
        print("still working...i = %d ; Leave %d num" % (i, positions_length - i))
        words_den.append(getWordDensity(positions, i))

    return words_den

def saveResult(words_den):
    filename = "words_den.txt"
    with open(filename, "w+") as f:
        for each in words_den:
            f.write(str(each) + "\n")

    return None

if __name__ == '__main__':
    positions = getWordsPosition()
    positions = set(positions)
    positions = list(positions)
    positions.sort()

    with open("sort_words_position.txt", "w+") as f:
        for each in positions:
            f.write(str(each) + "\n")

    words_den = getWordsDensity(positions)
    saveResult(words_den)

