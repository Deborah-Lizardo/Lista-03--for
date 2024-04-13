# Utilizando a estrutura de repetição for, faça um programa que receba 10
# números e conte quantos deles estão no intervalo [10,20] e quantos
# deles estão fora do intervalo
contador_num_fora = 0
contador_num_dentro = 0
contador = 0
print("Programa contador de números")
print (80 * "-")
print("Digite 10 números :")
for i in range (10) : #Solicitando 10 números
        num = float(input(f"Digite o {i + 1}º número: ")) 
for i2 in range (10,21) :#Está dentro do intervalo?
        if num == i2:
            contador_num_dentro +=1
            contador +=1
        else:   
            contador_num_fora +=1
            contador +=1
print(f"A quantidade inserida de números foram : {contador}")
print (f"A quantidade de números dentro do intervalo foi : {contador_num_dentro}")
print (f"A quantidade de números fora do intervalo foi : {contador_num_fora}")
