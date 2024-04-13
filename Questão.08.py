# Faça um algoritmo que leia um número positivo e imprima seus 
# divisores. 
numero = 0
contador = 0
print("Programa de divisores")
print(80* "-")
while True:
    numero= int(input(f"Digite um número inteiro positivo: "))
    if numero <= 0:
        print("O número inserido não é válido.")
        continue
    else:
        print(f"Os divisores de {numero} são:")
        divisor = 1
        while divisor <= numero: #Divisor menor ou igual ao numero
            if numero % divisor == 0:#Resto da divisão zero
                print(divisor)
            divisor +=1
        break