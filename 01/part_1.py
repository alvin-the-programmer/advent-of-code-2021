f = open("input", "r")
text = f.read()
nums = [ int(line) for line in text.split("\n") ]

last = nums[0]
count = 0
for num in nums:
  if num > last:
    count += 1
  last = num

print(count)
