lista = ['Luigi', 'Mario', 'Anna', 'Maria', 'Cristina']

# Stampo la lista
print(lista)

# Stampo un elemento specifico (ad esempio, il secondo elemento)
print(lista[1])

# Stampo ad uno a uno tutti gli elementi della lista
print() # stampo una riga vuota per separare
print('Stampo tutti gli elementi della lista uno a uno:')
indice = 0 # inizializzo l'indice al valore 0 (la prima posizione della lista)
print(f'Elemento in posizione {indice}: {lista[indice]}')

indice = indice + 1 # incremento l'indice di 1
print(f'Elemento in posizione {indice}: {lista[indice]}')

indice += 1 # incremento l'indice di 1 (come fatto prima, ma con una sintassi diversa e più compatta)
print(f'Elemento in posizione {indice}: {lista[indice]}')

indice += 1
print(f'Elemento in posizione {indice}: {lista[indice]}')
indice += 1
print(f'Elemento in posizione {indice}: {lista[indice]}')

# Fine: ho stampato tutti gli elementi della lista!
