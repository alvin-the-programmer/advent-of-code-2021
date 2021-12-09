def parse_input(file):
  f = open(file, "r")
  text = f.read()
  rows = [ [ int(n) for n in row ] for row in text.split("\n") ]
  return rows

def find_low_positions(grid):
  low_positions = []
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      point = grid[r][c]
      neighbors = []
      for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        d_r, d_c = delta
        n_r = r + d_r
        n_c = c + d_c
        n_r_inbounds = 0 <= n_r < len(grid)
        n_c_inbounds = 0 <= n_c < len(grid[0])
        if n_r_inbounds and n_c_inbounds:
          neighbors.append(grid[n_r][n_c])
      if all(neighbor > point for neighbor in neighbors):
        low_positions.append((r, c))
  return low_positions

def explore_basin(grid, r, c, visited):
  r_inbounds = 0 <= r < len(grid)
  c_inbounds = 0 <= c < len(grid[0])

  if not r_inbounds or not c_inbounds:
    return 0

  if grid[r][c] == 9:
    return 0

  pos = (r, c)
  if pos in visited:

    return 0
  visited.add(pos)

  return 1 + explore_basin(grid, r + 1, c, visited) + explore_basin(grid, r - 1, c, visited) + explore_basin(grid, r, c + 1, visited) + explore_basin(grid, r, c - 1, visited)

def find_basin_sizes(grid, low_positions):
  sizes = []
  for low_pos in low_positions:
    r, c = low_pos
    size = explore_basin(grid, r, c, set())
    sizes.append(size)
  return sizes


grid = parse_input("input.txt")
low_positions = find_low_positions(grid)

sizes = find_basin_sizes(grid, low_positions)
a, b, c = sorted(sizes)[-3:]
print(a * b * c)

