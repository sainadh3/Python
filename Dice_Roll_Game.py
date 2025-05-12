import random
player_1_score,player_2_score=0,0
for i in range(1,11):
    player_1_roll=random.randint(1,6)
    player_2_roll=random.randint(1,6)
    if (player_1_roll>player_2_roll): player_1_score+=1  
    else: player_2_score+=1
    print(f'Round: {i}\n player_1 score: {player_1_roll}\n player_2 score: {player_2_roll}')
if player_1_score>player_2_score: print(f'Final Winner: player_1 - Rounds won {player_1_score}')  
else: print(f'Final Winner: player_2 - Rounds won {player_2_score}')