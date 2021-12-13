def parse_input(file):
  f = open(file, "r")
  text = f.read()
  section_1, section_2  = text.split("\n\n")
  
  section_1_pairs = [ line.split(",") for line in section_1.split("\n") ]
  points = set([ (int(x), int(y)) for x, y in section_1_pairs ])
  
  section_2_strings = section_2.split("\n")
  folds = []
  for s in section_2_strings:
    words = s.split(" ")
    axis, val = words[-1].split("=")
    folds.append((axis, int(val)))

  return (points, folds)

def fold(points, fold_instruction):
  letter, val = fold_instruction
  if letter == "y":
    return fold_horizontal(points, val)
  else:
    return fold_vertical(points, val)

def fold_horizontal(points, axis):
  new_points = set()
  for point in points:
    x, y = point
    if y > axis:
      diff = y - axis
      new_y = axis - diff
      new_points.add((x, new_y))
    else:
      new_points.add((x, y))
  return new_points

def fold_vertical(points, axis):
  new_points = set()
  for point in points:
    x, y = point
    if x > axis:
      diff = x - axis
      new_x = axis - diff
      new_points.add((new_x, y))
    else:
      new_points.add((x, y))
  return new_points

def print_grid(points):
  max_x = max([ x for x, y in points ])
  max_y = max([ y for x, y in points ])
  grid = [ ["."] * (max_x + 1) for _ in range(max_y + 1) ]
  for x, y in points:
    grid[y][x] = "#"
  print("-------------------------");
  for row in grid:
    print(''.join(row))
  print("-------------------------");

points, folds = parse_input("input_2.txt")
current_points = points
for f in folds:
  current_points = fold(current_points, f)
print_grid(current_points)
