# Faça um algoritmo que leia 10 números inteiros, armazene-os em uma 
# lista e imprima em ordem crescente
numeros_inteiros = []
contador = 0
for i in range (10) :
    numeros = int(input(f"Digite seu {contador + 1}º número inteiro :"))
    numeros_inteiros.append(numeros)
    contador +=1
# Imprime os números em ordem crescente
print("Números em ordem crescente:",sorted(numeros_inteiros))


