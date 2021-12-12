from collections import defaultdict

def parse_input(file):
  f = open(file, "r")
  text = f.read()
  return [ tuple(line.split('-')) for line in text.split("\n") ]

def build_graph(edges):
  graph = defaultdict(list)
  for edge in edges:
    a, b = edge
    if b != 'start':
      graph[a].append(b)
    if a != 'start':
      graph[b].append(a)
  return graph
  
def distinct_paths(graph, node, visited, freebie_used):
  if node == 'end':
    return 1

  next_freebie_used = freebie_used
  if node.lower() == node and node in visited:
    if freebie_used:
      return 0
    else:
      next_freebie_used = True

  visited.add(node)
  count = 0
  for neighbor in graph[node]:
    count += distinct_paths(graph, neighbor, set(visited), next_freebie_used)

  return count

edges = parse_input('input_4.txt')
graph = build_graph(edges)
answer = distinct_paths(graph, 'start', set(), False)
print(answer)