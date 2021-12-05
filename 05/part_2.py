from collections import Counter

def parse_input(file):
  f = open(file, "r")
  text = f.read()
  lines = [ line.split(' -> ') for line in text.split('\n') ]
  parsed_lines = []
  for line in lines:
    src, dst = line
    x1,y1 = src.split(",")
    x2,y2 = dst.split(",")
    parsed_lines.append(((int(x1), int(y1)), (int(x2), int(y2))))
  return parsed_lines

def is_orthogonal(line):
  src, dst = line
  x1,y1 = src
  x2,y2 = dst
  return x1 == x2 or y1 == y2

def get_orthogonal_points(orthogonal_line):
  if not is_orthogonal(orthogonal_line):
    raise Exception('line must be horizontal or vertical')
  src, dst = orthogonal_line
  x1,y1 = src
  x2,y2 = dst
  if x1 == x2:
    return set( (x1, y) for y in range(min(y1, y2), max(y1, y2) + 1) )
  else:
    return set( (x, y1) for x in range(min(x1, x2), max(x1, x2) + 1) )

def get_diagonal_points(diagonal_line):
  if is_orthogonal(diagonal_line):
    raise Exception('line must be diagonal, not orthogonal')
  src, dst = diagonal_line
  points = set([ src ])
  current = src
  while current != dst:
    x1, y1 = current
    x2, y2 = dst
    if x1 < x2:
      delta_x = 1
    else:
      delta_x = -1
    if y1 < y2:
      delta_y = 1
    else:
      delta_y = -1
    current = (x1 + delta_x, y1 + delta_y)
    points.add(current)
  return points
    

def count_intersect(lines):
  points = Counter()

  for line in lines:
    getter = get_orthogonal_points if is_orthogonal(line) else get_diagonal_points
    for p in getter(line):
      points[p] += 1

  return len([ count for count in points.values() if count > 1])

lines = parse_input("input.txt")
print(count_intersect(lines))
