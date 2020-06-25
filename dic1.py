favorite_l = {
    'mario': 'python',
    'juan': 'r',
    }

languaje = favorite_l['mario'].title()
print(languaje)
for key, value in favorite_l.items():
    print(f'\nKey: {key}')
    print(f'value: {value}')

for name, languaje in favorite_l.items():
    print(f'{name.title()}´s favorite languaje is {languaje.title()}')
for name in favorite_l.keys():
    print(name.title())
for languaje in favorite_l.values():
    print(languaje.title())
