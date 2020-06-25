
def saludar(nombre):
    if len(nombre) < 5:
        print(f'Hola buenos dias {nombre}')
    else:
        print(f'Que onda {nombre}')

personas = ['Juanito', 'Jose', 'Pedro']
for p in personas:
    saludar (p)