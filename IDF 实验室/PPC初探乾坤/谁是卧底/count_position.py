def get_data():
    filename = "whoiswoldy.txt"
    with open(filename, "r") as f:
        data = f.read()

    return data

def get_position():
    filename = "words_Position.txt"
    with open(filename, "r") as f:
        temp = f.read()
        temp = temp.split("\n")
        positions = []
        for each in temp:
            positions.append(int(each))

    return positions

def count_position(positions):
    counts = []

    length = len(positions)
    for i in range(length):
        count = 0
        temp = positions[i:]
        for each in temp:
            if each > (positions[i] + 100):
                break
            else:
                count += 1
        counts.append(count)

    return counts

if __name__ == '__main__':
    positions = get_position()
    positions.sort()
    counts = count_position(positions)
    data = get_data()

    for i in range(len(counts)):
        if counts[i] > 8:
            print("counts = %d position = %d" % (counts[i],positions[i]))
            print("string = %s" % data[positions[i]:positions[i] + 20])

