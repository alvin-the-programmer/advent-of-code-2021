def parse_input(file):
  f = open(file, "r")
  text = f.read()
  return sorted([ int(n) for n in text.split(",") ])

positions = parse_input("input.txt")
med = positions[len(positions) // 2]

total_fuel = 0
for pos in positions:
  total_fuel += abs(pos - med)
print(total_fuel)