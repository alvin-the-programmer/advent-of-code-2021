def parse_input(file):
  f = open(file, "r")
  text = f.read()
  return [ line for line in text.split("\n") ]

def first_illegal_char(line):
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
      if len(stack) == 0:
        return None
      if stack[-1] == ch:
        stack.pop()
      else:
        return ch


points = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

lines = parse_input('input.txt')
illegal_chars = [ first_illegal_char(line) for line in lines ]
answer = sum([ points[char] for char in illegal_chars if char is not None ])
print(answer)
