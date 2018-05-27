lugares = ['hawaii', 'indonesia', 'australia', 'amsterdan', 'canada']

print("Lista na forma original: ")
print(lugares)
print("")

print("Utilizando 'sorted()' para exibir em ordem alfabetica sem modificar a lista propriamente dita")
print(sorted(lugares))
print("")

print("Mostrando lista original novamente: ")
print(lugares)
print("")

print("Usando 'sorted()' para exibir a lista em ordem alfabetica inversa: ")
ordem_alfabetica = sorted(lugares)
ordem_alfabetica.reverse()
print(ordem_alfabetica)
print("")

print("Mostrando lista original novamente: ")
print(lugares)
