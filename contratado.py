import time as t # Importanto o módulo time para uso durante a saída de dados.

# Dicionários contendo as keywords para as vagas de Analista e Cientista de Dados.
keywords_analista = {'analista de dados': ['python', 'powerbi', 'sql', 'boa comunicação']} 
keywords_cientista = {'cientista de dados': ['python', 'banco de dados', 'machine learning', 'resolução de problemas', 'estatística']}

# Uma lista que abriga os registros de aplicações de candidatos contidos no dicionário 'aplicantes'.
registro_de_aplicacoes = []
aplicantes = {}

# Duas listas que abrigam os candidatos cujos currículos possuem ao menos uma palavra chave de acordo com a vaga na qual se candidataram.
lista_aprovados_an = []
lista_aprovados_ci = []

# Função de inserção de candidatos no sistema (nome, a vaga desejada e o resumo do candidato).
def inserindo_candidatos():
    print("=*"*50)
    print("Bem vindo ao Sistema de Registro de Aplicações de Candidatos - SRAC")
    print("A seguir, insira os nomes, as pretensões de vagas e o resumo dos currículos dos participantes.")
    print("=*"*50)
    t.sleep(1)

    while True:
        aplicantes.clear() # A cada ciclo de adição de candidatos, o dicionário é limpo para alojar o novo participante
        aplicantes['nome'] = input("Nome do candidato: ")

        # Esse bloco de While serve como prevenção de erro para caso o usuário selecione outra vaga que não seja a de analista ou cientista de dados.
        while True: 
            aplicantes['vaga'] = input("Para qual vaga é a aplicação: ").lower()
            if aplicantes['vaga'] == ('analista de dados' or 'cientista de dados'):
                break
            print("A vaga inserida não está disponível! Seleciona entre 'Analista de Dados' e 'Cientista de Dados'.")
        aplicantes['resumo'] = input("Insira o resumo do currículo do aplicante:\n").lower()

        print(f"\nAdicionando registro do(a) {aplicantes['nome']}...")
        t.sleep(1)
        print("Registro adicionado!")
        registro_de_aplicacoes.append(aplicantes.copy()) # O registro do candidato é inserido na lista de registros, o ciclo se reinicia caso o usuário queira inserir
        # mais candidatos, limpando o dicionário na linha 24 e reeiniciando o processo de adição.

        # Esse bloco de While serve de prevenção de erro para garantir que o usuário insira apenas 'S' ou 'N' como resposta.
        while True:
            adicionar = input("\nDeseja adicionar mais algum participante?[S/N]: ").lower()
            if adicionar in 'sn':
                break
            print("Erro. Responda com 'S' ou 'N'.")
        if adicionar == 'n':
            relatorio_aplicacoes()
        
# Função que lista todos os registros feitos de candidatos no sistema.
def relatorio_aplicacoes():
    print("=*"*50)
    t.sleep(1)
    print(f"Tivemos {len(registro_de_aplicacoes)} aplicações para nossas vagas, sendo elas:\n") # Mostra o total de aplicações.

    # Ciclo for simples para listar cada uma das aplicações dos candidatos.
    cont = 0 
    for candidaturas in registro_de_aplicacoes:
        cont += 1
        print(f"Aplicação {cont}: {candidaturas['nome']} se aplicou para {candidaturas['vaga']}")
    print()

    print("=*"*50)
    t.sleep(1)
    print("Dessas aplicações:\n")

    # Ciclo for que conta e depois printa na tela quantas aplicações foram para Analista e para Cientista de dados.
    candidaturas_analista = 0
    candidaturas_cientista = 0
    for candidatos in registro_de_aplicacoes:
        if candidatos['vaga'] == 'analista de dados':
            candidaturas_analista += 1
        if candidatos['vaga'] == 'cientista de dados':
            candidaturas_cientista += 1

    print(f"{candidaturas_analista} foram para Analista de Dados.")
    print(f"{candidaturas_cientista} foram para Cientista de Dados.")
    print("=*"*50)
    check_resumos_aprovados()

# Função que faz a verificação dos currículos, retornando os que contém no minimo uma keyword válida para a vaga na qual se aplicou o candidato e printa esses
# resumos na tela.
def check_resumos_aprovados():
    # Loop for que divide os registros de resumos de acordo com a vaga aplicada pelo participante e faz a verificação das keywords, salvando esses currículos
    # selecionados em uma lista de resumos aprovados.
    for candidatos in registro_de_aplicacoes:
        if candidatos['vaga'] == 'analista de dados':
            for keywords_1 in keywords_analista.values():
                for palavras_1 in keywords_1:
                    if palavras_1 in candidatos['resumo']:
                        lista_aprovados_an.append(candidatos)
                        break
                    continue
                break
        if candidatos['vaga'] == 'cientista de dados':
            for keywords_2 in keywords_cientista.values():
                for palavras_2 in keywords_2:
                    if palavras_2 in candidatos['resumo']:
                        lista_aprovados_ci.append(candidatos)
                        break
                    continue
                break

    # Ciclo for que apresenta na tela os resumos aprovados para a vaga de Analista de Dados. 
    t.sleep(1)
    print("Nome e Resumo dos candidatos aprovados para Analista de Dados:\n")
    for aprovados in lista_aprovados_an:
        print(f"Nome: {aprovados['nome']}\nResumo >> {aprovados['resumo']}\n")
    print("=*"*50)

    # Ciclo for que apresenta na tela os resumos aprovados para a vaga de Cientista de Dados.
    t.sleep(1)
    print("Nome e Resumo dos candidatos aprovados para Cientista de Dados:\n")
    for aprovados_2 in lista_aprovados_ci:
        print((f"Nome: {aprovados_2['nome']}\nResumo >> {aprovados_2['resumo']}\n"))
    print("=*"*50)

    t.sleep(1)
    print("Finalizando...")
    t.sleep(1)
    print("Programa Finalizado!")
    exit()

inserindo_candidatos()