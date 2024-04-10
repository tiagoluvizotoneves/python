# Notificador de Meta de Vendas

Este projeto visa monitorar as vendas mensais através de arquivos Excel e enviar notificações SMS quando um vendedor excede a meta estabelecida de vendas.

## Tecnologias Utilizadas

- Python
- Pandas: Para manipulação dos dados dos arquivos Excel.
- Twilio API: Para enviar notificações SMS.

## Configuração

Para executar este projeto, você precisa configurar algumas coisas:

### Instalação de Dependências

Certifique-se de que Python 3.x está instalado no seu sistema.
Instale as dependências necessárias executando `pip install -r requirements.txt` no terminal.


### Configuração da Twilio API

1. Crie uma conta no [Twilio](https://www.twilio.com/).
2. Obtenha o `account_sid` e `auth_token` do dashboard da Twilio.
3. Adquira um número de telefone na Twilio para enviar as mensagens.

### Dados

Os dados de vendas devem estar em arquivos Excel nomeados com o nome do mês (por exemplo, `janeiro.xlsx`, `fevereiro.xlsx`, etc.), contendo as colunas `Vendedor` e `Vendas`.

## Como Executar

1. Atualize o script com seu `account_sid`, `auth_token`, e os números de telefone do remetente e destinatário.
2. Coloque os arquivos de dados na mesma pasta do script.
3. Execute o script com o seguinte comando:

python main.py


## Funcionalidades

- **Leitura de Dados:** O script lê os dados de vendas dos arquivos Excel para cada mês.
- **Verificação de Meta:** Verifica se algum vendedor excedeu a meta de vendas de 55.000.
- **Notificação SMS:** Envia uma notificação SMS quando a meta é atingida, indicando o mês, o vendedor e o valor das vendas.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
