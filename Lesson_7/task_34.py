# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

poem = input("Введите стихотворение: ")
phrases = poem.split()
vowels = ["а", "о", "у", "ы", "э", "е", "ё", "и", "ю", "я"]
phrases_vowels = list(map(lambda x: list(filter(lambda y: y in vowels, list(x))), phrases))
count = len(phrases_vowels[0])
result = "Парам пам-пам"
for prase in phrases_vowels:
    if len(prase) != count:
        result = "Пам парам"
        break
print(result)
