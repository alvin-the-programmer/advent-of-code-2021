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

  max_row = len(grid) - 1
  max_col = len(grid[0]) - 1
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
        distance[neighbor] = min(distance[neighbor], d + grid[nr][nc])
        heapq.heappush(nodes, (distance[neighbor], neighbor))
    visited.add(node)

  return distance[target]

def get_neighbors(grid, r, c):
  deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  neighbors = []
  for dr, dc in deltas:
    nr = r + dr
    nc = c + dc
    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
      neighbors.append((nr, nc))
  return neighbors


grid = parse_input('input_2.txt')
answer = dijkstra(grid, (0, 0))
print(answer)