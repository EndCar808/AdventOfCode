with open("input.txt", 'r') as infile:
	data = infile.read().splitlines()

max_cubes = {
	"red": 12, 
	"blue": 14,
	"green": 13
	}

tot_count = 0

for i in range(len(data)):
	# print(data[i])
	# Extract game ID
	game_id = int(data[i].split(':')[0].split(" ")[-1])

	## Extract game data
	games = data[i].split(":")[1].split(";")

	## Check if valid game
	valid_game = True
	for game in games:

		# Extract sub game data
		game_data = game.split(" ")[1:]
		# print(game_data)
		for i in range(0, len(game_data), 2):
			cube_count = int(game_data[i])
			if cube_count > max_cubes[game_data[i + 1].rstrip(',')]:
				valid_game = False

	if valid_game:
		tot_count += game_id


print(tot_count)
