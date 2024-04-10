# Importa a biblioteca pandas para manipulação de dados
import pandas as pd
# Importa a classe Client da biblioteca twilio.rest para enviar mensagens SMS
from twilio.rest import Client

# Define as credenciais da conta Twilio
account_sid = "XXXXXX"
auth_token = "XXXXX"

# Cria uma instância do cliente Twilio com as credenciais fornecidas
client = Client(account_sid, auth_token)

# Lista de meses para analisar as vendas
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

# Itera sobre a lista de meses para processar os arquivos de vendas correspondentes
for mes in lista_meses:
    # Lê o arquivo Excel de vendas para o mês atual da iteração
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # Verifica se há alguma venda maior que 55000 no mês
    if (tabela_vendas['Vendas'] > 55000).any():
        # Encontra o nome do vendedor que superou a meta de vendas
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        # Encontra o valor de vendas que superou a meta
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        # Cria e envia uma mensagem SMS informando sobre o vendedor que bateu a meta e o valor de suas vendas
        message = client.messages.create(
            to="XXXXX",  # Número do destinatário da mensagem
            from_="XXXXX", # Número do remetente (fornecido pelo Twilio)
            body=f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')  # Corpo da mensagem
        # Imprime o identificador da mensagem enviada
        print(message.sid)
