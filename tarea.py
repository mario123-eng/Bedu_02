contacto_0 = {'nombre': 'mario', 'email':'mariomeng@gmail.com', 'telefono': 5540674087}
contacto_1 = {'nombre': 'juan', 'email':'juan@gmail.com', 'telefono': 5540675678}
contacto_2 = {'nombre': 'poncho', 'email':'poncho@gmail.com', 'telefono': 5540678467}
contactos_existentes = [contacto_0, contacto_1, contacto_2]
for contacto_existente in contactos_existentes:
    print(contacto_existente)

agregar_contactos = []
while len(agregar_contactos) < 2:
    nombre = input('Nombre del contacto:')
    email = input('Cual es tu email:')
    telefono = input('Cual es tu telefono:')
    agregar_contacto = {
        'nombre': nombre,
        'email': email,
        'telefono': telefono,
    }
    agregar_contactos.append(agregar_contacto)
    print(f'\nLista de Contactos:')

for contacto_existente in contactos_existentes:
    print(contacto_existente.get('nombre'),  contacto_existente.get('email'), contacto_existente.get('telefono'))
for agregar_contacto in agregar_contactos:
    print(agregar_contacto.get('nombre'),  agregar_contacto.get('email'), agregar_contacto.get('telefono'))

contactos = contactos_existentes + agregar_contactos 
delete = input('Que contacto quieres borrar?')
delete = int(delete)
contactos.pop(delete)
for contacto in contactos:
    print(contacto.get('nombre'), contacto.get('email'), contacto.get('telefono'))

user = input('Que contacto quieres ver?')
user = int(user)
user_selected = contactos[user]
print(user_selected)