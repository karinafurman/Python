print('1 - GUN, 2 - Lightning, 3 - Devil, 4 - Dragon, 5 - Water, 6 - Air, 7 - Paper, 8 - Sponge, 9 - Wolf, 10 - Tree, 11 - Human, 12 - Snake, 13 - Scissors, 14 - Fire, 15 - Rock')

player_1 = int(input('Make your choice from 1 to 15: '))
player_2 = int(input('Make your choice from 1 to 15: '))

if (player_1 <= 0 or player_1 > 15) or (player_2 <= 0 or player_2 > 15):
    print('Один из вас ввел неверное число. Введите от 1 до 15')

elif player_1 == player_2:
    print('Заново!')


elif player_1 == 1 and (player_2 <= 15 and player_2 >= 9): 
    print('Player 1 are win!')

elif player_1 >= 2 and player_1 <= 6 and ((player_2 <= player_1 - 1) or (player_2 <= 15 and player_2 >= player_1 + 8)): 
    print('Player 1 are win!')
    
elif player_1 == 7 and ((player_2 <= 6 and player_2 >= 1) or (player_2 == 6)): 
    print('Player 1 are win!')

elif player_1 >= 8 and player_1 <= 15 and (player_2 <= player_1 - 1 and player_2 >= player_1 - 7): 
    print('Player 1 are win!')

else:
    print('Player 2 are win!')
    
    