data = []
num_tot = 0
with open("input.txt") as infile:
# with open("test.txt") as infile:
	## Read in lines from input file
	for line in infile:

		## Loop through each character in the line
		num_tmp = []
		for c in line.strip():

			## Append to tmp num only the numbers
			if c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
				num_tmp.append(c)
			else: 
				continue

		## Update total with calibration values - first and last digits
		num_tot += int(num_tmp[0] + num_tmp[-1])
		print(num_tmp[0] + num_tmp[-1])
		

print(num_tot)