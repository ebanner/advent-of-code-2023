file = "input.txt"
result = 0
with open(file) as f:
    for line in f:
        card = line.split(":")[1]
        my_nums, winning_nums = card.split("|")

        # The str.split() method without an argument splits on whitespace
        my_nums = set(my_nums.strip().split())
        winning_nums = set(winning_nums.strip().split())

        # Getting the intersection of 2 sets
        matches = len(my_nums.intersection(winning_nums))
        if matches:
            result += 2 ** (matches - 1)

print(f"RESULT: {result}")