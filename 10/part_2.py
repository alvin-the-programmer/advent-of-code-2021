import statistics

def parse_input(file):
  f = open(file, "r")
  text = f.read()
  return [ line for line in text.split("\n") ]

def missing_chars(line):
  pair = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
  }
  stack = []
  for ch in line:
    if ch in pair:
      stack.append(pair[ch])
    else:
      if stack[-1] == ch:
        stack.pop()
      else:
        return None
  return stack

def calculate_score(sequence):
  points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
  }
  total_score = 0
  for ch in sequence:
    total_score  = (total_score * 5) + points[ch]
  return total_score

lines = parse_input('input.txt')
sequences = [ missing_chars(line)[::-1] for line in lines if missing_chars(line) is not None ]
scores = [ calculate_score(seq) for seq in sequences ]
print(statistics.median(scores))