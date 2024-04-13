#  Dada a lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6] imprima o número que se repete 
# mais vezes.
#identificar lista-vetor
print("Resposta questão 10")
print (80* "-")
lista =  [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
num_repetido = 0
frequency= 0 
for num in lista:
    if lista.count(num) > frequency: #Count vai contar quantas vezes o número vai repetir
        frequency = lista.count(num) #Frequencia do numero repetido = count dele
        num_repetido = num #número que mais repete vai treceber num
print(f" De acordo a lista [2, 4, 7, 2, 3, 3, 1, 0, 2, 6], o número que mais se repete é o número  {num_repetido}, repetindo {frequency} vezes.")