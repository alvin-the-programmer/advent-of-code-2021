f = open("input", "r")
text = f.read()

pairs = [ line.split(" ") for line in text.split("\n") ]
commands = [ (pair[0], int(pair[1])) for pair in pairs ]

x = 0
y = 0

for command in commands:
  direction, value = command
  if direction == 'forward':
    x += value
  elif direction == 'up':
    y -= value
  else:
    y += value

print(x * y)