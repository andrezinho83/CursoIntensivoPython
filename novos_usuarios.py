current_users = ['admin', 'root', 'Andre', 'fsociety01', 'fsociety02']
new_users = ['elliot', 'fsociety01', 'fsociety02', 'fsociety03', 'Pimentinha']

for new_user in new_users:
	if new_user in current_users:
		print("Ola " +new_user.lower().strip()+ ", forneca um novo nome de usuario pois este ja esta em uso.")
	else:
		print("Usuario " +new_user.lower().strip()+ " disponivel.")




#teste = [print(new_user) for new_user in new_users]
