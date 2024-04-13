# Faça um programa que calcule e mostre a soma dos 50 primeiros
# números pares
print ("Programa de números pares")
print (80 * "-")
contador = 0
num = 0
contador_par = 0
soma_par = 0
while contador_par < 50:
    num = int(input(f"Digite o {contador + 1}º número par: "))
    if num %2 == 0 :
        #Se for par contabilizar no contador par
        contador_par +=1
        contador +=1
        soma_par = soma_par + num
print (f"A soma dos números pares inseridos foi : {soma_par}")