#new_name: str = input('type name: ')
#greet_message: str  = 'hello bob'
#greet_message: str  = (greet_message[:-3] + new_name)
#greet_message: str = greet_message.replace('bob', new_name)
#print(greet_message)


#river: str = 'mmmmmississippi'
#print('m' + river.lstrip('m')) #удаляет указанные символы слева направо пока не встретит тот символ который не указан
#print('m' + river.strip('m')) #удаляет все указанные символы

#words: str = '-----dsa das das---'
#print(words.strip('-').split())

#import string #импорт всегда в самом начале файла

#numbers: str = string.digits
#word: str = 'hell123o b32ob'
#for number in numbers:
    #word = word.replace(number,'')
#print(word.replace(numbers, ''))

#word: str = 'hell123o b32ob'
#numbers: str = string.digits
#_word: str = ''
#_sum: float = 0.0
#_prod: float = 1.0
#_list: list = []
#_set: set = set ([])
#_dict: dict = {}
#for ch in word:
    #if ch in numbers:
        #continue
    #else:
        #_word += ch
#word = _word
#del _word

#words.casefold, words.upper, words.lower().replace('',''), words.find 

ords: str = 'Hello Bob, are you bob?'
while True:
    bob_index = words.lower().find('bob')
    if bob_index == -1:
        break
else:
    words = ( words [:bob_index] + 'Mary' + words[bob_index + len('bob'):])
    print(words, len('bob'))

_list: list = [1,2,3]
_str: str = '123'
_tuple: tuple = (1, 2, 3)

#3 - 5 

_list[-1] = 5 #can be changed
_str[-1] = 5 #cannot be changed like tuple  
_tuple[1][1] = 5 #can be changed only if incluldes list