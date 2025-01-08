''' TRUTHY Y FALSY '''

# print(bool(True))
# print(bool(3 < 1))

# Falsy
print(bool(None))
print(bool(False))
print(bool(1))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))

print('Es truthy' if [] else 'Es Falsy')

numeros = []
if numeros:
    for i in numeros:
        print(i * 10)
else:
    print('la lista esta vacia, no puedo realiza ninguna operacion')
