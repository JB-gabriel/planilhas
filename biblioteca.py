import pandas as pd

try:

    df = pd.read_excel('tarefas.xlsx')


    print("Planilha carregada com sucesso!")
    print(df)

except FileNotFoundError:
    print("Erro: O arquivo 'tarefas.xlsx' não foi encontrado.")
    print("Verifique se o nome do arquivo está correto e se ele está na mesma pasta do seu script.")