import json

try:
    with open("animais.json", "r", encoding="utf-8") as arquivo:
        animais = json.load(arquivo)

except FileNotFoundError:
    animais = []

while True:
    print("\n=== SISTEMA DE ADOÇÃO DE ANIMAIS ===")
    print("1 - Cadastrar animal")
    print("2 - Listar animais")
    print("3 - Remover animal")
    print("4 - Editar animal")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        while True:
            nome = input("Digite o nome do animal: ").strip().capitalize()

            if nome != "":
                break

            print("O nome do animal não pode ficar vazio.")
            
        while True:
            especie = input("Digite a espécie do animal: ").strip().capitalize()

            if especie != "":
                break

            print("A espécie do animal não pode ficar vazia.")

        while True:
            try:
                idade = int(input("Digite a idade do animal: "))

                if idade >= 0:
                    break

                print("A idade não pode ser negativa.")

            except ValueError:
                print("Digite uma idade válida usando números inteiros.")

        animal = {
            "nome": nome,
            "especie": especie,
            "idade": idade
      }

        animais.append(animal)

        with open("animais.json", "w", encoding="utf-8") as arquivo:
            json.dump(animais, arquivo, indent=4, ensure_ascii=False)

        print(f"\nAnimal {nome} cadastrado com sucesso!")

    elif opcao == "2":
        print("\n=== ANIMAIS CADASTRADOS ===")

        if len(animais) == 0:
            print("Nenhum animal cadastrado.")

        else:
            for animal in animais:
                print(f"Nome: {animal['nome']}")
                print(f"Espécie: {animal['especie']}")
                print(f"Idade: {animal['idade']} ano(s)")
                print("-" * 30)
 
    elif opcao == "3":
        print("\n=== REMOVER ANIMAL ===")

        if len(animais) == 0:
            print("Nenhum animal cadastrado para remover.")

        else:
            for i, animal in enumerate(animais, start=1):
                print(f"{i} - {animal['nome']} ({animal['especie']})")

            while True:
                try:
                    numero = int(input("Digite o número do animal que deseja remover: "))

                    if numero <= len(animais) and numero > 0:
                        break

                    print("Digite um número válido.")

                except ValueError:
                    print("Digite uma opção válida usando números inteiros.")

            indice = numero - 1
            animal_removido = animais.pop(indice)

            with open("animais.json", "w", encoding="utf-8") as arquivo:
                json.dump(animais, arquivo, indent=4, ensure_ascii=False)

            print(f"Animal {animal_removido['nome']} removido com sucesso!")

    elif opcao == "4":
        print("\n=== EDITAR ANIMAL ===")

        if len(animais) == 0:
            print("Nenhum animal cadastrado para editar.")

        else:
            for i, animal in enumerate(animais, start=1):
                print(f"{i} - {animal['nome']} — {animal['idade']} ano(s) ({animal['especie']})")

            while True:
                try:
                    numero = int(input("Digite o número do animal que deseja editar: "))

                    if numero <= len(animais) and numero > 0:
                        break

                    print("Digite um número válido de animal.")

                except ValueError:
                    print("Digite um número inteiro válido.")

            indice = numero - 1

            print("1 - Nome\n2 - Idade\n3 - Espécie")

            while True:
                try:
                    campo_escolhido = int(input("Qual campo deseja editar: "))

                    if campo_escolhido <= 3 and campo_escolhido > 0:
                        break

                    print("Digite uma opção válida entre 1 e 3.")

                except ValueError:
                    print("Digite um número inteiro válido.") 

            if campo_escolhido == 1:
                while True:
                    novo_nome = input("Digite o novo nome do animal: ").strip().capitalize()

                    if novo_nome != "":
                        break

                    print("O nome do animal não pode ficar vazio.")

                animais[indice]['nome'] = novo_nome

            elif campo_escolhido == 2:
                while True: 
                    try:
                        nova_idade = int(input("Digite a nova idade do animal: "))
                        if nova_idade >= 0:
                            break

                        print("A idade não pode ser negativa.")

                    except ValueError:
                        print("Digite um número inteiro válido.")

                animais[indice]['idade'] = nova_idade

            elif campo_escolhido == 3:
                while True: 
                    nova_especie = input("Digite a nova espécie do animal: ").strip().capitalize()

                    if nova_especie != "":
                        break

                    print("A espécie do animal não pode ficar vazia.")

                animais[indice]['especie'] = nova_especie

            with open("animais.json", "w", encoding="utf-8") as arquivo:
                json.dump(animais, arquivo, indent=4, ensure_ascii=False)

            print("Animal atualizado com sucesso!")


    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")
