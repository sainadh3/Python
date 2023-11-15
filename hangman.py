from random import choice
from hangman_words import word_list

# word_list=['spoon', 'sun', 'camel']
lives=6

choosen_word=choice(word_list)
# print(choosen_word)

guess_1=['_']*(len(choosen_word))
# print(len(choosen_word))


while guess_1.count('_')!=0:

    if lives==0:
        print(f'You Loose. The word is {choosen_word}')
        break
    print(''.join(guess_1))
    guess=input('guess letter in word').lower()
    if guess not in choosen_word:
        lives-=1
        print(f'Your guess letter not in the word. Lives left {lives}')
    elif guess in guess_1:
        print(f'your already guessed this letter. Lives left {lives}')
    for i in range(len(choosen_word)):
        if guess == choosen_word[i]:
            guess_1[i]=guess


if lives!=0 and (guess_1.count('_')==0):
    print('You Win, the word is',end=" ")
    print(''.join(guess_1))