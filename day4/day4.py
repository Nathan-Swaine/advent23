f = open("data.txt").readlines()
s = 0
cards = [1 for _ in f]
for index, line in enumerate(f):
  line = line.split(":")[1] #get card num
  a, b = line.split("|") # split into winning | your numbers
  a, b = a.split(), b.split() #break a,b into array such that a[1,2,3] and b[1,2,3]
  n = len(set(a) & set(b)) # what is the length of the intersection of a and b
  if n > 0: # if its greater than 0 then we have a winning card
    s += 2 ** (n - 1) # add 2^(n-1) to the score
  for i in range(n):
    cards[index + i + 1] += cards[index]

print(s, sum(cards))