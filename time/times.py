import pandas as pd
from scipy.stats import poisson

def calcular_probabilidade_vitoria(media_gols_time1, media_gols_time2):
    max_gols = 10  # Número máximo de gols a considerar para a probabilidade
    prob_vitoria_time1 = 0
    prob_vitoria_time2 = 0
    prob_empate = 0
    
    for i in range(max_gols):
        for j in range(max_gols):
            prob_i = poisson.pmf(i, media_gols_time1)
            prob_j = poisson.pmf(j, media_gols_time2)
            if i > j:
                prob_vitoria_time1 += prob_i * prob_j
            elif i < j:
                prob_vitoria_time2 += prob_i * prob_j
            else:
                prob_empate += prob_i * prob_j
    
    return prob_vitoria_time1, prob_empate, prob_vitoria_time2

def obter_resultados_ultimos_5_jogos(time):
    placares_casa = []
    placares_fora = []
    for i in range(5):
        resultado = input(f'Informe o resultado do jogo {i+1} do {time} (formato "casa x-y fora" ou deixe em branco se não ocorreu): ')
        if resultado.strip():  # Verifica se a entrada não está vazia
            casa, fora = map(int, resultado.split()[0].split('-'))
            placares_casa.append(casa)
            placares_fora.append(fora)
        else:
            placares_casa.append(None)  # Usa None para jogos não ocorridos
            placares_fora.append(None)
    return placares_casa, placares_fora

def main():
    time1 = input('Informe o nome do primeiro time: ')
    print(f'Informe os resultados dos últimos 5 jogos do {time1}:')
    placares_casa_time1, placares_fora_time1 = obter_resultados_ultimos_5_jogos(time1)
    
    time2 = input('Informe o nome do segundo time: ')
    print(f'Informe os resultados dos últimos 5 jogos do {time2}:')
    placares_casa_time2, placares_fora_time2 = obter_resultados_ultimos_5_jogos(time2)
    
    # Calcular as médias de gols por jogo dos últimos jogos que ocorreram
    gols_time1 = [g for g in placares_casa_time1 if g is not None]
    gols_time2 = [g for g in placares_fora_time2 if g is not None]
    
    media_gols_time1 = sum(gols_time1) / len(gols_time1) if gols_time1 else 0
    media_gols_time2 = sum(gols_time2) / len(gols_time2) if gols_time2 else 0
    
    # Calcular a probabilidade de vitória
    if media_gols_time1 > 0 and media_gols_time2 > 0:
        prob_vitoria_time1, prob_empate, prob_vitoria_time2 = calcular_probabilidade_vitoria(media_gols_time1, media_gols_time2)
        print(f'Probabilidade de vitória do {time1}: {prob_vitoria_time1:.2f}')
        print(f'Probabilidade de empate: {prob_empate:.2f}')
        print(f'Probabilidade de vitória do {time2}: {prob_vitoria_time2:.2f}')
    else:
        print('Não há jogos suficientes para calcular as probabilidades.')

if __name__ == "__main__":
    main()
