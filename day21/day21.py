topSet = {i+j*1j:c for i,r in enumerate(open('data.txt'))
              for j,c in enumerate(r) if c in '.S'}

finished = []
notchecked = {x for x in topSet if topSet[x]=='S'}
subset = lambda x: complex(x.real%131, x.imag%131)

for s in range(3 * 131):
  if s == 64: print(len(notchecked))
  if s%131 == 65: finished.append(len(notchecked))

  notchecked = {p+d for d in {1, -1, 1j, -1j}
    for p in notchecked if subset(p+d) in topSet}

f = lambda n,a,b,c: a+n*(b-a+(n-1)*(c-b-b+a)//2)
print(f(26501365 // 131, *finished))