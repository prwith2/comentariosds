import os
from collections import Counter
os.system("cls")
inutil = ["a", "ao", "aos", "aqui", "com", "como", "da", "das", "de", "do", "dos", "e", "em",
    "entre", "isso", "isto", "na", "nas", "no", "nos", "o", "os", "para", "por", "que", "se",
    "seu", "seus", "um", "uma", "é", "alguém", "algo", "ambos", "nenhum", "ninguém", "tudo",
    "todos", "mas", "ou", "aqui", "ali", "lá", "onde", "quando", "como", "assim", "então",
    "quem", "qual", "quanto", "como", "por que", "além disso", "portanto", "contudo", "entretanto",
    "coisa", "coisas", "isso", "aquilo","minhas"]

while True:
    print("""
    0 - Sair
    1 - Adicionar novo comentário
    2 - Gerar mapa de palavras
    """)
    escolha = input("Insira uma opção: ")
    try:
        match int(escolha):
            case 0:
                break

            case 1:
                with open("sujo.txt", "a+", encoding="utf-8") as arq:
                    coment = input("Digite seu comentário: ")
                    arq.write("\n" + coment)

            case 2:
                sujo = open("sujo.txt", "r", encoding="utf-8")
                limpo = open("limpo.txt", "w+", encoding="utf-8")
                comentLimpo = []
                for linha in sujo.readlines():
                    palavras = linha.split()
                    palavras_filtradas = [palavra for palavra in palavras if palavra.lower() not in inutil]
                    comentLimpo.append(" ".join(palavras_filtradas))
                for linha in comentLimpo:
                    limpo.write(linha + "\n")
                limpo.seek(0)
                print(limpo.read())
                limpo.close()
                sujo.close()
                with open("limpo.txt", "r", encoding="utf-8") as limpo:
                    listaPal = (limpo.read()).split()
                    cont = Counter(listaPal)
                    comum = cont.most_common(5)
                    for p,f in comum:
                        print(f"Palavra: {p} | Quantidade: {f}")

            case _:
                print("Opção inválida.")
    except ValueError:
        print("Opção inválida")
