import random
import time

operators = ['+', '-', '*', '//']
total_problems = 10


def problem_maker():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 10)
    operator = random.choice(operators)
    expression = f'{first_number} {operator} {second_number}'
    answer = eval(expression)
    return expression, answer


wrong = 0
input('Press enter to start')

start_time = time.time()

for problem in range(total_problems):
    expr, ans = problem_maker()
    while True:
        guess = input(f'{expr} = ')
        if guess == str(ans):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time
print(f'You finished with {wrong} wrong answers in {total_time:.2f} seconds.')