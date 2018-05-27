###
## Criar uma lista dos dez primeiros cubos (isto e, o cubo de cada inteiro de 1 a 10)
## e utilize um laco for para exibir o valor de cada cubo.
###

#lista = []
#for numero in range(1,11):
#	print(numero**3)

### Melhor forma
lista = []
var1 = [lista.append(numero**3) for numero in range(1,11)]
print(lista)
