def elements(x: list) -> str | int | list:
    numbers = []
    for i in range(1, len(x)):
        if x[i] - x[i-1] > 1:
            numbers.append(i)
    if len(numbers) == 0:
        return "Не найдено"
    elif len(numbers) == 1:
        return numbers[0]
    else:
        return numbers


user = input('Введите числа: ').split(" ")
user_narr = []
for e in user:
    user_narr.append(int(e))

answer = elements(user_narr)
print('Ответ: ', answer)