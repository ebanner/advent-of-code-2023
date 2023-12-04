from collections import defaultdict
file = "input.txt"

cards = defaultdict(int)

with open(file) as f:
    for line in f:
        card_num, card = line.split(":")
        card_num = card_num.split()[1]
        my_nums, winning_nums = card.split("|")

        cards[int(card_num)] += 1

        # The str.split() method without an argument splits on whitespace
        my_nums = set(my_nums.strip().split())
        winning_nums = set(winning_nums.strip().split())

        # Getting the intersection of 2 sets
        matches = len(my_nums.intersection(winning_nums))
        for i in range(1, int(matches + 1)):
            cards[int(card_num) + i] += cards[int(card_num)]

result = sum([x for x in cards.values()])
print(f"RESULT: {result}")