import json
import uuid
from datetime import datetime, date


ARQUIVO = "visitantes.json"


class Visitante:
    def __init__(
        self,
        nome,
        data_nascimento,
        cpf,
        tipo_ingresso,
        data_visita,
        numero_ingresso=None
    ):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.tipo_ingresso = tipo_ingresso
        self.data_visita = data_visita
        self.numero_ingresso = numero_ingresso or str(uuid.uuid4())

    def calcular_idade(self):
        nascimento = datetime.strptime(
            self.data_nascimento,
            "%d/%m/%Y"
        ).date()

        hoje = date.today()
        idade = hoje.year - nascimento.year

        if (hoje.month, hoje.day) < (
            nascimento.month,
            nascimento.day
        ):
            idade -= 1

        return idade

    def para_dict(self):
        return {
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "cpf": self.cpf,
            "tipo_ingresso": self.tipo_ingresso,
            "data_visita": self.data_visita,
            "numero_ingresso": self.numero_ingresso
        }

    @classmethod
    def de_dict(cls, dados):
        return cls(
            dados["nome"],
            dados["data_nascimento"],
            dados["cpf"],
            dados["tipo_ingresso"],
            dados["data_visita"],
            dados.get("numero_ingresso")
        )


class GerenciadorVisitantes:
    def __init__(self, arquivo=ARQUIVO):
        self.arquivo = arquivo
        self.visitantes = self.carregar_visitantes()

    def carregar_visitantes(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                return [
                    Visitante.de_dict(visitante)
                    for visitante in dados
                ]

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []

    def salvar_visitantes(self):
        with open(self.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(
                [visitante.para_dict() for visitante in self.visitantes],
                arquivo,
                indent=4,
                ensure_ascii=False
            )

    def buscar_por_cpf(self, cpf):
        for visitante in self.visitantes:
            if visitante.cpf == cpf:
                return visitante

        return None

    def cadastrar(self, visitante):
        if self.buscar_por_cpf(visitante.cpf) is not None:
            return False

        self.visitantes.append(visitante)
        self.salvar_visitantes()
        return True

    def remover(self, cpf):
        visitante = self.buscar_por_cpf(cpf)

        if visitante is None:
            return False

        self.visitantes.remove(visitante)
        self.salvar_visitantes()
        return True

    def ordenar_por_nome(self):
        self.visitantes.sort(
            key=lambda visitante: visitante.nome.lower()
        )
        self.salvar_visitantes()

    def ordenar_por_idade(self):
        self.visitantes.sort(
            key=lambda visitante: visitante.calcular_idade()
        )
        self.salvar_visitantes()

    def filtrar_por_ingresso(self, tipo):
        encontrados = []

        for visitante in self.visitantes:
            if visitante.tipo_ingresso == tipo:
                encontrados.append(visitante)

        return encontrados

    def consultar_por_data(self, data_procurada):
        encontrados = []

        for visitante in self.visitantes:
            if visitante.data_visita == data_procurada:
                encontrados.append(visitante)

        return encontrados

    def estatisticas(self):
        total = len(self.visitantes)

        if total == 0:
            return None

        quantidade_normal = 0
        quantidade_vip = 0
        quantidade_premium = 0
        soma_idades = 0

        for visitante in self.visitantes:
            tipo = visitante.tipo_ingresso

            if tipo == "Normal":
                quantidade_normal += 1

            elif tipo == "VIP":
                quantidade_vip += 1

            elif tipo == "Premium":
                quantidade_premium += 1

            soma_idades += visitante.calcular_idade()

        return {
            "total": total,
            "normal": quantidade_normal,
            "vip": quantidade_vip,
            "premium": quantidade_premium,
            "media_idade": soma_idades / total
        }


gerenciador = GerenciadorVisitantes()


def carregar_visitantes():
    return gerenciador.visitantes


def salvar_visitantes(visitantes):
    gerenciador.visitantes = visitantes
    gerenciador.salvar_visitantes()


def solicitar_texto(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Campo não pode ficar vazio.")


def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "").strip()

    if not cpf.isdigit():
        return False

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    return True


def solicitar_cpf():
    while True:
        cpf = input("Digite o CPF: ").strip()

        if validar_cpf(cpf):
            return cpf

        print("CPF inválido.")
        print("Informe um CPF com 11 números.")


def solicitar_data_nascimento():
    while True:
        data_texto = input(
            "Digite a data de nascimento (DD/MM/AAAA): "
        ).strip()

        try:
            data = datetime.strptime(
                data_texto,
                "%d/%m/%Y"
            ).date()

            if data > date.today():
                print("A data de nascimento não pode ser futura.")
                continue

            return data.strftime("%d/%m/%Y")

        except ValueError:
            print("Data de nascimento inválida.")


def solicitar_data_visita():
    while True:
        data_texto = input(
            "Digite a data da visita (DD/MM/AAAA): "
        ).strip()

        try:
            data = datetime.strptime(
                data_texto,
                "%d/%m/%Y"
            ).date()

            if data < date.today():
                print()
                print("Data da visita inválida.")
                print("Informe uma data igual ou posterior à data atual.")
                continue

            return data.strftime("%d/%m/%Y")

        except ValueError:
            print()
            print("Data da visita inválida.")
            print("Informe uma data igual ou posterior à data atual.")


def calcular_idade(data_nascimento):
    nascimento = datetime.strptime(
        data_nascimento,
        "%d/%m/%Y"
    ).date()

    hoje = date.today()

    idade = hoje.year - nascimento.year

    if (hoje.month, hoje.day) < (
        nascimento.month,
        nascimento.day
    ):
        idade -= 1

    return idade


def escolher_ingresso():
    while True:
        print()
        print("1 - Normal")
        print("2 - VIP")
        print("3 - Premium")

        opcao = input("Escolha o tipo de ingresso: ").strip()

        if opcao == "1":
            return "Normal"

        elif opcao == "2":
            return "VIP"

        elif opcao == "3":
            return "Premium"

        else:
            print("Opção inválida.")


def cadastrar_visitante():
    print()
    print("=" * 40)
    print("         CADASTRAR VISITANTE")
    print("=" * 40)

    nome = solicitar_texto("Nome: ")
    data_nascimento = solicitar_data_nascimento()
    cpf = solicitar_cpf()

    if gerenciador.buscar_por_cpf(cpf) is not None:
        print()
        print("Já existe um visitante cadastrado com este CPF.")
        print()
        print("O cadastro não foi realizado.")
        return

    print()
    print("Tipo de ingresso:")
    tipo_ingresso = escolher_ingresso()

    data_visita = solicitar_data_visita()

    visitante = Visitante(
        nome,
        data_nascimento,
        cpf,
        tipo_ingresso,
        data_visita
    )

    gerenciador.cadastrar(visitante)

    print()
    print("Visitante cadastrado com sucesso!")
    print(f"Número do ingresso: {visitante.numero_ingresso}")


def remover_visitante():
    print()
    print("=" * 40)
    print("          REMOVER VISITANTE")
    print("=" * 40)

    cpf = solicitar_cpf()

    if not gerenciador.remover(cpf):
        print()
        print("Nenhum visitante encontrado com esse CPF.")
        return

    print()
    print("Visitante removido com sucesso!")


def listar_visitantes():
    visitantes = gerenciador.visitantes

    print()
    print("=" * 40)
    print("              VISITANTES")
    print("=" * 40)

    if not visitantes:
        print()
        print("Nenhum visitante cadastrado.")
        return

    for visitante in visitantes:
        idade = visitante.calcular_idade()

        print()
        print(f"Nome: {visitante.nome}")
        print(f"Idade: {idade}")
        print(f"Ingresso: {visitante.tipo_ingresso}")


def ordenar_visitantes():
    visitantes = gerenciador.visitantes

    if not visitantes:
        print()
        print("Nenhum visitante cadastrado.")
        return

    print()
    print("=" * 40)
    print("          ORDENAR VISITANTES")
    print("=" * 40)
    print()
    print("1 - Ordenar por nome")
    print("2 - Ordenar por idade")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        gerenciador.ordenar_por_nome()

        print()
        print("Visitantes ordenados por nome.")

    elif opcao == "2":
        gerenciador.ordenar_por_idade()

        print()
        print("Visitantes ordenados por idade.")

    else:
        print()
        print("Opção inválida.")
        return

    print()
    print("========================================")
    print("          VISITANTES ORDENADOS")
    print("========================================")

    for visitante in gerenciador.visitantes:
        idade = visitante.calcular_idade()

        print(
            f"{visitante.nome} - "
            f"{idade} anos - "
            f"{visitante.tipo_ingresso}"
        )


def filtrar_visitantes():
    visitantes = gerenciador.visitantes

    if not visitantes:
        print()
        print("Nenhum visitante cadastrado.")
        return

    print()
    print("=" * 40)
    print("        FILTRO DE INGRESSOS")
    print("=" * 40)
    print()
    print("1 - Normal")
    print("2 - VIP")
    print("3 - Premium")

    opcao = input("Escolha: ").strip()

    tipos = {
        "1": "Normal",
        "2": "VIP",
        "3": "Premium"
    }

    if opcao not in tipos:
        print()
        print("Opção inválida.")
        return

    tipo = tipos[opcao]
    encontrados = gerenciador.filtrar_por_ingresso(tipo)

    print()
    print(f"VISITANTES {tipo.upper()}")

    if not encontrados:
        print()
        print("Nenhum visitante encontrado.")
        return

    for visitante in encontrados:
        idade = visitante.calcular_idade()

        print(
            f"{visitante.nome} - "
            f"{idade} anos"
        )


def consultar_visitante():
    print()
    print("=" * 40)
    print("          CONSULTAR VISITANTE")
    print("=" * 40)

    cpf = solicitar_cpf()
    visitante = gerenciador.buscar_por_cpf(cpf)

    if visitante is None:
        print()
        print("Visitante não encontrado.")
        return

    idade = visitante.calcular_idade()

    print()
    print("=" * 40)
    print("          INGRESSO ENCONTRADO")
    print("=" * 40)

    print()
    print(f"Nome: {visitante.nome}")
    print(f"Idade: {idade} anos")
    print(f"CPF: {visitante.cpf}")
    print(
        f"Data de nascimento: "
        f"{visitante.data_nascimento}"
    )
    print(f"Ingresso: {visitante.tipo_ingresso}")
    print(f"Data da visita: {visitante.data_visita}")
    print()
    print("Número do ingresso:")
    print(visitante.numero_ingresso)


def consultar_por_data():
    print()
    print("=" * 40)
    print("      CONSULTAR POR DATA DA VISITA")
    print("=" * 40)

    data_procurada = solicitar_data_visita()
    encontrados = gerenciador.consultar_por_data(data_procurada)

    print()
    print(
        f"VISITANTES DO DIA {data_procurada}"
    )

    if not encontrados:
        print()
        print("Nenhum visitante encontrado para esta data.")
        return

    for visitante in encontrados:
        idade = visitante.calcular_idade()

        print(
            f"{visitante.nome} - "
            f"{idade} anos - "
            f"{visitante.tipo_ingresso}"
        )


def estatisticas():
    print()
    print("=" * 40)
    print("        ESTATÍSTICAS DO PARQUE")
    print("=" * 40)

    dados = gerenciador.estatisticas()

    if dados is None:
        print()
        print(
            "Não existem visitantes cadastrados "
            "para gerar estatísticas."
        )
        return

    print()
    print(f"Total de visitantes: {dados['total']}")
    print()
    print(f"Ingressos Normal: {dados['normal']}")
    print(f"Ingressos VIP: {dados['vip']}")
    print(f"Ingressos Premium: {dados['premium']}")
    print()
    print(
        f"Média de idade: "
        f"{dados['media_idade']:.1f} anos"
    )


def menu():
    while True:
        print()
        print("=" * 40)
        print("            PARQUE AVENTURA")
        print("=" * 40)
        print()
        print("1 - Cadastrar visitante")
        print("2 - Remover visitante")
        print("3 - Listar visitantes")
        print("4 - Ordenar visitantes")
        print("5 - Filtrar visitantes")
        print("6 - Consultar visitante")
        print("7 - Consultar por data da visita")
        print("8 - Estatísticas")
        print("0 - Encerrar programa")
        print()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_visitante()

        elif opcao == "2":
            remover_visitante()

        elif opcao == "3":
            listar_visitantes()

        elif opcao == "4":
            ordenar_visitantes()

        elif opcao == "5":
            filtrar_visitantes()

        elif opcao == "6":
            consultar_visitante()

        elif opcao == "7":
            consultar_por_data()

        elif opcao == "8":
            estatisticas()

        elif opcao == "0":
            print()
            print("Programa encerrado.")
            break

        else:
            print()
            print("Opção inválida.")
            print("Escolha uma opção do menu.")


if __name__ == "__main__":
    menu()