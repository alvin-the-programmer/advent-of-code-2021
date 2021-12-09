from collections import defaultdict, Counter

def parse_input(file):
  f = open(file, "r")
  text = f.read()
  lines = [ entry.split(" | ") for entry in text.split("\n") ]
  
  entries = []
  for line in lines:
    signal_str, output_str = line
    signals = signal_str.split(' ')
    outputs = output_str.split(' ')
    entries.append((signals,  outputs))
  return entries

def decode_key(entry):
    signals, outputs = entry
    s = defaultdict(list)
    for signal in signals:
      s[len(signal)].append(signal)

    # step A
    solve_0 = list(set(s[3][0]) - set(s[2][0]))[0]

    # step B
    narrow_46 = list(set(s[3][0]) & set(s[2][0]))

    # step C
    narrow_13 = list(set(s[4][0]) - set(s[2][0]))

    # step D
    narrow_35 = [ char for char in Counter(''.join(s[5])) if Counter(''.join(s[5]))[char] == 1 ]

    # step E
    solve_3 = list(set(narrow_13) & set(narrow_35))[0]
    solve_1 = list(set(narrow_13) - set([solve_3]))[0]
    solve_5 = list(set(narrow_35) - set([solve_3]))[0]

    # step F
    current_solns = [ solve_0, solve_3, solve_1, solve_5 ]
    size_3 = [ signal for signal in trim_matches(s[5], current_solns) if len(signal) == 3 ]
    solve_2 = list(set(size_3[0]) - set(s[2][0]))[0]

    # step G
    current_solns = [ solve_0, solve_3, solve_1, solve_5, solve_2 ]
    solve_6 = [ signal for signal in trim_matches(s[6], current_solns) if len(signal) == 1 ][0]

    # step H
    solve_4 = list(set(s[2][0]) - set([solve_6]))[0]

    key = {}
    key[solve_0] = "0"
    key[solve_1] = "1"
    key[solve_2] = "2"
    key[solve_3] = "3"
    key[solve_4] = "4"
    key[solve_5] = "5"
    key[solve_6] = "6"
    return key

def trim_matches(signals, matches):
  new_signals = []
  for signal in signals:
    new_signals.append(''.join(list(set(signal) - set(''.join(matches)))))
  return new_signals

def translate(output, key):
  digit = {
    "023456": "0",
    "46": "1",
    "01245": "2",
    "01246": "3", 
    "1346": "4",
    "01236": "5",
    "012356": "6",
    "046": "7",
    "0123456": "8",
    "012346": "9"
  }

  translation = []
  for char in output:
    translation.append(key[char])
  sorted_translation = ''.join(sorted(translation))
  return digit[sorted_translation]

entries = parse_input('input.txt')
total = 0
for entry in entries:
  signals, outputs =  entry
  key = decode_key(entry)
  num = int(''.join([ translate(o, key) for o in outputs ]))
  total += num

print(total)

# step A solve 0: diff s2,s3
# step B narrow 4,6candidates: overlap s2,23
# step C narrow 1,3candidates: diff s4,s2
# step D narrow 3,5candidates: choose s5 unique
# step E solve 3,1,5: overlap 3,5candidates with 1,3candidates
# step F solve 2: remove solved from s5, take size 3 signal and diff with s2
# step G solve 6: remove solved from s6, size 1 signal is 6
# step H solve 4: diff s2, solve6
#
# sizes:
# s2 -> [d1-46]
# s3 -> [d7-046]
# s4 -> [d4-1346]
# s5 -> [d2-01245, d3-01246, d5-01236]
# s6 -> [d0-023456, d6-012356, d9-012346]
# s7 -> [d8-0123456]
#
# s5 -> [d2-4, d3-46, d5-6]
# s6 -> [d0-46, d6-6, d9-46]
#
# unique sizes: 1, 4, 7, 8
#
#
#      0
#  3       4
#      1
#  5       6
#      2
