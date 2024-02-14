import random
useraction = input('enter a choice of (rock,paper,scissor):')
possible = ['rock','paper','scissor']
computeraction = random.choice(possible)
print(f'your choice {useraction}')
print(f'computer choice {computeraction}')
if useraction  == computeraction:
    print('its a tie!!')
elif useraction== 'rock':
    if computeraction == 'paper':
        print('computer wins!!\n Better luck next time')
    else:
        print('you won!!')
elif useraction == 'paper':
    if computeraction == 'rock':
        print('you won!!')
    else:
        print('computer wins!!\n Better luck next time')
elif useraction == 'scissor':
    if computeraction == 'rock':
        print('computer wins!!\n Better luck next time')
    else:
        print('you won!!')        
        
                    
    
     