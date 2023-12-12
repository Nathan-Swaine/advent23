xSpace, ySpace = zip(*[(x,y) for y,r in enumerate(open('data.txt'))
  for x,c in enumerate(r) if c == '#']) #if str read in is a galaxy then enumerate

#get coords for two #, then calc absolute distance between and return {(x2-x1)^2 + (y2-y1)^2}
    
def distance(ps):
    ps = [sum((l, 1)
          [p in ps] for p in range(p)) # p in ps as tuple is bad 
            for p in ps]
    return sum(abs(a-b) for a in ps for b in ps)//2 #calc space
#452 galaxies
#19148 .'s

for l in 2, 1_000_000: print(sum(map(distance, [xSpace, ySpace])))