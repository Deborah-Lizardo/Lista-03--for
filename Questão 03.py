# Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a 
# tabuada de 1 a 10 do valor lido.
# for i in range (0,len(Nome)) :
#     print(f"{i+1}. {Nome[i]}")
print ("Demonstratvio de tabuada")
cont = 0 
tabuada = 0
while True :
    num = int(input("Digite um número de 1-10 :"))
    print("Digite 0 para sair")
    print(f"Tabuada de valor {num}")
    if num == 0:
        break
    elif num >= 1 and num <= 10 :
        for i in range (1,11):
            multipli = i  * num 
            print(f"{num} X {i} ={multipli}  ")
    else:
        print("Inválido, por favor digitar novamente.")
        continue