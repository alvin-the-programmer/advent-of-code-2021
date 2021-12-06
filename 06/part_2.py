from collections import Counter

def parse_input(file):
  f = open(file, "r")
  text = f.read()
  return sorted([ int(n) for n in text.split(",") ])

def simulate(initial_fish, num_days):
  current_count = Counter(initial_fish)
  for day in range(num_days):
    next_count = Counter()
    for i in range(9):
      if i == 0:
        next_count[6] += current_count[i]
        next_count[8] += current_count[i]
      else:
        next_count[i - 1] += current_count[i]
    current_count = next_count
  return sum(current_count.values())

fish = parse_input("input.txt")
print(simulate(fish, 256))




