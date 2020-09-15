matches_won = dict(Serena=5, Venus=3, Maria=0, Naomi=1)

for player, won_matches in matches_won.items():
	match = 'match' if won_matches == 1 else 'matches'
	print(f'{player} has won {won_matches} {match}')
