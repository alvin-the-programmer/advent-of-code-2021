from collections import Counter

def parse_input(file):
  f = open(file, "r")
  text = f.read()
  return sorted([ int(n) for n in text.split(",") ])

def fuel_cost(src, dst):
  delta = abs(src - dst)
  return (delta * (delta + 1)) / 2


positions = parse_input("input.txt")
count = Counter(positions)

best = float('inf')
for target in count:
  total_cost = 0
  for pos in count:
    total_cost += fuel_cost(pos, target) * count[pos]
  best = min(best, total_cost)
  
print(best)

