#projetinho melhorado pelo chat gpt

print("CALCULO DE IMC")
print("__________________________________________________")
print("Coloque suas credenciais abaixo, para análise:")

nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))

# Verificação básica para garantir que altura e peso são números válidos

altura = float(input('Digite sua altura em metros (por exemplo, 1.75): '))
peso = float(input('Digite o seu peso em kg: '))


mult_altura = altura ** 2
imc = peso / mult_altura
imc_arredondado = round(imc, 1)

print("")
print(f"Olá {nome}, sua classificação do IMC está logo abaixo:")

if imc_arredondado < 18.5:
    classificacao = "MAGREZA"
elif 18.5 <= imc_arredondado <= 24.9:
    classificacao = "NORMAL"
elif 25 <= imc_arredondado <= 29.9:
    classificacao = "SOBREPESO"
elif 30 <= imc_arredondado <= 39.9:
    classificacao = "OBESIDADE"
else:
    classificacao = "OBESIDADE GRAVE"

print(f"O seu IMC é {imc_arredondado}, você está classificado em: {classificacao}")
print("")
