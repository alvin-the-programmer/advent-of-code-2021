from collections import Counter

def parse_input(file):
  f = open(file, "r")
  text = f.read()
  section_a, section_b = text.split("\n\n")
  template = list(section_a)
  
  replace = {}
  for line in section_b.split("\n"):
    target, insert = line.split(" -> ")
    replace[target] = insert
  
  return template, replace

def build(template, replace, steps):
  current_template = template
  for step in range(steps):
    new_template = []
    for i in range(len(current_template) - 1):
      double = "".join(current_template[i:i + 2])
      if double in replace:
        if new_template:
          new_template.pop();
        new_template.append(double[0])
        new_template.append(replace[double])
        new_template.append(double[1])
    current_template = new_template
  return current_template
  

template, replace = parse_input("input_2.txt")
polymer = build(template, replace, 10)
count = Counter(polymer)
diff = max(count.values()) - min(count.values())
print(diff)

