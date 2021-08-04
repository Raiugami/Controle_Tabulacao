import os
import time

print("\n -=- -=- -=- -=- -=- -=- -=- TABULAÇÂO ENCAMINHAMENTO-=- -=- -=- -=- -=- -=- -=- \n")

while True:

    arquivo = open("Tabulação.txt", "a")
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

    operacao = int(input(''' Escolha a operação:  

        [1] Aliança
        [2] Banco Pan
        [3] Bradesco Affinity
        [4] Conectcar
        [5] CTF
        [6] ENEL - RJ
        [7] Intermédica PME / Interodonto IOD
        [8] Kroton
        [9] Lenovo
        [10] Marisa
        [11] Motorola
        [12] OI
        [13] PASA
        [14] Sem Parar
        [15] Shell
        [16] Unimed - RJ
        [17] Via Varejo
        [18] VIVO
        [19] White Martins 

        informe aqui:  '''))

    if operacao == 1:
        print("Operação : Aliança")
        arquivo.write("\nOperação : Aliança")
    elif operacao == 2:
        print("Operação : Banco PAN")
        arquivo.write("\nOperação : Banco PAN")
    elif operacao == 3:
        print("Operação : Bradesco Affinity")
        arquivo.write("\nOperação : Bradesco Affinity")
    elif operacao == 4:
        print("Operação : Conectar")
        arquivo.write("\nOperação : Conectar")
    elif operacao == 5:
        print("Operação : CTF")
        arquivo.write("\nOperação : CTF")
    elif operacao == 6:
        print("Operação : ENEL - RJ")
        arquivo.write("\nOperação : ENEL - RJ")
    elif operacao == 7:
        print("Operação : Intermédica PME / Interodonto IOD")
        arquivo.write("\nOperação : Intermédica PME / Interodonto IOD")
    elif operacao == 8:
        print("Operação: Kroton")
        arquivo.write("\nOperação : Kroton")
    elif operacao == 9:
        print("Operação : Lenovo")
        arquivo.write("\nOperação : Lenovo")
    elif operacao == 10:
        print("Operação : Marisa ")
        arquivo.write("\nOperação : Marisa")
    elif operacao == 11:
        print("Operação : Motorola")
        arquivo.write("\nOperação : Motorola")
    elif operacao == 12:
        print("Operação : OI ")
        arquivo.write("\nOperação : OI")
    elif operacao == 13:
        print("Operação : PASA ")
        arquivo.write("\nOperação : PASA")
    elif operacao == 14:
        print("Operação : Sem Parar")
        arquivo.write("\nOperação : Sem Parar")
    elif operacao == 15:
        print("Operação : Shell")
        arquivo.write("\nOperação : Shell")
    elif operacao == 16:
        print("Operação : Unimed - RJ")
        arquivo.write("\nOperação : Unimed - RJ")
    elif operacao == 17:
        print("Operação : Via Varejo")
        arquivo.write("\nOperação : Via Varejo")
    elif operacao == 18:
        print("Operação :VIVO")
        arquivo.write("\nOperação :VIVO")
    elif operacao == 19:
        print("Operação :White Martins")
        arquivo.write("\nOperação :White Martins")
    else:
        print("Nenhuma operação encontrada :(")

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
        link = ""
        if operacao == 1:
            link: str = 'vdi-aliança.atento.com.br:'
        elif operacao == 2:
            link: str = 'vdi-bancopan.atento.com.br:'
        elif operacao == 3:
            link: str = 'vdi-bradesco.atento.com.br:'
        elif operacao == 4:
            link: str = 'vdi-conectcar.atento.com.br:'
        elif operacao == 5:
            link: str = 'vdi-ctf.atento.com.br:'
        elif operacao == 6:
            link: str = 'vdi-enel.atento.com.br:'
        elif operacao == 7:
            link: str = 'vdi-intermedica.atento.com.br:'
        elif operacao == 8:
            link: str = 'vdi-kroton.atento.com.br:'
        elif operacao == 9:
            link: str = 'vdi-lenovo.atento.com.br:'
        elif operacao == 10:
            link: str = 'vdi-marisa.atento.com.br:'
        elif operacao == 11:
            link: str = 'vdi-motorola.atento.com.br:'
        elif operacao == 12:
            link: str = 'vdi-oi.atento.com.br:'
        elif operacao == 13:
            link: str = 'vdi-pasa.atento.com.br:'
        elif operacao == 14:
            link: str = 'vdi-semparar.atento.com.br:'
        elif operacao == 15:
            link: str = 'vdi-shell.atento.com.br:'
        elif operacao == 16:
            link: str = 'vdi-unimed.atento.com.br:'
        elif operacao == 17:
            link: str = 'vdi-viavarejo.atento.com.br:'
        elif operacao == 18:
            link: str = 'vdi-vivo.atento.com.br:'
        elif operacao == 19:
            link: str = 'vdi-whitemartins.atento.com.br:'

        print("Problema: TS - VDI problema\n")
        arquivo.write("\nProblema: TS - VDI problema")
        porta = str(input('\nInforme a porta da área remota: '))
        arquivo.write("\nPorta: {}{}\n".format(link, porta))
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

    horario = str(input('\nInforme o horario de trabalho do colaborador: '))
    arquivo.write("Horario: {}\n".format(horario))

    print("Processando...")
    time.sleep(3)
    print(" \n ======== Registrado :D ======== \n ")
    time.sleep(3)

    arquivo.write('-=-'*24)
    arquivo.close()
    os.system("notepad.exe Tabulação.txt")
