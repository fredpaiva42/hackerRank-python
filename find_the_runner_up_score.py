n = int(input())
arr = list(map(int, input().split()))
new_arr = []

segundo_maior = 0

for _ in arr:
    if _ not in new_arr:
        new_arr.append(_)

new_arr.sort()

for _ in range(len(new_arr) - 1):
    segundo_maior = new_arr[_]

print(segundo_maior)
