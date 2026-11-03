from funcoes import posicao_valida, preenche_frota


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

print(frota)
