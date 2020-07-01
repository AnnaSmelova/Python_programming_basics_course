# Во входном файле (вы можете читать данные из sys.stdin,
# подключив библиотеку sys) записан текст. Словом считается
# последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или
# символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('06_words_count.txt', 'r', encoding='utf8')

lines = in_file.readlines()
a = set()
for i in range(len(lines)):
    string = lines[i].strip().split()
    for el in string:
        a.add(el)
print(len(a))
