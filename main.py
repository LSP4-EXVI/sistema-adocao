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

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")
