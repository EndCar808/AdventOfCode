with open("input.txt") as infile:
# with open("test.txt") as infile:
	data = infile.read().splitlines()

tot_num_cards = [1] * len(data)

points = 0

for i, line in enumerate(data):
	## Split into left and right of |
	tmp = line.split('|')

	## Extract list of winning numbers - There will be empty strings in list while splitting
	## So make sure to filter these out
	win_nums = list(filter(None, tmp[0].split(':')[1].split(' ')))

	## Extract same for drawn numbers
	drawn_nums = list(filter(None, tmp[1].split(' ')))
	# print(tmp, win_nums, drawn_nums)

	num_match = 0
	for dn in drawn_nums:
		if dn in win_nums:
			num_match += 1
	
	for n in range(num_match):
		tot_num_cards[i + 1 + n] += tot_num_cards[i] * 1
	
	# print(i + 1, num_match, tot_num_cards)
# 
# for i, t in enumerate(tot_num_cards):
# 	print(i + 1, t)

print(sum(tot_num_cards))