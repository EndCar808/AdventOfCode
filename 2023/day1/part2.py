import re

# word_digit_pairs = [
#     ('zero', '0'),
#     ('one', '1'),
#     ('two', '2'),
#     ('three', '3'),
#     ('four', '4'),
#     ('five', '5'),
#     ('six', '6'),
#     ('seven', '7'),
#     ('eight', '8'),
#     ('nine', '9')
# ]

# num_tot = 0

# # with open("input.txt") as infile:
# with open("test.txt") as infile:

# 	## Read in lines from input file
# 	for line in infile:
# 		## Split line into text and numbers
# 		ans = list(filter(None, re.split(r'(\d+)', line.split()[0])))

# 		for i, elemnt in enumerate(ans):

# 		print(ans)




		# ## Loop through each character in the line
		# num_tmp = []
		# for c in line.strip():

		# 	## Append to tmp num only the numbers
		# 	if c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
		# 		num_tmp.append(c)
		# 	else: 
		# 		continue

		# ## Update total with calibration values - first and last digits
		# num_tot += int(num_tmp[0] + num_tmp[-1])
		# print(num_tmp[0] + num_tmp[-1])
		

# print(num_tot)
# 
#

def compute_value(line):
    first, last = None, None
    for i, c in enumerate(line):
        if c.isdigit():
            first, last = first or int(c), int(c)
        for d, w in enumerate(("one", "two", "three", "four", "five", "six", "seven", "eight", "nine"), 1):
            if line[i: i + len(w)] == w:
                first, last = first or d, d
    return 10*first + last

with open("input.txt") as infile:
# with open("test.txt") as infile:
	lines = []
	for line in infile:
		lines.append(line.strip())


	print(sum(map(compute_value, lines)))
