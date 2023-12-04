infile = "sampleinput.txt"
infile = "input.txt"
result = 0
with open(infile) as f:
    for line in f:
        game_num = int(line.split(":")[0].split(" ")[1])
        games = [x.split(",") for x in line.split(":")[1].split(";")]
        red, blue, green = 0, 0, 0
        for game in games:
            for draw in game:
                scount, color = draw.strip().split(" ")
                count = int(scount)
                if color == "red":
                    red = max(red, count)
                if color == "blue":
                    blue = max(blue, count)
                if color == "green":
                    green = max(green, count)
        result += red * blue * green
print(result)
