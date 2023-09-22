from typing import TypeAlias
IntOrNoneType = int | None
ComplicatedDict: TypeAlias = dict[int | str | None]
alphabet: dict[int|str|None|float, str|int|float|dict[int, str|int|dict[int|str]]] {1: 'A', 2: 'B', 3: set([1,2,3,4,3]), 4: {1: 'A', 2: 3}, 'Z': 10, 0.1:'SHA', True: 'sdas', False: 14325, None: 'dassfaf', [1,2]: 3, } #hashfunc отсутствует у списка
class A:
    def __init__(self, **kwargs):
        for key, value in kwargs:
            self.key = value
O_letter = alphabet.get('Z',None)
if not bool(O_letter):
    print('NO O')
#print(alphabet.get(4))

for pair #key, value in alphabet: #.keys, values, items
    #if value in 'AY':
    print(pair)