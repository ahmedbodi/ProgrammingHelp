def minmax(numbers):
    lowest = None
    highest = None
    for number in numbers:
        if number < lowest or lowest is None:
            lowest = number
        if number > highest or highest is None:
            highest = number
    return lowest, highest

min, max = minmax([1,2,3,4,5,6,7,8,9,10])
print(min, max)
