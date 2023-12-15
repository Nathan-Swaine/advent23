pos = list(map(str.split, open('data.txt').read().split('\n\n')))
#set pos as a mapped delimited list of input data

def mirrorFunc(p):
  for i in range(len(p)):
    #is there exactly s in p where c != d for l,m in zip(p[i-1::-1], p[i:])
    if sum(c != d for l,m in zip(p[i-1::-1], p[i:])
      for c,d in zip(l, m)) == s: return i
  else: return 0

for s in 0,1: print(sum(100 * mirrorFunc(p) + mirrorFunc([*zip(*p)]) for p in pos))
#f([*zip(*p)]) check in one direction then rotate the input and check again
#s is global so used in both 