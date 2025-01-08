''' LISTAS '''

miLista = [2, 8, 10]

print(len(miLista))

''' Metodos '''
print(miLista)
miLista.append(101)
print(miLista)

otraLista = ['Python', 'Javascript', 'Java']
otraLista.insert(1, 'C++')

print(otraLista)
frameworks = ['Flask', 'Express', 'Spring']
elementoSacado = frameworks.pop()
print(frameworks)
print(elementoSacado)


''' Desempaquetamiento de una lista  '''

lenguajes = ['Rust', 'Cobol', 'Basic']

primerLen, segundoLen, tercerLen = lenguajes

print(primerLen)
print(segundoLen)
print(tercerLen)
print(lenguajes)


''' Listas por comprension '''
''' sintaxis
[nueva_lista for i in iterable]
[x for x in iterable]
'''

print([item for item in range(6)])

print([item * 5 for item in range(6)])

resultado = [item * 5 for item in range(6) if item % 2 == 0]
print(resultado)

saludo = 'hola Mundo'
vocales = [letra for letra in saludo if letra in 'aeiou']
print(vocales)
