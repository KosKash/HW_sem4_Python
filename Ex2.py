import random
# Надеюсь вы прочитайте это: к сожалению из-за работы не получается успевать все, но я стараюсь ;)

def eq(size: int, name: str):

    k = {}
    for i in range(size+1):
        k[i] = random.randint(0, 100)
    
    eq = ''
    for i in range(size, -1, -1,):
        if i > 1:
            if k[i] > 1:
                eq += f'{k[i]}x^{i} + '
            elif k[i] == 1:
                eq += f'x^{i} + '
        elif i == 1:
            if k[i] > 1:
                eq += f'{k[i]}x + '
            elif k[i] == 1:
                eq += f'x + '
        elif i == 0:
            if k[i] > 1:
                eq += f'{k[i]}'
            elif k[i] == 1:
                eq += f'1'
    eq = (eq + " = 0")
    
    with open(f"{name}.txt", "w") as data:
        data.writelines(eq)

def to_dict(eq: str) -> dict:
    eq = eq.replace(' ', '')
    eq = eq[:-2]
    eq = eq + ' x^0'
    eq_list = eq.split('+')
    for i in range(len(eq_list)):
        eq_list[i] = eq_list[i].replace('x^', ':')
        eq_list[i] = eq_list[i].replace('x', ':1')
        
    for i in range(len(eq_list)):
        eq_list[i] = eq_list[i].split(':')
    
    keys = []
    values = []
    for i in range(len(eq_list)):
        values.append(int(eq_list[i][0]))
        keys.append(int(eq_list[i][1]))
    keys = keys[::-1]
    values = values[::-1]
    eq_dict = dict(zip(keys, values))
    return eq_dict

def sad(dic:dict) ->dict:
    keymax = 0
    for k,v in dic.items():
        if k > keymax:
            keymax = k
    key_list = []
    for k in dic.keys():
        key_list.append(k)
    for i in range(keymax):
        if i not in key_list:
            dic[i] = 0
    sorted(dic.items())
    sort_dic = dict(sorted(dic.items()))
    return sort_dic

def summ(dict1: dict, dict2: dict) -> dict:
    if len(dict1) > len(dict2):
        for i in range(len(dict1)):
            dict1[i] > dict1[i] + dict2[i]
        return dict1
    else:
        for i in range(len(dict2)):
            dict2[i] = dict2[i] + dict1[i]
        return dict2

def to_eq_out(k: dict) -> str:
    eq = ''
    for i in range(len(k) - 1, -1, -1,):
        if i > 1:
            if k[i] > 1:
                eq += f'{k[i]}x^{i} + '
            elif k[i] == 1:
                eq += f'x^{i} + '
        elif i == 1:
            if k[i] > 1:
                eq += f'{k[i]}x + '
            elif k[i] == 1:
                eq += f'x + '
        elif i == 0:
            if k[i] > 1:
                eq += f'{k[i]}'
            elif k[i] == 1:
                eq += f'1'
    eq = (eq + " = 0")
    return (eq)

def init():
    print("Какой режим вы хотите использовать? \n1. Авто \n2. Тест")
    value = input('>>> ')
    match value:
            case '1':
                eq(9,1)
                eq(9,2)
                with open('1.txt', 'r') as data:
                    for line in data:
                        eq1 = line
                with open('2.txt', 'r') as data:
                    for line in data:
                        eq2 = line
                print(f'{eq1} первое уравнение \n{eq2} второе уравнение')
                result = to_eq_out(summ(sad(to_dict(eq1)),(sad(to_dict(eq2)))))
                print(f'Сумма равна - {result}')
                with open(f"result_auto.txt", "w") as data:
                    data.writelines(result)
           
                
            case '2':
                with open("test1.txt", "w") as data:
                    data.writelines('82x^9 + 52x^7 + 97x^6 + 15 = 0')
                with open('test2.txt','w') as data:
                    data.writelines('82x^9 + 52x^7  = 0')
                with open('test1.txt', 'r') as data:
                    for line in data:
                        eq1 = line
                with open('test2.txt', 'r') as data:
                    for line in data:
                        eq2 = line
            
                result = to_eq_out(summ(sad(to_dict(eq1)),(sad(to_dict(eq2)))))
                test_res = "164x^9 + 104x^7 + 97x^6 + 15 = 0"
                
                if test_res == result:
                    print("Status: OK")
                else:
                    print('Check')
            case __:  
                print('Incorrect')  

init()    

    



