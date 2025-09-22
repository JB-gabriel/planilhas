import pandas as pd


def carregar_planilha():

    try:
        df = pd.read_excel('tarefas.xlsx')
        print(df)

    except FileNotFoundError:
        print("Erro: O arquivo 'tarefas.xlsx' não foi encontrado.")
        print("Verifique se o nome do arquivo está correto e se ele está na mesma pasta do seu script.")


