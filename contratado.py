vagas = {
    'analista de dados': ['python', 'powerbi', 'sql', 'boa comunicação'],
    'cientista de dados': ['python', 'banco de dados', 'machine learning', 'resolução de problemas', 'estatística']
}

aplicantes = {}
resumos = {}
lista_participantes = []
lista_resumos = []

num_candidatos = int(input("Quantos candidatos irão ser aplicados?: "))

for ciclos in range(num_candidatos):
    aplicantes['nome'] = input("Nome do candidato: ")
    aplicantes['vaga'] = input("Para qual vaga está se inscrevendo: ")
    resumos['resumo'] = input("Insira o resumo: ")
    lista_participantes.append(aplicantes.copy())
    lista_resumos.append(resumos.copy())


print('\n'+"=*"*35)
print(f"No total, foram registradas as aplicações de {num_candidatos} participantes:\n")

aplicacao_cont = 0
for dicionarios in lista_participantes:
    aplicacao_cont += 1
    print(f"Aplicação {aplicacao_cont}: {dicionarios}")

resum_cont = 0
for resumos in lista_resumos:
    for valores in resumos.values():
        resum_cont += 1
        print(f"Resumo {resum_cont}: {valores}")