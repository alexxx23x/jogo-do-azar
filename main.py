import random

print("\n===================================")
print("   🎲 BEM-VINDO AO JOGO DE APOSTAS 🎲")
print("===================================\n")
print(" Regras:")
print(" - Você aposta um valor em R$.")
print(" - Escolhe um número de 0 a 15.")
print(" - 6 números serão sorteados.")
print(" - Se um deles for igual ao seu, você ganha 2x o valor apostado!\n")


creditos = int(input(" Deposite quantos R$ você deseja jogar: "))

while creditos > 0:
    print("\n-----------------------------------")
    print(" 💰 R$ atuais:", creditos, "R$")
    aposta = int(input(" Quanto deseja apostar? "))

    if aposta <= 0 or aposta > creditos:
        print(" ❌ Valor inválido, tente novamente.")
        continue

    escolha = int(input(" Escolha um número entre 0 e 15: "))
    if escolha < 0 or escolha > 15:
        print(" ❌ Número inválido, tente novamente.")
        continue

    confirmar = input(f" Confirmar aposta de {aposta} R$ no número {escolha}? (s/n): ")
    if confirmar.lower() != "s":
        sair = input(" Deseja sair do jogo? (s/n): ")
        if sair.lower() == "s":
            break
        else:
            continue

    
    sorteados = [random.randint(0, 15) for _ in range(6)]

    print("\n 🔢 Números sorteados:")
    print(" ---------------------")
    print(" |", sorteados[0], "|", sorteados[1], "|", sorteados[2], "|")
    print(" |", sorteados[3], "|", sorteados[4], "|", sorteados[5], "|")
    print(" ---------------------")

    if escolha in sorteados:
        ganho = aposta * 2
        creditos += ganho
        print(f"\n 🎉 Parabéns! Você ganhou {ganho} R$!")
    else:
        creditos -= aposta
        print(f"\n 😢 Que pena! Você perdeu {aposta} R$.")

print("\n===================================")
print(" 💀 Fim do jogo. Você ficou sem dinheiro ou desistiu.")
print("===================================\n")
