def is_isogram(word):
    word = word.upper()
    for i in range(len(word)):
        if word.count(word[i]) > 1:
            return False
    return True

print(is_isogram('moOse'))
