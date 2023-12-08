import time
start_time = time.time()
def evaluate(line):
  cards, bid = line.split() # deconstruct line 
  cards = cards.translate(str.maketrans('TJQKA', face)) # assumings that there are no overlapping strings like eightwo eight two
  best = max(type(cards.replace('0', r)) for r in cards)
  return best, cards, int(bid)

def type(cards):
  return sorted(map(cards.count, cards), reverse=True) # return list  contating all items from map(cards.count, cards) 

for face in 'ABCDE', 'A0CDE':
  print(sum(rank * bid for rank, (*_, bid) in
    enumerate(sorted(map(evaluate, open('data.txt'))), start=1)))
    

end_time = time.time()
execution_time = (end_time - start_time) * 1000  # convert to milliseconds

print("Execution time:", execution_time, "milliseconds\n")
# https://en.wikipedia.org/wiki/Entropy_(information_theory)
# five of a kind: 5+5+5+5+5 = 25,
# four of a kind: 4+4+4+4+1 = 17,
# full house: 3+3+3+2+2 = 13,
# three of a kind: 3+3+3+1+1 = 11,
# then use just sorted () to find the ranking