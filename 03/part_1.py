from collections import Counter

f = open("input", "r")
text = f.read()

grid = [ list(line) for line in text.split("\n") ]
transposed_grid = list(map(list, zip(*grid)))

def calculate_binary(comparator, groups):
  binary_str = ''
  for group in groups:
    count = Counter(group)
    bit = comparator(count.keys(), key=lambda k : count[k])
    binary_str += bit
  return binary_str

gamma = calculate_binary(max, transposed_grid)
epsilon = calculate_binary(min, transposed_grid)
gamma_number = int(gamma, 2)
epsilon_number = int(epsilon, 2)
print(gamma_number * epsilon_number)

