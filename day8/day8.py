import math, re
direction, discard, *graph = open("data.txt").read().split('\n')
graph = {node: d for node, *d in [re.findall(r'\w+', s) for s in graph]}
start = [node for node in graph if node.endswith('A')]
def solve(location, i=0):
  while not location.endswith('Z'):
      dir = direction[i % len(direction)]
      location = graph[location][dir=='R']
      i += 1
  return i
print(solve('AAA'))
print(math.lcm(*map(solve, start)))