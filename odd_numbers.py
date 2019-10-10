def getOddNumbers(start, end):
    result = []
    for x in range(start, end, -1):
        if x % 2 is not 0:
            result.append(str(x))
    return result

def writeToFile(numbers):
    file = open('numbers.txt', 'w+') # Open A File in Write Mode
    file.write(','.join(numbers)) # Write All The nuumbers to a file seperated by a comma
    file.close()


def readFromFile():
    file = open('numbers.txt')
    text = file.readlines()[0]
    file.close()
    return text.split(',')


def main():
    numbers = getOddNumbers(100, 0)
    writeToFile(numbers)
    numbers = readFromFile()
    numbers_asc = sorted(numbers)
    print(numbers_asc)
main()
