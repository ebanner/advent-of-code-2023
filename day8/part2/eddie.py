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


def move(nodes, instruction, map):
    new_nodes = []
    for node in nodes:
        left_node, right_node = map[node]
        if instruction == 'L':
            new_node = left_node
        else:
            assert instruction == 'R'
            new_node = right_node
        new_nodes.append(new_node)
    return new_nodes


def follow_instructions(nodes, instructions, map):
    num_moves = 0
    for instruction in instructions:
        nodes = move(nodes, instruction, map)
        num_moves += 1
        if termination_status(nodes):
            return True, nodes, num_moves
    return False, nodes, num_moves


def termination_status(nodes):
    for node in nodes:
        if not node.endswith('Z'):
            return False
    return True


def get_start_nodes(map):
    nodes = map.keys()
    start_nodes = [node for node in nodes if node.endswith('A')]
    return start_nodes


if __name__ == '__main__':
    lines = get_lines()
    instructions = get_instructions(lines)
    map = get_map(lines)
    start_nodes = get_start_nodes(map)

    num_moves = 0
    nodes = start_nodes
    total_moves = 0
    from tqdm import tqdm
    for i in tqdm(range(1_000_000_000)):
        found, nodes, num_moves = follow_instructions(nodes, instructions, map)
        total_moves += num_moves
        if found:
            break

    print(total_moves)

