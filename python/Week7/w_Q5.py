def common_letter(word1, word2):
    common=[]
    for char in word1:
        if char in word2 and char not in common:
            common.append(char)
    return common


word1="English"
word2="Nepali"
result=common_letter(word1, word2)
print("Common letters between", word1, "and", word2, "are:", result)
