import json
import os
from datetime import datetime


ARQUIVO = "casos.json"


def carregar_casos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    return []


def salvar_casos(casos):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(casos, arquivo, indent=4, ensure_ascii=False)


def encontrar_caso(casos, id_caso):
    for caso in casos:
        if caso["id"] == id_caso:
            return caso

    return None


def criar_caso(casos):
    print("\n=== NOVO CASO ===")

    titulo = input("Título: ")
    local = input("Local: ")

    if casos:
        novo_id = max(caso["id"] for caso in casos) + 1
    else:
        novo_id = 1

    caso = {
        "id": novo_id,
        "titulo": titulo,
        "local": local,
        "suspeitos": [],
        "resolvido": False,
        "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "data_resolucao": None
    }

    casos.append(caso)

    salvar_casos(casos)

    print("\nCaso criado com sucesso!")


def adicionar_suspeito(casos):
    print("\n=== ADICIONAR SUSPEITO ===")

    try:
        id_caso = int(input("Informe o ID do caso: "))
    except ValueError:
        print("ID inválido!")
        return

    caso = encontrar_caso(casos, id_caso)

    if caso is None:
        print("Caso não encontrado!")
        return

    nome = input("Nome: ")

    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida!")
        return

    suspeito = {
        "nome": nome,
        "idade": idade,
        "evidencias": []
    }

    caso["suspeitos"].append(suspeito)

    salvar_casos(casos)

    print("\nSuspeito adicionado!")


def registrar_evidencia(casos):
    print("\n=== NOVA EVIDÊNCIA ===")

    try:
        id_caso = int(input("Caso: "))
    except ValueError:
        print("ID inválido!")
        return

    caso = encontrar_caso(casos, id_caso)

    if caso is None:
        print("Caso não encontrado!")
        return

    if not caso["suspeitos"]:
        print("Este caso ainda não possui suspeitos.")
        return

    nome_suspeito = input("Suspeito: ")

    suspeito_encontrado = None

    for suspeito in caso["suspeitos"]:
        if suspeito["nome"].lower() == nome_suspeito.lower():
            suspeito_encontrado = suspeito
            break

    if suspeito_encontrado is None:
        print("Suspeito não encontrado!")
        return

    print("\nDescrição da evidência:")
    descricao = input()

    suspeito_encontrado["evidencias"].append(descricao)

    salvar_casos(casos)

    print("\nEvidência registrada!")


def analisar_caso(casos):
    print("\n========================================")
    print("          RELATÓRIO DO CASO")
    print("========================================")

    try:
        id_caso = int(input("Informe o ID do caso: "))
    except ValueError:
        print("ID inválido!")
        return

    caso = encontrar_caso(casos, id_caso)

    if caso is None:
        print("Caso não encontrado!")
        return

    print(f"\nCaso: {caso['titulo']}")
    print(f"Local: {caso['local']}")

    if caso["resolvido"]:
        print("Status: RESOLVIDO")
    else:
        print("Status: ABERTO")

    print("\nSuspeitos:")

    if not caso["suspeitos"]:
        print("Nenhum suspeito cadastrado.")
        return

    principal_suspeito = None
    maior_quantidade = -1

    for numero, suspeito in enumerate(caso["suspeitos"], start=1):

        quantidade_evidencias = len(suspeito["evidencias"])

        print(f"\n{numero} - {suspeito['nome']}")
        print(f"    Idade: {suspeito['idade']}")
        print(f"    Evidências: {quantidade_evidencias}")

        if quantidade_evidencias > maior_quantidade:
            maior_quantidade = quantidade_evidencias
            principal_suspeito = suspeito

    print("\n========================================")

    if principal_suspeito:
        print(f"PRINCIPAL SUSPEITO: {principal_suspeito['nome']}")
        print(f"Quantidade de evidências: {maior_quantidade}")

    print("========================================")


def resolver_caso(casos):
    print("\n=== RESOLVER CASO ===")

    try:
        id_caso = int(input("Informe o ID do caso: "))
    except ValueError:
        print("ID inválido!")
        return

    caso = encontrar_caso(casos, id_caso)

    if caso is None:
        print("Caso não encontrado!")
        return

    if not caso["suspeitos"]:
        print("Este caso não possui suspeitos.")
        return

    principal_suspeito = None
    maior_quantidade = -1

    for suspeito in caso["suspeitos"]:
        quantidade = len(suspeito["evidencias"])

        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
            principal_suspeito = suspeito

    print("\nQuem é o responsável?")
    nome_responsavel = input("Digite o nome do suspeito: ")

    print("\nAnalisando evidências...")

    if principal_suspeito["nome"].lower() == nome_responsavel.lower():

        print("✓ Evidências analisadas")
        print("✓ Suspeito identificado")
        print("\nCASO RESOLVIDO!")

        caso["resolvido"] = True
        caso["data_resolucao"] = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        salvar_casos(casos)

    else:

        print("\nAs evidências não são suficientes para confirmar o suspeito.")
        print("O caso continua aberto.")


def listar_casos(casos):
    print("\n========================================")
    print("             LISTA DE CASOS")
    print("========================================")

    if not casos:
        print("Nenhum caso cadastrado.")
        return

    for caso in casos:

        print(f"\nID: {caso['id']}")
        print(f"Título: {caso['titulo']}")
        print(f"Local: {caso['local']}")

        if caso["resolvido"]:
            status = "RESOLVIDO"
        else:
            status = "ABERTO"

        print(f"Status: {status}")
        print(f"Data de criação: {caso['data_criacao']}")

        if caso["data_resolucao"]:
            print(f"Data de resolução: {caso['data_resolucao']}")

        print(f"Quantidade de suspeitos: {len(caso['suspeitos'])}")

        print("----------------------------------------")


def menu():
    casos = carregar_casos()

    while True:

        print("\n========================================")
        print("        AGÊNCIA DE INVESTIGAÇÕES")
        print("========================================")
        print("1 - Criar novo caso")
        print("2 - Adicionar suspeito")
        print("3 - Registrar evidência")
        print("4 - Analisar caso")
        print("5 - Resolver caso")
        print("6 - Listar casos")
        print("7 - Sair")
        print("========================================")

        opcao = input("Escolha: ")

        if opcao == "1":
            criar_caso(casos)

        elif opcao == "2":
            adicionar_suspeito(casos)

        elif opcao == "3":
            registrar_evidencia(casos)

        elif opcao == "4":
            analisar_caso(casos)

        elif opcao == "5":
            resolver_caso(casos)

        elif opcao == "6":
            listar_casos(casos)

        elif opcao == "7":
            salvar_casos(casos)
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    menu()
```
