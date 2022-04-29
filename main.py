import random
print("********************************")
print("Bem vindo ao Jogo da Adivinhação")
print("********************************")

num_secreto = random.randrange(1,101)
tentativas = 3

print(num_secreto)

while(tentativas > 0):
    print("*** Tentativas restantes: ", tentativas)
    entrada = input("Digite o seu número: ")
    entradaCerto = int(entrada)
    print("Você digitou: ", entrada)

    if(entradaCerto < 1 or entradaCerto > 100):
        print("Você deve digitar um número entre 1 e 100!!")
        continue

    if(num_secreto == entradaCerto):
        print("***** VOCÊ ACERTOU!!")
        break

    else:
        if(entradaCerto > num_secreto):
            print("VOCÊ ERROU! SEU NÚMERO É MAIOR DO QUE O NÚMERO SECRETO!")
        elif(entradaCerto < num_secreto):
            print("VOCÊ ERROU! SEU NÚMERO É MENOR DO QUE O NÚMERO SECRETO!")

    tentativas = tentativas - 1
