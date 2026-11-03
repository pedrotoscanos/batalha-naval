import random
from funcoes import afundados, faz_jogada, monta_tabuleiros, posicao_valida, posiciona_frota, preenche_frota


embarcacoes = {
    'porta-aviões': [4, 1],
    'navio-tanque': [3, 2],
    'contratorpedeiro': [2, 3],
    'submarino': [1, 4]
}
frota = {}

for nome_navio in embarcacoes:
    tamanho, quantidade = embarcacoes[nome_navio]
    for i in range(quantidade):
        posicionou = False
        while not posicionou:
            print(f'Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}')
            try:
                linha = int(input('Linha: '))
                coluna = int(input('Coluna: '))
            except ValueError:
                print('Esta posição não está válida!')
                continue
            escolha = '1'
            if tamanho > 1:
                escolha = input('[1] Vertical\n[2] Horizontal\n>')
            if escolha not in ['1', '2']:
                print('Esta posição não está válida!')
                continue
            orientacao = 'vertical' if escolha == '1' else 'horizontal'
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
                posicionou = True
            else:
                print('Esta posição não está válida!')

frota_oponente = {
    'porta-aviões': [[[9, 1], [9, 2], [9, 3], [9, 4]]],
    'navio-tanque': [[[6, 0], [6, 1], [6, 2]], [[4, 3], [5, 3], [6, 3]]],
    'contratorpedeiro': [[[1, 6], [1, 7]], [[0, 5], [1, 5]], [[3, 6], [3, 7]]],
    'submarino': [[[2, 7]], [[0, 6]], [[9, 7]], [[7, 6]]]
}
tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)
jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    escolheu = False
    while not escolheu:
        linha = -1
        while not 0 <= linha < 10:
            try:
                linha = int(input('Jogador, qual linha deseja atacar? '))
            except ValueError:
                linha = -1
            if not 0 <= linha < 10:
                print('Linha inválida!')
        coluna = -1
        while not 0 <= coluna < 10:
            try:
                coluna = int(input('Jogador, qual coluna deseja atacar? '))
            except ValueError:
                coluna = -1
            if not 0 <= coluna < 10:
                print('Coluna inválida!')
        if tabuleiro_oponente[linha][coluna] in ['X', '-']:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        else:
            escolheu = True
    faz_jogada(tabuleiro_oponente, linha, coluna)
    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    else:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        while tabuleiro_jogador[linha][coluna] in ['X', '-']:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
        print(f'Seu oponente está atacando na linha {linha} e coluna {coluna}')
        faz_jogada(tabuleiro_jogador, linha, coluna)
        if afundados(frota, tabuleiro_jogador) == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False

