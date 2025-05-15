to_do =["Dirigirnos al Hotel", "Ir a almorzar", "Visitar museo","Volver al Hotel"]
print(to_do)
numbers =[1,2,3,4,5,6,7,8,9,0]
print(numbers)
print(type(to_do))
print(type(numbers))

mix=["uno",2,"tres",4, "cinco",True,1,2,34,5]
print(mix)

print(len(mix))
print(f'Primer elemento: {mix[0]}')
print(f'Segundo elemento: ',(mix[1]))
print(f'Tercer elemento: ',(mix[2]))
print(f'Cuarto elemento: {mix[3]}')
print(f'Ultimo elemento {mix[-1]}')


Cadena= "Daniel Rodriguez"

print(len(Cadena))
print(f'Primer elemento: {Cadena[0]}')
print(f'Segundo elemento: ',(Cadena[1]))
print(f'Tercer elemento: ',(Cadena[2]))
print(f'Cuarto elemento: {Cadena[3]}')
print(f'Ultimo elemento {Cadena[-1]}')

print(f'elementos de la lista desde la posición cero a la  5:\n {Cadena[0:]}')
print(mix)
mix.append(False)
print(mix)
mix.append([1,2,3,4,5,6,7,8,9,10])
print(mix)
mix.insert(0,"Daniel Tester")
print(mix)

print(mix.index("Daniel Tester"))
print(numbers)
print(f'Elemento Mayor:  {max(numbers)}')
print(f'Elemento :  {min(numbers)}')

#eliminar elementos de la lista 
del numbers[-1]
print(numbers)


