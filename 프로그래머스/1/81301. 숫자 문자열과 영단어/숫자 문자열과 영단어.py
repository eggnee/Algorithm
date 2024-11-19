def solution(s):
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numberLetter = ''
    answer = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            numberLetter += i     
        if numberLetter in alpha:
            answer += str(alpha.index(numberLetter))
            numberLetter = ''
    return int(answer)