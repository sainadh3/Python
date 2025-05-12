'''
Serious of Steps to be followed:

The prediction() function should predict 0 or 1 as output by comparing the values stored in the count_zero and count_one variables.

If count_zero > count_one, the function should return 0.

Else if count_one > count_zero, the function should return 1.

Else if count_zero == count_one, the function should return 0 or 1 randomly.


The update_counts() function should update the values stored in the count_zero and count_one variables based on the player inputs.

If the player_input == 0, the count_zero value should increase by 1.

Else if the player_input == 1, the count_one value should increase by 1.

The update_counts() function should not return anything. It should just update the values stored in the count_zero and count_one variables.

Now we are going to modify the count_zero and count_one variables using the update_counts() function. But, count_zero and count_one are global variables.

The update_scores() function should take the predicted and player_input values as inputs and should update the player_scores and the computer_scores by comparing the predicted value with the player_input value.

If the predicted value is the same as the player_input value, increase the computer_score by 1.

Else, increase the player_score by 1.

The predicted value is obtained from the prediction() function. Immediately after updating the scores, the update_scores() function must print the updated values stored in the player_score and computer_score variables.


In game_play function, you have to code a few of the functional requirements. They are as follows:

Get the predicted value using the prediction() function and store it in the predicted variable.

Take input from a player using the input() function and store it in the player_input variable. Print "Enter either 0 or 1: " while taking the input.

Convert the player_input value to an integer value.

Update the values stored in the count_zero and count_one variables using the update_counts() function.

Update the values stored in the player_score and computer_score variables using the update_scores() function.

'''


import random
computer_score,player_score=0,0
count_zero,count_one=0,0


def prediction():
    global count_zero,count_one
    if count_zero>count_one:
        predict= 0
    elif count_one>count_zero:
        predict =1
    else:
        predict= random.randint(0,1)
    return predict
def update_counts(player_input):
    global count_zero,count_one
    if player_input==0:
        count_zero+=1
    else:
        count_one+=1
def update_score(predicted,player_input):
    global computer_score,player_score
    if (predicted==player_input):
        computer_score+=1
        print('computer score is %s'%computer_score)
        print('player score is %s'%player_score)
    else:-
        player_score+=1
        print('player score is %s'%player_score)
        print('computer score is %s'%computer_score)
def game_play():
    while True:
        player_input=int(input('Enter number either 0 or 1:'))
        valid_entries=[0,1]
        if player_input not in valid_entries:
            print('You enetered wrong input')
            player_input=int(input('Enter number either 0 or 1:'))
        update_counts(player_input)
        predicted=prediction()
        update_score(predicted,player_input)
        if computer_score==10:
            print('Computer wins, you loose')
            break
        if player_score==10:
            print('Player wins, computer loose')
            break

game_play()
    