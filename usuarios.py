usuarios = ['admin', 'andre', 'suporte', 'root', 'pimentinha']
#usuarios =[]

if usuarios:
	for usuario in usuarios:
		print("lista com conteudo")
		if usuario == 'admin':
			print("Ola " +usuario+ ", gostaria de ver um relatorio de status?")
		else:
			print("Ola " +usuario+ ", obrigado por fazer login novamente.")
else:
	print("Precisamos encontrar alguns usuarios.")
