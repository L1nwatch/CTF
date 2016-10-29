def getWordsPosition():
    filename = "sort_words_position.txt"
    positions = []
    with open(filename, "r") as f:
        data = f.read()
        data = data.split("\n")
        for each in data:
            positions.append(int(each))

    return positions

def getString():
    filename = "whoiswoldy.txt"
    with open(filename, "r") as f:
        data = f.read()

    return data

if __name__ == '__main__':
    positions = getWordsPosition()
    string = getString()
    counts = 0
    for each in positions:
        counts += 1
#        if counts % 100 == 0:
#            input("input anything to continue:")
        if string[each:each+20].find("what") != -1:
            print(string[each:each+20])
            print("position = ", each)
