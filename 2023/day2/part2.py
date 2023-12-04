with open("input.txt", 'r') as infile:
# with open("test.txt", 'r') as infile:
	data = infile.read().splitlines()

max_cubes = {
	"red": 12, 
	"blue": 14,
	"green": 13
	}

tot_count = 0
power = 0

for i in range(len(data)):
	# print(data[i])
	# Extract game ID
	game_id = int(data[i].split(':')[0].split(" ")[-1])

	## Extract game data
	games = data[i].split(":")[1].split(";")

	tmp = {
		"red": 0, 
		"blue": 0,
		"green": 0
		}

	for game in games:

		# Extract sub game data
		game_data = game.split(" ")[1:]

		for i in range(0, len(game_data), 2):
			cube_color = game_data[i + 1].rstrip(',')
			cube_count = int(game_data[i])

			if cube_count > tmp[cube_color]:
				tmp[cube_color] = cube_count

	## Compute power
	tmp_prod = 1
	for val in list(tmp.values()):
		tmp_prod *= val
	power += tmp_prod

	# print(games, tmp, list(tmp.values()), tmp_prod)
print(tot_count, power)
