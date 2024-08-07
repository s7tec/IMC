#projetino de calculo de imc 
print("CALCULO DE IMC")
print("__________________________________________________")
print("Coloque suas credenciais abaixo, para analise:")

nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura em metros (por exemplo, 1.75): '))
peso = float(input('Digite o seu peso em kg: '))

mult_altura = altura  ** 2
imc = peso / mult_altura
imc_aredondado = round(imc, 1)
print("")
print("Olá" ,nome, "sua classificação do imc está logo abaixo:")

if imc_aredondado < 18.5:
    print("O seu imc é", imc_aredondado, "você está classsificado em: MAGREZA")
elif imc_aredondado >= 18.5 and imc_aredondado <= 24.9:
    print("O seu imc é", imc_aredondado, "você está classsificado em: NORMAL")
elif imc_aredondado >= 25 and imc_aredondado <= 29.9:
    print("O seu imc é", imc_aredondado, "você está classsificado em: SOBREPESO")
elif imc_aredondado >= 30 and imc_aredondado <=39.9:
    print("O seu imc é", imc_aredondado, "você está classsificado em: OBESIDADE")
else:
    print("O seu imc é", imc_aredondado, "você está classsificado em: OBESIDADE GRAVE")
print("")
