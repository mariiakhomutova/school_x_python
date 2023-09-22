a : list[int] = [1, 2, 3, 3, 5]
b: list[int] = [0, 0, 1, 0, 1]

def mask_list(array: list[int], mask: list[int]) -> list[int]:
    return [val * mask[i] * .5 for i, val in enumerate(array)]

def test_mask_list():
    print('проверяем')
    assert mask_list([1, 2, 3], [0, 1, 0]) == [0, 2, 0], 'маска работает неправильно' #использровать ассерт только в тестах

answer= [val * b[i] for i, val in enumerate(a)] #firstvariant
    print(answer)



for i in a:
    answer.append(i*2) #secondvariant

for i, val in enumerate(a):
    print(f'index = {i}')
    print(f'value = {val}\n')