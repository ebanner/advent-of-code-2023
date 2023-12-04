file = "input.txt"

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
                elif c != ".":
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

def is_part(num) -> bool:
    # num is a dict{ "name": str, "points": list[list[int]] }
    points = num["points"]
    for s in symbols:
        nbrs = get_neighbors(s[:2])
        for p in points:
            if p in nbrs:return True
    return False

def calculate_sum() -> int:
    result = 0
    for n in nums:
        if is_part(n):
            result += int(n["value"])
    return result
nums, symbols = parse_input()

print(f"RESULT: {calculate_sum()}")