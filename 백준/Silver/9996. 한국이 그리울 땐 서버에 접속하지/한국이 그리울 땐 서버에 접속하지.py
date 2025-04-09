N = int(input())
prefix, postfix = input().split("*")

for _ in range(N):
    word = input()
    if word[:len(prefix)] == prefix and word[-len(postfix):] == postfix:
        if len(word) >= len(prefix) + len(postfix):
            print("DA")
            continue
    
    print("NE")
