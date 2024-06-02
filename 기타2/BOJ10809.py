alpha = [-1] * 26

word = input()

for i in range(len(word)):
    # **if문 추가하여 처음 등장하는 위치를 저장
    if alpha[ord(word[i])-ord('a')] == -1:
        alpha[ord(word[i])-ord('a')] = i

for j in range(len(alpha)):
    print(alpha[j], end=" ")