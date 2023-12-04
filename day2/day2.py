from collections import Counter
from functools import reduce
from operator import mul, or_
thres = Counter({"red":12, "green":13, "blue":14})
tot_1 = 0
tot_2 = 0
with open("input.txt", "r") as f:
  for game in f:
    game_id, draws = game.strip().split(": ") # split input at the ':' character
    game_id = int(game_id.split(" ")[1]) # str to int conversion
    draws = [[c.split(" ") for c in d.split(", ")] for d in draws.split("; ")] # further split input string into colored cubes and the associted number of cubes per color per game
    draws = [Counter({c[1]:int(c[0]) for c in d}) for d in draws]
    tot_1 += all(all(draws[i][color] <= thres[color] for color in draws[i]) for i in range(len(draws))) * game_id # check if all counters in the drawers are below the threshold
    tot_2 += reduce(mul, reduce(or_, draws).values()) # calc the sum of the product of the number of cubes per color per game min
    
print(1, tot_1)
print(2, tot_2)