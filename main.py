from re import *



def file_to_set(cur_file, cur_set):
    for line in cur_file:
        cur_set.add(line)


def spaces_delete(cur_set):
    res = set()
    for line in cur_set:
        new_line = sub(" ", "", line)
        res.add(new_line)
    return res

def oper_count(oper, oper_dict, f_set):
    oper_dict[oper] = 0
    for line in f_set:
        oper_dict[oper] += line.count(oper)
    

# Открытие файла и получение из него данных

f1 = open('test.py', 'r')
f2 = open('test_copy.py', 'r')
set1 = set()
set2 = set()

file_to_set(f1, set1)
file_to_set(f2, set2)


# Построковая обработка и сравнение множеств

set_wo1 = spaces_delete(set1)
set_wo2 = spaces_delete(set2)
inter_set = set_wo1 & set_wo2
len1 = len(set_wo1)
len2 = len(set_wo2)
len_inter = len(inter_set)


# Токенизация и сравнение

# Сравнение количественных параметров

oper_dict1 = dict()
oper_dict2 = dict()
oper_res = []

oper_count("+", oper_dict1, set1)
oper_count("-", oper_dict1, set1)
oper_count("=", oper_dict1, set1)
oper_count("/", oper_dict1, set1)
oper_count("//", oper_dict1, set1)
oper_count("^", oper_dict1, set1)
oper_count("|", oper_dict1, set1)
oper_count("&", oper_dict1, set1)
oper_count("if ", oper_dict1, set1)
oper_count("elif ", oper_dict1, set1)
oper_count("else ", oper_dict1, set1)
oper_count("for ", oper_dict1, set1)
oper_count("while ", oper_dict1, set1)
oper_count("def ", oper_dict1, set1)

oper_count("+", oper_dict2, set2)
oper_count("-", oper_dict2, set2)
oper_count("=", oper_dict2, set2)
oper_count("/", oper_dict2, set2)
oper_count("//", oper_dict2, set2)
oper_count("^", oper_dict2, set2)
oper_count("|", oper_dict2, set2)
oper_count("&", oper_dict2, set2)
oper_count("if ", oper_dict2, set2)
oper_count("elif ", oper_dict2, set2)
oper_count("else ", oper_dict2, set2)
oper_count("for ", oper_dict2, set2)
oper_count("while ", oper_dict2, set2)
oper_count("def ", oper_dict2, set2)

for key in oper_dict1:
    if oper_dict1[key] == 0 and oper_dict2[key] == 0:
        oper_res.append(0)
    elif oper_dict1[key] == oper_dict2[key]:
        oper_res.append(1)
    else:
        oper_res.append(-0.5)


# Вывод результатов

res_q = 0
for elem in oper_res:
    res_q += elem
if res_q > 0:
    print("Количественный критерий вызывает подозрение")
else:
    print("Количественный критерий не вызывает подозрение")
    
    
    
if min(len1, len2) <= (len_inter * 2 - 1):
    print("Критерий построчной проверки вызывает подозрение")
else:
    print("Критерий построчной проверки не вызывает подозрение")