def solution(strings, n):
    dic = {}
    for i in strings:
        dic[i] = i[n]
    return sorted(dic, key = lambda x : (dic[x], x))