import random

def gerar_dado(tipo):
    opcoes = {
        'nome': ['Matheo', 'João', 'Maria', 'Yara', 'Leo'],
        'email': ['Matheo@gmail.com', 'joao@hotmail.com', 'Maria@gmail.com', 'yara@hotmail.com', 'Leo@gmail.com'],
        'telefone': ['11 988773322', '11 965335577', '11 953344566', '11 974637486', '11 987648721'],
        'cidade': ['São Paulo', 'Santo André', 'Jardins', 'São Bernardo do campo', 'São Caetano do sul'],
        'estado': ['São Paulo', 'Rio de Janeiro', 'Ceará', 'Minas Gerais', 'Manaus']
    }
    return random.choice(opcoes[tipo])

def salvar_dados(dados):
    with open('dados.txt', 'a') as arquivo:
        for dado in dados:
            arquivo.write(f'{dado}\n')

while True:
    print('Bem vindo ao gerador de dados, para finalizar o programa, digite "parar"')
    print('-'*30)
    print('Escolha uma das opções abaixo para ser gerada aleatoriamente:')
    print('[1] - Nome')
    print('[2] - E-mail')
    print('[3] - Telefone')
    print('[4] - Cidade')
    print('[5] - Estado')

    print(('-'*30))
    escolhas = input('Digite os números das opções desejadas, se escolher mais de uma os separe pelo "espaço" no seu teclado: ')
    escolhas = escolhas.split(' ')

    dados_para_salvar = []
    
    for escolha in escolhas:
        if escolha.strip() in ['1', '2', '3', '4', '5']:
            tipo = {
                '1': 'nome',
                '2': 'email',
                '3': 'telefone',
                '4': 'cidade',
                '5': 'estado'
            }[escolha.strip()]
            dado_gerado = gerar_dado(tipo)
            print(dado_gerado)
            dados_para_salvar.append(f'{tipo.capitalize()}: {dado_gerado}')

    print('-'*30)
    salvar_arquivo = input('Deseja salvar os dados em um arquivo? (s/n): ')
    if salvar_arquivo.lower() == 's':
        salvar_dados(dados_para_salvar)

    print('-'*30)
    entrada = input('Deseja sair do programa? Digite "parar": ')
    if entrada.lower() == 'parar':
        print("Saindo do programa...")
        break