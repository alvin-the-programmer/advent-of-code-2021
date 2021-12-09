def parse_input(file):
  f = open(file, "r")
  text = f.read()
  rows = [ [ int(n) for n in row ] for row in text.split("\n") ]
  return rows

def find_low_points(grid):
  low_points = []
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
        low_points.append(point)
  return low_points

grid = parse_input("input.txt")
low_points = find_low_points(grid)
print(sum([ p + 1 for p in low_points ]))