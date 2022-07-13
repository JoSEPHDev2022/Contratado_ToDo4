import time as t

keywords_analista = {'analista de dados': ['python', 'powerbi', 'sql', 'boa comunicação']}
keywords_cientista = {'cientista de dados': ['python', 'banco de dados', 'machine learning', 'resolução de problemas', 'estatística']}

registro_de_aplicacoes = []
aplicantes = {}

lista_aprovados_an = []
lista_aprovados_ci = []

def inserindo_candidatos():
    print("=*"*50)
    print("Bem vindo ao Sistema de Registro de Aplicações de Candidatos - SRAC")
    print("A seguir, insira os nomes, as pretensões de vagas e o resumo dos currículos dos participantes.")
    print("=*"*50)
    t.sleep(1)
    while True:
        aplicantes.clear()
        aplicantes['nome'] = input("Nome do candidato: ")

        while True: 
            aplicantes['vaga'] = input("Para qual vaga é a aplicação: ").lower()
            if aplicantes['vaga'] in ('analista de dados cientista de dados'):
                break
            print("A vaga inserida não está disponível! Seleciona entre 'Analista de Dados' e 'Cientista de Dados'.")
        aplicantes['resumo'] = input("Insira o resumo do currículo do aplicante:\n").lower()
        print(f"\nAdicionando registro do(a) {aplicantes['nome']}...")
        t.sleep(1)
        print("Registro adicionado!")
        registro_de_aplicacoes.append(aplicantes.copy())

        while True:
            adicionar = input("\nDeseja adicionar mais algum participante?[S/N]: ").lower()
            if adicionar in 'sn':
                break
            print("Erro. Responda com 'S' ou 'N'.")
        if adicionar == 'n':
            relatorio_aplicacoes()
        
def relatorio_aplicacoes():
    print("=*"*50)
    t.sleep(1)
    print(f"Tivemos {len(registro_de_aplicacoes)} aplicações para nossas vagas, sendo elas:\n")
    cont = 0 
    for candidaturas in registro_de_aplicacoes:
        cont += 1
        print(f"Aplicação {cont}: {candidaturas['nome']} se aplicou para {candidaturas['vaga']}")
    print()
    print("=*"*50)
    t.sleep(1)
    print("Dessas aplicações:\n")
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

def check_resumos_aprovados():
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
    t.sleep(1)
    print("Nome e Resumo dos candidatos aprovados para Analista de Dados:\n")
    for aprovados in lista_aprovados_an:
        print(f"Nome: {aprovados['nome']}\nResumo >> {aprovados['resumo']}\n")
    print("=*"*50)

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