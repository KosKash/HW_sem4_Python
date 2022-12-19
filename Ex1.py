import random


size = int(input(">>> Введите максимальную степень:  "))
k = {}
for i in range(size+1):
    k[i] = random.randint(0,100)
print(k)
eq = ''
for i in range(size, -1,-1,) :
    if i > 1:
        if k[i] > 1:
            eq += f'{k[i]}x^{i} + '
        elif k[i] == 1:
            eq += f'x^{i} + '
    elif i == 1:
        if k[i] > 1:
            eq += f'{k[i]}x + '
        elif k[i] == 1:
            eq+= f'x + '
    elif i == 0:
        if k[i] > 1:
            eq += f'{k[i]}'
        elif k[i] == 1:
            eq+= f'1'
eq = (eq + " = 0")
print(eq)
with open("Ex_1.txt","w") as data:
    data.writelines(eq)
    data.write("\n")

    

    
   

        
