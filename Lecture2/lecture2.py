#snake_case
#i: int = 0
#f: float = .0
#s: str = 'sdads'
#b: bool = True
#n: None = None
#_list: list = [1,3,23,45,0,None,'sad',False]
#_set: set = {i,f,s,b,n}

#for n in numbers:
    #if n % 2 == 0:
        #print(f'Число -  {n} четное')
    #else:
        #print(f'Число -  {n} не четное')
#for n in numbers:
    #if n % 3 == 0 and n % 5 == 0: #большая команда идет сначала 
        #print(f'Число -  {n} делится на 3 и на 5')
    #elif n % 3 == 0:
        #print(f'Число -  {n} делится на 3')
    #elif n % 5 == 0:
        #print(f'Число -  {n} делится на 5')
    #else:
        #print(f'Число -  {n} не делится на 3 и на 5')

#word: str = input('Введите слово: ')
#vowel: str = 'aeiouy'
#vowel_count: int = 0
#for c in word:
    #if c in vowel:
        #vowel_count += 1
#print (vowel_count)

#N = int(input('N: ')) #если пересечения включены
#sum = 0
#for i in range(N+1):
    #if i % 3 == 0 or i % 5 == 0:
      #sum = sum + i
#print(sum)

n: int = int(input('N: '))

while n > 0:
    print(n)
    n = n - 1 