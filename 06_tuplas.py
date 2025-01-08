''' TUPLAS '''

tupla = ('a', 'z', 'p')

print(tupla[1])

''' tupla de un solo elemento '''
tupla2 = (10,)
# print(tupla2)
print(type(tupla2))

''' tupla implicita '''
tuplaImplicita = 'a', 'z', 'p'
print(type(tuplaImplicita))

''' Desempaquetamiento '''
v1, v2, v3 = tuplaImplicita
print(v1)
print(v2)
print(v3)

''' inmutabilidad '''

calificaciones = (4.2, 3.5, 1.0)
# calificaciones[2] = 3.0


numbers = (110, [5, 6], 200)

numbers[1][1] = 10

print(numbers)
