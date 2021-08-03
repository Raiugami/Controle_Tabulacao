import os
import time

print("\n -=- -=- -=- -=- -=- -=- -=- TABULAÇÂO ENCAMINHAMENTO-=- -=- -=- -=- -=- -=- -=- \n")

while True:

    arquivo = open("TMA2.txt", "a")
    problema = int(input(''' Escolha o problema:  

    [1] SD - Aplicativo com Problema
    [2] SD - Bitlocker
    [3] SD - CPU Problema
    [4] SD - Headset Problema
    [5] SD - Monitor Problema
    [6] SD - Mouse Problema
    [7] SD - Teclado Problema
    [8] SD - Windows - Falha de logon
    [9] SD - Windows - Sistema Operacional
    [10] TS - VDI problema
    [11] TSWVD - VDI problema


    informe aqui:  '''))

    if problema == 1:
        print("Problema: SD - Aplicativo com Problema")
        arquivo.write("\nProblema: SD - Aplicativo com Problema\n")

    elif problema == 2:
        print("Problema: SD - Bitlocker")
        arquivo.write("\nProblema: SD - Bitlocker\n")

    elif problema == 3:
        print("Problema: SD - CPU Problema")
        arquivo.write("\nProblema: SD - CPU Problema\n")
        rua = str(input('\nInforme a rua do colaborador: '))
        arquivo.write("Rua: {}\n".format(rua))
        numero = str(input('\nInforme o numero da casa do colaborador: '))
        arquivo.write("Horario: {}\n".format(numero))
        cep = str(input('\nInforme o CEP do colaborador: '))
        arquivo.write("Horario: {}\n".format(cep))

    elif problema == 4:
        print("Problema: SD - Headset Problema")
        arquivo.write("\nProblema: SD - Headset Problema\n")
        rua = str(input('\nInforme a rua do colaborador: '))
        arquivo.write("Rua: {}\n".format(rua))
        numero = str(input('\nInforme o numero da casa do colaborador: '))
        arquivo.write("Horario: {}\n".format(numero))
        cep = str(input('\nInforme o CEP do colaborador: '))
        arquivo.write("Horario: {}\n".format(cep))

    elif problema == 5:
        print("Problema: SD - Monitor Problema")
        arquivo.write("\nProblema: SD - Monitor Problema\n")
        rua = str(input('\nInforme a rua do colaborador: '))
        arquivo.write("Rua: {}\n".format(rua))
        numero = str(input('\nInforme o numero da casa do colaborador: '))
        arquivo.write("Horario: {}\n".format(numero))
        cep = str(input('\nInforme o CEP do colaborador: '))
        arquivo.write("Horario: {}\n".format(cep))

    elif problema == 6:
        print("Problema: SD - Mouse Problema")
        arquivo.write("\nProblema: SD - Mouse Problema\n")
        rua = str(input('\nInforme a rua do colaborador: '))
        arquivo.write("Rua: {}\n".format(rua))
        numero = str(input('\nInforme o numero da casa do colaborador: '))
        arquivo.write("Horario: {}\n".format(numero))
        cep = str(input('\nInforme o CEP do colaborador: '))
        arquivo.write("Horario: {}\n".format(cep))

    elif problema == 7:
        print("Problema: SD - Teclado Problema")
        arquivo.write("\nProblema: SD - Teclado Problema")
        rua = str(input('\nInforme a rua do colaborador: '))
        arquivo.write("Rua: {}\n".format(rua))
        numero = str(input('\nInforme o numero da casa do colaborador: '))
        arquivo.write("Horario: {}\n".format(numero))
        cep = str(input('\nInforme o CEP do colaborador: '))
        arquivo.write("Horario: {}\n".format(cep))

    elif problema == 8:
        print("Problema: SD - Windows - Falha de logon")
        arquivo.write("\nProblema: SD - Windows - Falha de logon")

    elif problema == 9:
        print("Problema: SD - Windows - Sistema Operacional")
        arquivo.write("\nProblema: SD - Windows - Sistema Operacional\n")

    elif problema == 10:
        print("Problema: TS - VDI problema\n")
        arquivo.write("\nProblema: TS - VDI problema")
        porta = str(input('\nInforme o endereço e porta da área remota: (ex:vdi-viavarejo.atento.com.br:3359) : '))
        arquivo.write("Link: {}\n".format(porta))

    elif problema == 11:
        print("Problema: TSVDI - WVD Microsoft\n")
        arquivo.write("\nProblema: TSWVD - VDI problema\n")
        link = str(input('\nInforme o link da área remota: '))
        arquivo.write("Link: {}\n".format(link))
        pool = str(input('\nInforme o pool da área remota: '))
        arquivo.write("Link: {}\n".format(pool))

    else:
        print("Opção invalida :( ")

    colaborador = str(input('\nInforme o nome do colaborador: '))
    arquivo.write("Colaborador: {}\n".format(colaborador))

    re = str(input('\nInforme o RE do colaborador: '))
    arquivo.write("RE: {}\n".format(re))

    telefone = str(input('\nInforme o telefone(com DDD) do colaborador: '))
    arquivo.write("Telefone: {}\n".format(telefone))

    supervisor = str(input('\nInforme o nome do supervisor: '))
    arquivo.write("Supervisor: {}\n".format(supervisor))

    site = str(input('\nInforme o site do colaborador: '))
    arquivo.write("Site: {}\n".format(site))

    problema = str(input('\nInforme a operação do colaborador: '))
    arquivo.write("Operação: {}\n".format(problema))

    horario = str(input('\nInforme o horario de trabalho do colaborador: '))
    arquivo.write("Horario: {}\n".format(horario))

    print("Processando...")
    time.sleep(3)
    print(" \n ======== Registrado :D ======== \n ")
    time.sleep(3)

    arquivo.write('-=-' * 24)
    arquivo.close()
    os.system("notepad.exe TMA2.txt")
