def get_lines():
    import sys
    lines = [line.strip() for line in sys.stdin.readlines()]
    return lines


def get_instructions(lines):
    instructions = lines[0]
    return instructions


def parse_line(line):
    node = line[0:3]
    left_node = line[7:10]
    right_node = line[12:15]
    return node, [left_node, right_node]


def get_map(lines):
    map = {}
    for line in lines[2:]:
        node, [left, right] = parse_line(line)
        map[node] = (left, right)
    return map


def move(node, instruction, map):
    left_node, right_node = map[node]
    if instruction == 'L':
        return left_node
    else:
        assert instruction == 'R'
        return right_node


def follow_instructions(node, instructions, map):
    for instruction in instructions:
        node = move(node, instruction, map)
    return node


if __name__ == '__main__':
    lines = get_lines()
    instructions = get_instructions(lines)
    map = get_map(lines)

    num_moves = 0
    node = 'AAA'
    for _ in range(2):
        node = follow_instructions(node, instructions, map)
        num_moves += len(instructions)
        if node == 'ZZZ':
            break

    print(num_moves)

