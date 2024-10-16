nome = str(input('Digite o nome do Heroi: '))
print (f'Seja bem vindo {nome},')
nivelXP = int(input(f"Qual é o nivél de XP do {nome}? "))
if nivelXP < 0:
    print(f'O Herói {nome} precisa de um XP positivo para iniciar')
elif nivelXP >0 and nivelXP <= 1000:
    print(f'O Herói de nome {nome} está no nível de Ferro')
elif nivelXP > 1000 and nivelXP <= 2000:
    print(f'O Herói de nome {nome} está no nível de Bronze')
elif nivelXP > 2001 and nivelXP <= 5000:
    print(f'O Herói de nome {nome} está no nível de Prata')
elif nivelXP > 5001 and nivelXP <= 7000:
    print(f'O Herói de nome {nome} está no nível de Ouro')
elif nivelXP > 7001 and nivelXP <= 8000:
    print(f'O Herói de nome {nome} está no nível de Platina')
elif nivelXP > 8001 and nivelXP <= 9000:
    print(f'O Herói de nome {nome} está no nível de Ascendente')
elif nivelXP > 9001 and nivelXP <= 10000:
    print(f'O Herói de nome {nome} está no nível de Imortal')
elif nivelXP > 10001:
    print(f'O Herói de nome {nome} está no nível de Radiante')
