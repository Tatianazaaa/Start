#Задача №3741. Удаление фрагмента
#Дана строка, в которой буква h встречается минимум два раза.
#Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.

text = 'In the hole in the ground there lived a hobbit'
result = (text[:text.find('h')] + text[text.rfind('h') +1:])
print(result)