import re
rot = lambda b:' '.join(map(''.join,zip(*(b.split())[::-1])))
ld = lambda b:sum(i for r in b.split() for i,c in enumerate(r,1) if c=='O')
cy = lambda d:re.sub('[.O]+',lambda m:''.join(sorted(m[0])), rot(d))
def powercycle(d,n,cache={}):
  for r in range(n):
    d = cy(cy(cy(cy(d))))
    if s:=cache.get(d,0):return cache[(n-s)%(r-s)+(s-1)] 
    cache |= {d:r, r:ld(rot(d))}
d = open('data.txt').read().replace('\n',' ')
print('part 1:', ld(cy(d)))
print('part 2:', powercycle(d,1_000_000_000))