
# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers
for _ in range(1):
	value = randint(1, 50)
	print(value)
attempt=3
while attempt > 0:
    user_input = int(input('Enter Number: '))

    if user_input == value:
        msg = 'You Won!'
        break
    else:
        print(f'Try again! {attempt} attempt left.')
        attempt -= 1
        continue

print(msg)