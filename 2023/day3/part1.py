with open("input.txt") as infile:
	data = infile.read().splitlines()


for line in data:
	print(line.strip('.'))