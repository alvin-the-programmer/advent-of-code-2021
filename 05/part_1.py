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

def filter_orthogonal(lines):
  return [ line for line in lines if is_orthogonal(line) ]

def is_orthogonal(line):
  src, dst = line
  x1,y1 = src
  x2,y2 = dst
  return x1 == x2 or y1 == y2

def get_points(orthgonal_line):
  if not is_orthogonal(orthgonal_line):
    raise Exception('line must be horizontal or vertical')
  src, dst = orthgonal_line
  x1,y1 = src
  x2,y2 = dst
  if x1 == x2:
    return [ (x1, y) for y in range(min(y1, y2), max(y1, y2) + 1) ]
  else:
    return [ (x, y1) for x in range(min(x1, x2), max(x1, x2) + 1) ]

def count_intersect(orthogonal_lines):
  points = Counter()

  for line in orthogonal_lines:
    for p in get_points(line):
      points[p] += 1

  return len([ count for count in points.values() if count > 1])

lines = parse_input("input.txt")
orthogonal_lines = filter_orthogonal(lines)

print(count_intersect(orthogonal_lines))

