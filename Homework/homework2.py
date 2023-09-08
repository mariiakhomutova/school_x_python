player1, player2 = input('Ввод: ').split(' ')
if (player1 == 'бумага' and player2 == 'бумага') or (player1 == 'ножницы' and player2 == 'ножницы') or (player1 == 'камень' and player2 == 'камень'):
    print('ничья')
elif (player1 == 'бумага' and player2 == 'камень') or (player1 == 'ножницы' and player2 == 'бумага') or (player1 == 'камень' and player2 == 'ножницы'):
    print('игрок 1 выиграл')
else:
    print('игрок 2 выиграл')