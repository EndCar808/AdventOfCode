with open("input.txt") as infile:
# with open("test.txt") as infile:
	data = infile.read().splitlines()

points = 0

for line in data:
	## Split into left and right of |
	tmp = line.split('|')

	## Extract list of winning numbers - There will be empty strings in list while splitting
	## So make sure to filter these out
	win_nums = list(filter(None, tmp[0].split(':')[1].split(' ')))

	## Extract same for drawn numbers
	drawn_nums = list(filter(None, tmp[1].split(' ')))
	# print(tmp, win_nums, drawn_nums)

	num_match = 0
	match = False
	for dn in drawn_nums:
		if dn in win_nums:
			num_match += 1
			# print("Yes", dn, num_match)
			match = True

	if match:
		points += 2 ** (num_match - 1) 
	# print(points)
	

print(points)