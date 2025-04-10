N = int(input())
chu_list = list(map(int, input().split()))
chu_list.sort()

result = [0, 0]

for chu in chu_list:
    new_result = [result[0] + chu, result[1] + chu]
    if new_result[0] - 1 > result[1]:
        break
    result = [result[0], new_result[1]]

print(result[1] + 1)