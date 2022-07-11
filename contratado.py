keywords_analista = {'analista de dados': ['python', 'powerbi', 'sql', 'boa comunicação']}
keywords_cientista = {'cientista de dados': ['python', 'banco de dados', 'machine learning', 'resolução de problemas', 'estatística']}

registro_de_aplicacoes = []
aplicantes = {}

while True:
    aplicantes.clear()
    aplicantes['nome'] = input("Nome: ")

    while True: 
        aplicantes['vaga'] = input("Qual a vaga que quer se aplicar: ").lower()
        if aplicantes['vaga'] in ('analista de dados cientista de dados'):
            break
        print("A vaga inserida não está disponível!")
    aplicantes['resumo'] = input("Insira o resumo do currículo do aplicante:\n")
    registro_de_aplicacoes.append(aplicantes.copy())

    while True:
        adicionar = input("Deseja adicionar mais algum participante?[S/N]: ").lower()
        if adicionar in 'sn':
            break
        print("Erro. Responda com 'S' ou 'N'.")
    if adicionar == 'n':
        break
        
print("=*"*30)
print(f"Tivemos {len(registro_de_aplicacoes)} aplicações, sendo elas:\n")

cont = 0 
for candidaturas in registro_de_aplicacoes:
    cont += 1
    print(f"Aplicação {cont}: {candidaturas}")

print("=*"*30)
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