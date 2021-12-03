from collections import Counter

TIE = 'tie'

f = open("input", "r")
# f = open("small_input", "r")

text = f.read()

lines = text.split("\n")
grid = [ list(line) for line in lines ]
transposed_grid = list(map(list, zip(*grid)))

def get_bit_criteria(comparator, group):
  count = Counter(group)
  if len(set(count.values())) == 1:
    return TIE
  return comparator(count.keys(), key=lambda k : count[k])

def transpose(strs):
  grid = [ list(str) for str in strs ]
  return list(map(list, zip(*grid)))

def calculate(comparator, candidates):
  current_candidates = candidates
  idx = 0
  while len(current_candidates) > 1:
    transposed = transpose(current_candidates)
    bit_criteria = get_bit_criteria(comparator, transposed[idx])
    if bit_criteria == TIE:
      if comparator == max:
        bit_criteria = '1'
      else:
        bit_criteria = '0'
    current_candidates = [ candidate for candidate in current_candidates if candidate[idx] == bit_criteria ]
    idx += 1
  return current_candidates[0]

oxygen = calculate(max, lines)
carbon = calculate(min, lines)
print(oxygen)
print(carbon)
oxygen_number = int(oxygen, 2)
carbon_number = int(carbon, 2)
print(oxygen_number)
print(carbon_number)
print(oxygen_number * carbon_number)

