#SISTEMA DE CONTROLE DE VAGAS DE LABORATÓRIO

c = 1
vagas = 20
alunos = 0

print("Bem vindo ao programa de controle de vagas de laboratório, segue os comandos abaixo: ")

while c == 1:
    print("\n============================= LABORATÓRIO DE INFORMÁTICA ============================")
    print("1 - Registrar entrada de aluno ......................................................")
    print("2 - Registrar saída de aluno ........................................................")
    print("3 - Consultar alunos presentes ......................................................")
    print("4 - Consultar vagas disponíveis .....................................................")
    print("5 - Encerrar sistema ................................................................")

    com = int(input("\nDigite o número do comando desejado: "))

    if com == 1:
        print("\nAluno registrado com sucesso!")
        vagas -= 1
        alunos += 1

        if vagas == 0:
            print("\nLaboratório lotado!")

        elif vagas <= 0:
            print("\nImpossível concluir essa ação! Laboratório lotado!")

    elif com == 2:
        print("\nAluno retirado com sucesso!")
        vagas += 1
        alunos -= 1

        if alunos < 0:
            print("\nLaboratório vazio!")

    elif com == 3:
        print(f"\nAlunos presentes - {alunos}")

    elif com == 4:
        print(f"\nVagas disponíveis - {vagas}")

    elif com == 5:
        print("\nPrograma encerrado!")
        break

    else:
        print("\nERROR!")