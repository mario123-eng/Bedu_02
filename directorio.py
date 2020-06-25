contactos = []
while len(contactos) < 2:
    nombre = input('Nombre del Contacto:')
    telefono = input('Telefono del contacto:')
    email = input('email del contacto:')
    contacto = {
        'nombre': nombre, 
        'telefono': telefono,
        'email': email,
    }
    contactos.append(contacto)
    print(f'Nuestro directorio tiene {len(contactos)} elementos')
print('-------------')
print(f'Directorio contiene {len(contactos)}')

for contacto in contactos:
    print(contacto.get('nombre'), contacto.get('telefono'), contacto.get('email'))
    
# -------------
# nombre, telefono, correo
