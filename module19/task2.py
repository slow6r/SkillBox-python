sentence = input("Введите строку: ")
words = sentence.split()
longest_word = max(words, key=len)
print(f'Самое длинное слово: «{longest_word}».')
print(f'Длина этого слова: {len(longest_word)} символов.')
