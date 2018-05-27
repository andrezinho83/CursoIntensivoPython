###
## Lista de jogadores
###

players = ['Andre', 'Katia', 'Aline', 'Elisa', 'Mel']

print("\nOs tres primeiros da lista:")
print(players[0:3])
print("")

print("Do primeiro e o segundo item da lista:")
print(players[:2])
print("")

print("Do terceiro ao ultimo item da lista:")
print(players[2:])
print("")

print("Os dois ultimos jogadores da lista:")
print(players[-2:])
print("")

print("Lista dos tres primeiros jogadores:")
for player in players[:3]:
	print(player.title())
