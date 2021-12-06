def parse_input(file):
  f = open(file, "r")
  text = f.read()
  return [ int(n) for n in text.split(",") ]

def simulate(initial_fish, num_days):
  current_fish = initial_fish[:]
  for day in range(num_days):
    next_fish = []
    for fish in current_fish:
      if fish == 0:
        next_fish.append(6)
        next_fish.append(8)
      else:
        next_fish.append(fish - 1)
    current_fish = next_fish
  return len(current_fish)


fish = parse_input("input.txt")
print(simulate(fish, 80))


