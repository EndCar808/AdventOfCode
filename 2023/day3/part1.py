# with open("input.txt") as infile:
with open("test.txt") as infile:
	data = infile.read().splitlines()


for line in data:
	# print(line)
	# print(line.strip('.'))
	# count=0

	test = [(i, c) for i, c in enumerate(line) if c.isdigit()]
	print(test)

	# print(count)