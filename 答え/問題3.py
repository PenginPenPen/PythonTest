x= int(input())
banned_word =[]
for i in range(x):
        banned_word.append(input())
text = input()
for word in banned_word:
        text = text.replace(word, '*' * len(word))
print(text)