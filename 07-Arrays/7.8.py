computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# sort alphabetically
computer_games.sort()

i = 0
counter = 1
while i < len(computer_games):
    print(counter, computer_games[i])
    counter += 1
    i += 1
