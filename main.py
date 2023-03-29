print("*************************")
print("***ASTROLOGY  NOTEBOOK***")
print("*************************\n")

fim = False
notebook = {'empty':'empty'} #Como criar um dict vazio?
# Preenche o notebook com "sem entrada"

for x in range(12):
    for y in range(13):
        for z in range(13):
            notebook.update({(x, y, z): 'sem entradas'})

while (fim == False):

    #Inputa a ação (Consultar ou editar notebook) e pergunta em qual campo será inserido o registro
    acao = int(input("Consulta (1) Inserir Registro (2) Sair (3)"))

    if (acao == 3):
        break

    print("Selecione Planeta:")
    planeta = int(input ("Nulo (0) - Sol (1) - Lua (2) - Asc (3) - Mercúrio (4) - Vênus (5) - Marte (6) \n"
                    " - Saturno (7) - Jupiter (8) - Urano (9) - Netuno (10) - Plutão(11)"))

    print("Selecione Signo:")
    signo = int(input ("Nulo (0) - Áries (1) - Touro (2) - Gêmeos (3) -  Câncer (4) \n"
                  " Leão (5) - Virgem (6) - Libra (7) - Escorpião (8)\n"
                  " Sagitário (9) - Capricórnio (10) - Aquário (11) - Peixes(12)"))

    print("Selecione Casa:")
    casa = int(input ("Nulo (0) - Casas (1-12)"))
    chave = (planeta, signo, casa)

    #Consulta:
    if (acao == 1):
        print(notebook[chave])

    #Edição:
    elif (acao == 2):

        if (notebook[chave] == 'sem entradas'):
            anotacao = str(input(f"Insira sua entrada para Planeta:{planeta}, Signo:{signo}, Casa:{casa}"))
            notebook.update({chave: anotacao})

        else:
            anotacao = str(input(f"Insira sua entrada para Planeta:{planeta}, Signo:{signo}, Casa:{casa}"))
            nova_anotacao = str(f'{notebook[chave]} \n {anotacao}')
            notebook.update({chave : nova_anotacao}) #Preciso fazer as anotações aparecerem separadas

    else :
        print("Comando inválido")
