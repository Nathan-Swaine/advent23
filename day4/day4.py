import time
start_time = time.time()
file = open("data.txt").readlines()
score = 0
cards = [1 for _ in file]
for index, line in enumerate(file):
  line = line.split(":")[1] #get card num
  winning, drawn = line.split("|") # split into winning | your numbers
  winning, drawn = winning.split(), drawn.split() #break winning, drawn into array such that winning[1,2,3] and drawn[1,2,3]
  n = len(set(winning) & set(drawn)) # what is the length of the intersection of winning and drawn
  if n > 0: # if its greater than 0 then we have a winning card
    score += 2 ** (n - 1) # add 2^(n-1) to the score
  for i in range(n):
    cards[index + i + 1] += cards[index]

end_time = time.time()
execution_time = (end_time - start_time) * 1000  # convert to milliseconds

print("Execution time:", execution_time, "milliseconds\n")
print(score, sum(cards))

