# para definir un lista se usa []
familiares = ['Mario', 'Ursula']
print(type(familiares))

contador = 0
for familiar in familiares:
    contador = contador + 1
print (f'Familiar = {familiar} --- Contador {contador}')

print(f'Total de familiares {contador}')
print('Total elementos en lista Familaires')
print(len(familiares))
# len es para contar tu lista