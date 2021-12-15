import heapq
from collections import defaultdict

def parse_input(file):
  f = open(file, "r")
  text = f.read()
  lines = text.split("\n")
  rows = []
  for line in lines:
    rows.append([ int(ch) for ch in line ])
  return rows


def dijkstra(grid, source):
  distance = defaultdict(lambda: float('inf'))
  distance[source] = 0
  nodes = [ (0, source) ]

  max_row = len(grid) * 5 - 1
  max_col = len(grid[0]) * 5 - 1
  target = (max_row, max_col)

  visited = set()
  while target not in visited:
    d, node = heapq.heappop(nodes)
    if node in visited:
      continue
    r, c = node
    for neighbor in get_neighbors(grid, r, c):
      if neighbor not in visited:
        nr, nc = neighbor
        distance[neighbor] = min(distance[neighbor], d + get_risk(grid, nr, nc))
        heapq.heappush(nodes, (distance[neighbor], neighbor))
    visited.add(node)

  return distance[target]

def get_neighbors(grid, r, c):
  num_rows = len(grid) * 5
  num_cols= len(grid[0]) * 5
  deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  neighbors = []
  for dr, dc in deltas:
    nr = r + dr
    nc = c + dc
    if 0 <= nr < num_rows and 0 <= nc < num_cols:
      neighbors.append((nr, nc))
  return neighbors

def get_risk(grid, r, c):
  base_r = r % len(grid)
  base_c = c % len(grid[0])
  row_area = r // len(grid)
  col_area = c // len(grid[0])
  increase = row_area + col_area
  total = grid[base_r][base_c] + increase
  if total > 9:
    return total - 9
  else:
    return total

grid = parse_input('input_2.txt')
answer = dijkstra(grid, (0, 0))
print(answer)