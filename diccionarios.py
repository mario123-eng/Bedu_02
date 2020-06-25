diccionario = {
    'llave': 'valor',
    'llave_2' : 89,
    'llave_flotante': 3.1416,
    'llave_lista': [
        10,
        20,
        50
    ],
    'lista_diccionarios': [
        {
            'nombre':'arbol',
            'ciudad':'cdmx'
        }
    ]
}
print(diccionario)
print(diccionario.get('llave_flotante'))
print(len(diccionario))