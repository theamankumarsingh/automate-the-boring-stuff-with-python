import random,logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
guess = ''
coin=['tails','heads']
logging.debug(guess)
while guess not in coin:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug(guess)
toss = coin[random.randint(0, 1)] # 0 is tails, 1 is heads
logging.debug(toss)
logging.debug(guess)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug(guess)
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')