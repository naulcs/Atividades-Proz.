# Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

# Escreva um código que imprima todos os números exceto o número 13.
# Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

# Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

i = 20
while i > 0:
    if i != 13:
        print(i)
    i -= 1

# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return 0
    
#     Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

while True:
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

    opcao = int(input("Digite o número para a operação correspondente: "))

    if opcao == 0:
        break
    elif opcao < 0 or opcao > 4:
        print("Essa opção não existe")
        continue

    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))

    if opcao == 1:
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    elif opcao == 2:
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
    elif opcao == 3:
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    elif opcao == 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
        else:
            print("Erro! Divisão por zero não é permitida.")

# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

while True:
    nome_completo = input("Digite seu nome completo: ")

    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                break
            else:
                print("Erro! Ano inválido. Por favor, digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Erro! Isso não é um número. Por favor, digite um ano válido.")

    idade = 2022 - ano_nascimento

    print(f"Nome: {nome_completo}")
    print(f"Idade em 2022: {idade} anos")


#Declare dois arrays, cada um com um mínimo de cinco elementos, e imprima eles no terminal usando o comando print(). O primeiro array deve conter os produtos de uma loja da sua escolha (loja de comida, materiais de construção, música, etc). O segundo array deve conter os anos de nascimento de familiares e amigos seus. Lembre-se de usar nomes descritivos para nomear cada variável, e de usar o tipo de dado apropriado para cada lista (strings, booleanos, números inteiros, floats).

produtos_loja_musica = ["Guitarra", "Baixo", "Bateria", "Teclado", "Microfone"]

print("Produtos da loja de música: ", produtos_loja_musica)

anos_nascimento = [1980, 1992, 2001, 1965, 1978]

print("Anos de nascimento: ", anos_nascimento)
