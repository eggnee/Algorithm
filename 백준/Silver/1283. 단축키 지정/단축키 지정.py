alpha = set([])

def plusPar(word, i):
    alpha.add(word[i].upper())
    if len(word) - 1 == i:
        return word[0:i] + '[' + word[i] + ']'
    else:
        return word[0:i] + '[' + word[i] + ']' + word[i+1:]

def setKey(words):
    for i in range(len(words)):
            for j in range(len(words[i])):
                #print(words[i][j])
                if words[i][j].upper() not in alpha:
                    
                    words[i] = plusPar(words[i], j)
                    return

N = int(input())
arr = []

for _ in range(N):
    arr.append(list(input().split()))


for i in range(N):
    flag = False
    for j in range(len(arr[i])):
        word = arr[i][j]
        if word[0].upper() not in alpha:
            arr[i][j] = plusPar(word, 0)
            flag = True
            break
    if not flag:
        setKey(arr[i])

for words in arr:
    for word in words:
        print(word, end = " ")
    print()
