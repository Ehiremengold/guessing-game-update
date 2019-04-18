
#Declaring variables
name = input('Enter your name:')
guess = int()
guessnumber = 2
max_tries = 3
tries = 0
out_of_guess = False

welcome = print('Well, hello ' + name + ', I\'m q-bot')

question = input('I\'m thinking of a number. Do you want to guess what it is(y/n)?')
#questionnaire
if question == 'n':
    print('oh..okay')
elif question == 'y':
    print('Great!')
else:
    print('Invalid input, i guess you want to play!')
### As long as user's input is wrong the question is to continue
while guessnumber != guess and not out_of_guess:
     if tries < max_tries:
         guess = int(input('Guess the number:'))
         if guess > guessnumber:
             print('You are a little bit way off, guess a lower number')
         elif guess < guessnumber:
             print('You are a little bit way off, guess a higher number')
         tries += 1
     else:
         out_of_guess = True

if out_of_guess == True:
    print('Out of guess , You Lose!!!')
else:
    print('Correct, You win!')

