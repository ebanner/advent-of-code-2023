from functools import reduce
file, result = "input.txt", 0

def parse_input():
    nums = []
    symbols = []
    with open(file) as f:
        row = 0
        for line in f:
            prev = ""
            current_num = {
                "value": "",
                "points": []
            }
            for idx, c in enumerate(line.strip()):
                if c.isnumeric():
                    if not prev.isnumeric():
                        current_num = {
                            "value": c,
                            "points": [(row,idx)]
                        }
                    else: # prev isnumeric()
                        current_num["value"] += c
                        current_num["points"].append((row,idx))
                elif c == "*":
                    symbols.append((row,idx,c))
                if not nums or current_num["value"] != nums[-1]["value"]:
                    nums.append(current_num)
                prev = c
            row += 1
    return nums, symbols

def get_neighbors(cell):
    result = []
    x, y = cell
    result.append(( x-1, y-1 ))
    result.append(( x  , y-1 ))
    result.append(( x+1, y-1 ))
    result.append(( x-1, y   ))
    result.append(( x+1, y   ))
    result.append(( x-1, y+1 ))
    result.append(( x  , y+1 ))
    result.append(( x+1, y+1 ))
    return result

def is_gear(gear):
    nbrs = get_neighbors(gear[:2])
    result_set = set()
    for n in nums:
        value, points = n["value"], n["points"]
        if set(nbrs).intersection(set(points)):
            result_set.add(int(value))
    return len(result_set) == 2, result_set

nums, symbols = parse_input()

for s in symbols:
    s_is_gear, values = is_gear(s)
    if s_is_gear:
        result += reduce(lambda a, b: a * b, values)

print(f"RESULT: {result}")