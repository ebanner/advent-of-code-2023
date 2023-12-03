#infile = "sampleinput.txt"
infile = "input.txt"

result, red, green, blue = 0, 12, 13, 14
with open(infile) as f:
    for line in f:
        game_num = int(line.split(":")[0].split(" ")[1])
        games = [x.split(",") for x in line.split(":")[1].split(";")]
        possible = True
        for game in games:
            for draw in game:
                scount, color = draw.strip().split(" ")
                count = int(scount)
                if (color == "red" and count > red) or (color == "blue" and count > blue) or (color == "green" and count > green):
                    possible = False
        if possible:
            result += game_num
print(result)
