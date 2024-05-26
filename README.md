def calcular_probabilidade_vitoria(time, resultados):
    vitorias = resultados.count("ganho")
    total_jogos = len(resultados)
    probabilidade = (vitorias / total_jogos) * 100
    return probabilidade

def main():
    # Perguntar pelos nomes dos times
    time1 = input("Digite o nome do Time 1: ")
    time2 = input("Digite o nome do Time 2: ")

    # Coletar os resultados dos últimos 5 jogos de cada time
    resultados_time1 = []
    resultados_time2 = []

    print(f"\nInsira os resultados dos últimos 5 jogos para {time1}:")
    for i in range(5):
        resultado = input(f"Resultado do jogo {i+1} (ganho/perda): ")
        resultados_time1.append(resultado.lower())

    print(f"\nInsira os resultados dos últimos 5 jogos para {time2}:")
    for i in range(5):
        resultado = input(f"Resultado do jogo {i+1} (ganho/perda): ")
        resultados_time2.append(resultado.lower())

    # Calcular a probabilidade de vitória para cada time
    probabilidade_time1 = calcular_probabilidade_vitoria(time1, resultados_time1)
    probabilidade_time2 = calcular_probabilidade_vitoria(time2, resultados_time2)

    # Exibir os resultados
    print("\nProbabilidade de vitória:")
    print(f"{time1}: {probabilidade_time1:.2f}%")
    print(f"{time2}: {probabilidade_time2:.2f}%")

    # Determinar o time com maior probabilidade de vitória
    if probabilidade_time1 > probabilidade_time2:
        print(f"\n{time1} tem maior probabilidade de vitória!")
    elif probabilidade_time2 > probabilidade_time1:
        print(f"\n{time2} tem maior probabilidade de vitória!")
    else:
        print("\nOs times têm a mesma probabilidade de vitória!")

if __name__ == "__main__":
    main()
