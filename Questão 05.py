#  Ler 10 números e imprimir quantos são pares e quantos são ímpares. 
contador = 0
total_num = 0
contador_par = 0
contador_impar = 0
while contador < 10:
    num = int(input(f"Digite o {contador + 1}º número: "))
    if num %2 == 0 :
        #Se for par contabilizar no contador par
        contador_par +=1
        contador += 1
    elif num %2 != 0 :
        #Se for ímpar, contabilizar no contador de ímpares 
        contador_impar +=1
        contador +=1
        if num < 0 :
            print("Digite um número válido.")
        continue

print(f"A quantidade de pares inseridos foi : {contador_par}")
print(80 * "-")
print(f"A quantidade de ímpares inseridos foi : {contador_impar}")

