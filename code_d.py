# Faça um Programa que mostre a mensagem "Alo mundo" na tela.

# print("Hello World!")

# frase = "Hello World!"
# print(frase)

# frase = input("Por favor, digite uma frase: ")
# print(type(frase))
# print(frase)

# ---------------------------------------------------------------

# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

# num = int(input("Por favor, digite um número: "))
# print(f"O número informado foi {num}")

# -------------------------------------------------------
# Faça um Programa que peça dois números e imprima a soma.

# num1 = int(input('Por favor, digite um número: '))
# num2 = int(input('Por favor, digite outro número: '))
# soma = num1 + num2
# print(soma)

# --------------------------------------------------------

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# nota1 = float(input('Insira a 1ª nota: '))
# nota2 = float(input('Insira a 2ª nota: '))
# nota3 = float(input('Insira a 3ª nota: '))
# nota4 = float(input('Insira a 4ª nota: '))

# media = (nota1 + nota2 + nota3 + nota4) / 4

# print(f'Sua média foi de {media}')
#print('Sua media foi de ' , media)

# --------------------------------------------------------

# Faça um Programa que peça dois números e imprima o maior deles.

# num1 = int(input('Insira um numero: '))
# num2 = int(input('Insira outro numero: '))

# if(num1 > num2):
#     print(f'O nº {num1} é maior!')
# elif(num2 > num1):
#     print(f'O nº {num2} é maior!')
# else:
#     print('São iguais!')

# --------------------------------------------------------

# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# valor = int(input('Insira um número: '))

# if(valor > 0):
#     print(f'O valor {valor} é positivo')
# elif(valor < 0):
#     print(f'O valor {valor} é negativo')
# else:
#     print(f'O valor {valor} é neutro')


# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# vogal = input("Por favor, digite uma letra: ")

# if vogal == "a" or vogal == "e" or vogal == "i" or vogal == "o" or vogal == "u":
#     print("É uma vogal!")
# else:
#     print("É uma consoante!")

# # outra forma:

# if vogal in "aeiou":
#     print("É uma vogal!")
# else:
#     print("É uma consoante!")

# letra = input("Por favor, digite uma letra: ").upper()
# v = ["a", "e", "i", "o", "u"]

# if letra in v:
#   print(f'{letra} é vogal!')
# else:
#   print(f'{letra} é consoante!')


# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue 
# pedindo até que o usuário informe um valor válido.

contador=1

while contador <= 10:
    nota = float(input(f'Digite a nota {contador}: '))
    if nota <0 or nota >10:
        print('Digite um valor válido')
        continue
    contador +=1
 
    

