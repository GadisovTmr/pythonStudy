# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён,
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.



def dictionrary(*names):
    dictinary = {}
    for i in sorted(names):
        first_let = i[0]
        if first_let not in dictinary:
            dictinary[first_let] =[i]
        dictinary[first_let] += [i]

    return dictinary

print(dictionrary('Игорь', 'Сергей','Максим','Тимур','Светлана','Алена', 'Мария'))