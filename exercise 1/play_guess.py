import random

num = random.randint(1, 20)
wrong_ans = 0
print(num)
for i in range(5):
    guess_num = int(input('Guess the number'))
    if guess_num == num:
        print('you win')
        break
    else:
        wrong_ans += 1
if wrong_ans == 5:
    print('Game over', ' \n', 'right answer is :', num)
