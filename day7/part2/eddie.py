FIVE_OF_A_KIND = 'five-of-a-kind'
FOUR_OF_A_KIND = 'four-of-a-kind'
FULL_HOUSE = 'full-house'
THREE_OF_A_KIND = 'three-of-a-kind'
TWO_PAIR = 'two-pair'
ONE_PAIR = 'one-pair'
HIGH_CARD = 'high-card'


def get_lines():
    import sys
    lines = [line.strip() for line in sys.stdin.readlines()]
    return lines


def get_hands(lines):
    hands = []
    for line in lines:
        hand, _ = line.split()
        hands.append(hand)
    return hands


def get_hand_to_bid(lines):
    hand_to_bid = {}
    for line in lines:
        hand, bid = line.split()
        hand_to_bid[hand] = int(bid)
    return hand_to_bid


def get_counts(hand):
    counts = {}
    for card in hand:
        if card not in counts:
            counts[card] = 1
        else:
            counts[card] += 1
    return counts


def search(hand, i, check):
    if i == 4:
        return check(hand)
    elif hand[i] != 'J':
        return search(hand, i+1, check)
    else:
        for card in '23456789TJQKA':
            hand_ = list(hand)
            hand_[i] = card
            hand_ = ''.join(hand_)
            if search(hand_, i+1, check):
                return True
        return False


def is_five_of_a_kind(hand):
    def is_five_of_a_kind_check(hand):
        return list(sorted(get_counts(hand).values())) == [5]
    return search(hand, 0, is_five_of_a_kind_check)


def is_four_of_a_kind(hand):
    def is_four_of_a_kind_check(hand):
        return list(sorted(get_counts(hand).values())) == [1, 4]
    return search(hand, 0, is_four_of_a_kind_check)


def is_full_house(hand):
    def is_full_house_check(hand):
        return list(sorted(get_counts(hand).values())) == [2, 3]
    return search(hand, 0, is_full_house_check)


def is_three_of_a_kind(hand):
    def is_three_of_a_kind_check(hand):
        return list(sorted(get_counts(hand).values())) == [1, 1, 3]
    return search(hand, 0, is_three_of_a_kind_check)


def is_two_pair(hand):
    def is_two_pair_check(hand):
        return list(sorted(get_counts(hand).values())) == [1, 2, 2]
    return search(hand, 0, is_two_pair_check)


def is_one_pair(hand):
    def is_one_pair_check(hand):
        return list(sorted(get_counts(hand).values())) == [1, 1, 1, 2]
    return search(hand, 0, is_one_pair_check)


def is_high_card(hand):
    def is_high_card_check(hand):
        return list(sorted(get_counts(hand).values())) == [1, 1, 1, 1, 1]
    return search(hand, 0, is_high_card_check)



def get_type(hand):
    if is_five_of_a_kind(hand):
        return FIVE_OF_A_KIND
    elif is_four_of_a_kind(hand):
        return FOUR_OF_A_KIND
    elif is_full_house(hand):
        return FULL_HOUSE
    elif is_three_of_a_kind(hand):
        return THREE_OF_A_KIND
    elif is_two_pair(hand):
        return TWO_PAIR
    elif is_one_pair(hand):
        return ONE_PAIR
    elif is_high_card(hand):
        return HIGH_CARD
    else:
        raise Exception('unknown hand')


def reorder(hands):
    from functools import cmp_to_key

    card_to_value = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
        'J': 1,
    }
    for i in range(2, 10):
        card_to_value[str(i)] = i

    def custom_comparison_function(a, b):
        for i in range(5):
            if a[i] == b[i]:
                continue
            else:
                a_ = card_to_value[a[i]]
                b_ = card_to_value[b[i]]
                return -(a_ - b_)

    return list(sorted(hands, key=cmp_to_key(custom_comparison_function)))


def get_sorted_hands(hands):
    """
    [
        '32T3K',
        'T55J5',
        'KK677',
        'KTJJT',
        'QQQJA'
    ]

    """
    types = [
        FIVE_OF_A_KIND,
        FOUR_OF_A_KIND,
        FULL_HOUSE,
        THREE_OF_A_KIND,
        TWO_PAIR,
        ONE_PAIR,
        HIGH_CARD,
    ]
    piles = {type: [] for type in types}
    for hand in hands:
        type = get_type(hand)
        piles[type].append(hand)

    for type, pile in piles.items():
        piles[type] = reorder(pile)

    sorted_hands = []
    for type in types:
        pile = piles[type]
        sorted_hands.extend(pile)

    return sorted_hands


def get_ranks(sorted_hands):
    n = len(sorted_hands)
    ranks = list(range(n, 0, -1))
    return ranks


def get_winnings(sorted_hands, hand_to_bid):
    ranks = get_ranks(sorted_hands)

    winnings = 0
    for hand, rank in zip(sorted_hands, ranks):
        bid = hand_to_bid[hand]
        winnings += rank*bid
    return winnings


if __name__ == '__main__':
    lines = get_lines()
    hands = get_hands(lines)
    hand_to_bid = get_hand_to_bid(lines)

    sorted_hands = get_sorted_hands(hands)

    winnings = get_winnings(sorted_hands, hand_to_bid)

    print(winnings)

