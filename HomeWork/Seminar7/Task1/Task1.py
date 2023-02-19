# Задача 34: 
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-пам

def poem_vowels_count(testing_poem: list, checking_alfabet: set()) -> tuple[int]:

    list_of_vowels_number = []

    for i in range(len(testing_poem)):
        frase_vowels_number = int()
        for j in range(len(checking_alfabet)):
            frase = testing_poem[i]
            count = sum(map(lambda frase: 1 if checking_alfabet[j] in frase else 0, frase))
            frase_vowels_number += count
        list_of_vowels_number.append(frase_vowels_number)

    result = list_of_vowels_number
    return result

message_for_user_1 = 'Введите стихотворение: '
message_for_user_2 = 'Парам пам-пам'
message_for_user_3 = 'Пам парам'
alfabet_vowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]

poem = input(message_for_user_1).split(' ')
result = poem_vowels_count(testing_poem = poem, checking_alfabet = alfabet_vowels)

# Если проверять только "а", то можно так:
# poem = list(map(lambda poem: poem.count('а'), poem))

if sum(result) / len(result) == result[0]:
    print(message_for_user_2)
else:
    print(message_for_user_3)
