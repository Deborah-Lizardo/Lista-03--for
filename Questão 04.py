#  Leia várias idades e calcule a média entre as idades (usar uma variável 
# para idade).
contador = 0
total_idades = 0 
while True :
    idade = int(input("Digite uma idade ou 0 para calcular a média :"))
    if idade == 0 :
        break
    elif idade < 0:
        print("Idade negativa inserida. Reiniciando o programa...")
        print(80 * "-")
        continue
    total_idades = idade + total_idades
    contador +=1
    media = total_idades/contador
print(f"A média das idades inseridas é: {media:.2f}")