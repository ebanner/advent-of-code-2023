fileName = "input.txt"
#fileName = "input2.txt"

nums = set([
    "one",
    "two",
    "three",
    "four",
    "five",
    "six", 
    "seven",
    "eight",
    "nine",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
])

m = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "ruof": 4,
    "evif": 5,
    "xis": 6,
    "neves": 7,
    "thgie": 8,
    "enin": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

rnums = set([x[::-1] for x in nums])

def get_first_digit(line):
    idx = len(line)
    for n in nums:
        i = line.find(n)
        if i != -1 and i < idx:
            idx = i
            val = m[n]
    return val

def get_last_digit(line):
    idx = len(line)
    for n in rnums:
        i = line.find(n)
        if i != -1 and i < idx:
            idx = i
            val = m[n]
    return val

result = 0
with open(fileName) as f:
    for line in f:
        val = 0
        f = get_first_digit(line)
        val += 10 * f
        l = get_last_digit(line[::-1])
        val += l
        result += val
        print(f"line: {line}, f: {f}, l: {l}")

print(result)