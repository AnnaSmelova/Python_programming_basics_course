# Во входном файле (вы можете читать данные из файла input.txt) записан текст
# Словом считается последовательность непробельных подряд идущих символов.
# Слова разделены одним или большим числом пробелов или символами конца строки
# Для каждого слова из этого текста подсчитайте,
# сколько раз оно встречалось в этом тексте ранее.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('14_word_meet_number.txt', 'r', encoding='utf8')

d = {}
lines = in_file.readlines()
for i in range(len(lines)):
    string = lines[i].strip().split()
    for k in string:
        if k in d:
            print(d[k], end=' ')
            d[k] += 1
        else:
            print(0, end=' ')
            d[k] = 1
