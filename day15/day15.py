from functools import reduce
data = open('data.txt').read().strip().split(',')
char = lambda i, c: (i+ord(c)) * 17 % 256
hash = lambda s: reduce(char, s, 0)
print(sum(map(hash, data)))
boxes = [dict() for _ in range(256)]
for step in data:
  step_parts = step.strip('-').split('=') #should use match in this case but not supported in 3.9
  if len(step_parts) == 2:
    l, f = step_parts
    boxes[hash(l)][l] = int(f)
  elif len(step_parts) == 1:
    l = step_parts[0]
    boxes[hash(l)].pop(l, 0)

print(sum(i*j*f for i,b in enumerate(boxes, 1)
  for j,f in enumerate(b.values(), 1)))