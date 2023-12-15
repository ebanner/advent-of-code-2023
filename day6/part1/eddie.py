def get_lines():
    import sys
    lines = [line.strip() for line in sys.stdin.readlines()]
    return lines


def get_times(lines):
    times_str = lines[0]
    times = [int(time) for time in times_str.split()[1:]]
    return times


def get_distances(lines):
    distance_str = lines[1]
    distance = [int(time) for time in distance_str.split()[1:]]
    return distance


def get_num_ways(time, record):
    num_ways = 0
    for hold in range(time+1):
        distance = time*hold - hold**2
        if distance > record:
            num_ways += 1
    return num_ways



if __name__ == '__main__':
    lines = get_lines()
    times = get_times(lines)
    distances = get_distances(lines)

    num_ways_prod = 1
    for time, distance in zip(times, distances):
        num_ways = get_num_ways(time, distance)
        num_ways_prod *= num_ways
    print(num_ways_prod)
