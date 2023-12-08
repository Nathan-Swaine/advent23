from math import sqrt, ceil, prod
input = [line.strip().split(":")[1] for line in open("data.txt", "r")]

def getTime(data):
  time, dist = data
  t = ceil((time - sqrt(time**2 - 4 * dist)) / 2) #quadratic formula
  return time + 1 - 2 * t

data = zip(*[[int(i) for i in line.split()] for line in input])
data2 = [int(line.replace(" ", "")) for line in input]
rez = [getTime(d) for d in data]

part1 = prod(rez)
part2 = getTime(data2)
