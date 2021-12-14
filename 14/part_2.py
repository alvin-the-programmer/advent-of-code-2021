from collections import Counter

def parse_input(file):
  f = open(file, "r")
  text = f.read()
  section_a, section_b = text.split("\n\n")
  template = section_a
  
  replace = {}
  for line in section_b.split("\n"):
    target, insert = line.split(" -> ")
    replace[target] = insert
  
  return template, replace

# O(n) time, n = number steps
#   "large" hidden constant factor of 26*26 because of the total 
#   unique pair of letters
def build(template, replace, steps):
  char_count = Counter(list(template))
  pair_count = Counter()
  for i in range(len(template) - 1):
    pair_count[template[i:i+2]] += 1

  for step in range(steps):
    new_pair_count = Counter(pair_count)
    for pair in pair_count:
      a = pair[0]
      b = pair[1]
      if pair in replace:
        num = pair_count[pair]
        add = replace[pair]
        char_count[add] += num
        new_pair_count[pair] -= num
        new_pair_count[a + add] += num
        new_pair_count[add + b] += num

    non_zero_count = Counter()
    for k in new_pair_count:
      v = new_pair_count[k]
      if v > 0:
        non_zero_count[k] = v
    pair_count = non_zero_count
  return char_count

template, replace = parse_input("input_2.txt")
count = build(template, replace, 40)
diff = max(count.values()) - min(count.values())
print(diff)

