def solution(wallpaper):
    minI = len(wallpaper)
    minJ = len(wallpaper[0])
    maxI = 0
    maxJ = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                minI = min(minI, i)
                minJ = min(minJ, j)
                maxI = max(maxI, i+1)
                maxJ = max(maxJ, j+1)
    return [minI, minJ, maxI, maxJ]