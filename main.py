import re
from re import *



def file_to_set(cur_file, cur_set, cur_array):
    for line in cur_file:
        cur_set.add(line)
        cur_array.append(line)
        


def spaces_delete(cur_set):
    res = set()
    for line in cur_set:
        new_line = sub(" ", "", line)
        res.add(new_line)
    return res


def spaces_delete_arr(cur_arr):
    for i in range(len(cur_arr)):
        cur_arr[i] = sub(" ", "", cur_arr[i])


def oper_count(oper, oper_dict, f_set):
    oper_dict[oper] = 0
    for line in f_set:
        oper_dict[oper] += line.count(oper)
   
    
def tokenize(dictionary, line, sequence, counter):
    pattern = '\.|\,|\=|\>|\<|\+|\-|\/|\*|\^|\&|if|elif|else|def|for|while|in|range|and|or|from|import|is'
    # pattern = '='
    cur_line = re.split(pattern, line)
    for i in range(len(cur_line)):
        if cur_line[i] in dictionary:
            sequence.append(dictionary[cur_line[i]])
        else:
            if counter == 90:
                counter = 96
            counter += 1
            dictionary[cur_line[i]] = chr(counter)
            sequence.append(dictionary[cur_line[i]])
            
    
    
    

# Открытие файла и получение из него данных
filename1 = input()
filename2 = input()
f1 = open(filename1, 'r')
f2 = open(filename2, 'r')
set1 = set()
set2 = set()
arr1 = []
arr2 = []

file_to_set(f1, set1, arr1)
file_to_set(f2, set2, arr2)

# Построковая обработка и сравнение множеств

set_wo1 = spaces_delete(set1)
set_wo2 = spaces_delete(set2)
inter_set = set_wo1 & set_wo2
len1 = len(set_wo1)
len2 = len(set_wo2)
len_inter = len(inter_set)


# Токенизация и сравнение

token_dict_1 = dict()
token_dict_2 = dict()
spaces_delete_arr(arr1)
spaces_delete_arr(arr2)
sequence1 = []
sequence2 = []
counter1 = 0
counter2 = 0
token_res = False
cur_res = 0

for i in range(len(arr1)):
    tokenize(token_dict_1, arr1[i], sequence1, counter1)
for i in range(len(arr2)):
    tokenize(token_dict_2, arr2[i], sequence2, counter2)

max_len = max(len(sequence1), len(sequence2))
min_len = min(len(sequence1), len(sequence2))

if len(sequence1) == len(sequence2):
    token_res = True
elif len(sequence1) > len(sequence2):
    for i in range(max_len - min_len + 1):
        for j in range(min_len):
            if sequence1[j+i] == sequence2[j]:
                cur_res += 1
        if cur_res * 2 + 1 >= min_len:
            token_res = True
        cur_res = 0
else:
    for i in range(max_len - min_len + 1):
        for j in range(min_len):
            if sequence1[j] == sequence2[j+1]:
                cur_res += 1
        if cur_res * 2 > min_len:
            token_res = True
        cur_res = 0
    
    

# Сравнение количественных параметров

oper_dict1 = dict()
oper_dict2 = dict()
oper_res = []

oper_count("+", oper_dict1, set1)
oper_count("-", oper_dict1, set1)
oper_count("=", oper_dict1, set1)
oper_count(">", oper_dict1, set1)
oper_count("<", oper_dict1, set1)
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
oper_count(">", oper_dict2, set2)
oper_count("<", oper_dict2, set2)
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
    
    
if token_res:
    print("Критерий токенизированной проверки вызывает подозрение")
else:
    print("Критерий токенизированной проверки не вызывает подозрение")