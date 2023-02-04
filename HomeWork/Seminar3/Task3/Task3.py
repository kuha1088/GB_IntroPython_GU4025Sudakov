# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Пример:
# ноутбук
# 12

def get_user_word(msg):
    
    print(f"{msg}")
    
    while(True):
        try:
            user_input = input()
            if (user_input.isalpha()):
                return(user_input.upper())
            else:
                raise ValueError
        except ValueError:
            print("Введенное значение не соответствует правилам игры, повторите ввод.")

def word_check(word, dictionary):
    
    result = int()

    for i in word:
        result += dictionary.get(i)

    return result

dict_keys_eng_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
dict_keys_rus_1 = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
dict_keys_eng_2 = ['D', 'G']
dict_keys_rus_2 = ['Д', 'К', 'Л', 'М', 'П', 'У']
dict_keys_eng_3 = ['B', 'C', 'M', 'P']
dict_keys_rus_3 = ['Б', 'Г', 'Ё', 'Ь', 'Я']
dict_keys_eng_4 = ['F', 'H', 'V', 'W', 'Y']
dict_keys_rus_4 = ['Й', 'Ы']
dict_keys_eng_5 = ['K']
dict_keys_rus_5 = ['Ж', 'З', 'Х', 'Ц', 'Ч']
dict_keys_eng_8 = ['J', 'X']
dict_keys_rus_8 = ['Ш', 'Э', 'Ю']
dict_keys_eng_10 = ['Q', 'Z']
dict_keys_rus_10 = ['Ф', 'Щ', 'Ъ']

dict_eng_1 = dict.fromkeys(dict_keys_eng_1, 1)
dict_rus_1 = dict.fromkeys(dict_keys_rus_1, 1)
dict_eng_2 = dict.fromkeys(dict_keys_eng_2, 2)
dict_rus_2 = dict.fromkeys(dict_keys_rus_2, 2)
dict_eng_3 = dict.fromkeys(dict_keys_eng_3, 3)
dict_rus_3 = dict.fromkeys(dict_keys_rus_3, 3)
dict_eng_4 = dict.fromkeys(dict_keys_eng_4, 4)
dict_rus_4 = dict.fromkeys(dict_keys_rus_4, 4)
dict_eng_5 = dict.fromkeys(dict_keys_eng_5, 5)
dict_rus_5 = dict.fromkeys(dict_keys_rus_5, 5)
dict_eng_8 = dict.fromkeys(dict_keys_eng_8, 8)
dict_rus_8 = dict.fromkeys(dict_keys_rus_8, 8)
dict_eng_10 = dict.fromkeys(dict_keys_eng_10, 10)
dict_rus_10 = dict.fromkeys(dict_keys_rus_10, 10)

merge_dict = {**dict_eng_1, **dict_rus_1, **dict_eng_2, **dict_rus_2, **dict_eng_3, **dict_rus_3,\
              **dict_eng_4, **dict_eng_4, **dict_eng_5, **dict_rus_5, **dict_eng_8, **dict_rus_8,\
              **dict_eng_10, **dict_rus_10} 

print()
user_word = get_user_word(msg = "Введите слово: ")
print()

user_word = tuple(user_word)

result = word_check(word = user_word, dictionary = merge_dict)

print(f"Стоимость введенного слова = {result} очка(ов)")
