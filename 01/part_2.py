f = open("input", "r")
text = f.read()
nums = [ int(line) for line in text.split("\n") ]

last_sum = sum(nums[0:3])
count = 0
for i in range(1, len(nums) - 2):
  current_sum = sum(nums[i:i + 3])
  if current_sum > last_sum:
    count += 1
  last_sum = current_sum

print(count)