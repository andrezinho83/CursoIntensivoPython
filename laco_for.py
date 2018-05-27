# Exercicio: pag. 102

#lista = []
#for numero in range(1,1000001):
#	lista.append(numero)
#print(lista)

### Melhor forma.
lista = []
var1 = [lista.append(numero) for numero in range(1,1000001)]
#print(lista)
print("\nValor minimo da lista:")
print(min(lista))
print("\nValor maximo da lista:")
print(max(lista))
print("\nSoma da lista:")
print(sum(lista))
print("")
