#O operador % (módulo) devolve o resto da divisão. 
# Use-o para verificar se o número de moedas de um jogador é par. 
# (Dica: moedas % 2 == 0).

moedas = int(input("Quantas moedas o jogador possui? "))

if moedas % 2 == 0:
    print("O número de moedas é par")
else:
    print("O número de moedas é ímpar.")
