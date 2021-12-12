from collections import defaultdict

def parse_input(file):
  f = open(file, "r")
  text = f.read()
  return [ tuple(line.split('-')) for line in text.split("\n") ]

def build_graph(edges):
  graph = defaultdict(list)
  for edge in edges:
    a, b = edge
    graph[a].append(b)
    graph[b].append(a)
  return graph
  
def distinct_paths(graph, node, visited):
  if node == 'end':
    return 1

  if node.lower() == node and node in visited:
    return 0

  visited.add(node)

  count = 0
  for neighbor in graph[node]:
    count += distinct_paths(graph, neighbor, set(visited))

  return count

edges = parse_input('input_4.txt')
graph = build_graph(edges)
answer = distinct_paths(graph, 'start', set())
print(answer)