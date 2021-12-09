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


def total_keys(entries):
  count = 0
  key_segment_lengths = set([2, 4, 3, 7]) # 1, 4, 7, 8
  for entry in entries:
    outputs, signals = entry
    for signal in signals:
      if len(signal) in key_segment_lengths:
        count += 1
  return count

entries = parse_input('input.txt')
print(total_keys(entries))