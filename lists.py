n = int(input())

lista = []

while n > 0:
    entrada = list(map(str, input().split(" ")))
    if entrada[0] == "insert":
        index = int(entrada[1])
        elemento = int(entrada[2])
        lista.insert(index, elemento)
    elif entrada[0] == "print":
        print(lista)
    elif entrada[0] == "remove":
        elemento = int(entrada[1])
        lista.remove(elemento)
    elif entrada[0] == "sort":
        lista.sort()
    elif entrada[0] == "pop":
        lista.pop()
    elif entrada[0] == "reverse":
        lista.reverse()
    elif entrada[0] == "append":
        elemento = int(entrada[1])
        lista.append(elemento)
    n -= 1

# Outra solução
# n = int(input())
# lista = []
#
# comandos = {
#     "insert": lambda i, e: lista.insert(i, e),
#     "print": lambda: print(lista),
#     "remove": lambda e: lista.remove(e),
#     "append": lambda e: lista.append(e),
#     "sort": lambda: lista.sort(),
#     "pop": lambda: lista.pop(),
#     "reverse": lambda: lista.reverse()
# }
#
# for _ in range(n):
#     comando = input().split()
#     acao = comando[0]
#
#     if acao in comandos:
#         args = map(int, comando[1:])
#         comandos[acao](*args)
