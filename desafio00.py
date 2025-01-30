#Guardando nome do usuário
nome = str(input("Qual seu Nome?"))
Salário = float(input("Qual seu Salário"))
bonus = float(input("Qual o valor do bonus recebido?"))

valor_bonus = 1000 + Salário * bonus

print(f"O Usuario {nome} possui o bonus de {valor_bonus}")