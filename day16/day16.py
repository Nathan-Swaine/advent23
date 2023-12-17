g = {complex(i,j): c for j, r in enumerate(open('data.txt'))
  for i, c in enumerate(r.strip())}
#a+bi = a-bi with complex conjugate
#to update pos use pos += dir
#to update dir use dir = -dir

def fn(todo):
  done = set()
  while todo:
    pos, dir = todo.pop()
    while not (pos, dir) in done:
      done.add((pos, dir))
      pos += dir
      if g.get(pos) == '|': #should use match but not in python 3.9
        dir = 1j
        todo.append((pos, -dir))
      elif g.get(pos) == '-':
        dir = -1
        todo.append((pos, -dir))
      elif g.get(pos) == '/':
        dir = -complex(dir.imag, dir.real)
      elif g.get(pos) == '\\':
        dir = complex(dir.imag, dir.real)
      elif g.get(pos) is None:
        break

  return len(set(pos for pos, _ in done)) - 1

print(fn([(-1, 1)]))

print(max(map(fn, ([(pos-dir, dir)] for dir in (1,1j,-1,-1j)
  for pos in g if pos-dir not in g))))