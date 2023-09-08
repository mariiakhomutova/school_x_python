N = int(input('Введите число N: '))
new_list = [] 
for i in range(-N, N+1):
    new_list.append(i ** 2)
print ('Вывод: ', new_list)