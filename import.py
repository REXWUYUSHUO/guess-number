import random

r = random.randint(1, 100)
while True:
    num = input('請猜數字:')
    num = int(num)
    if num == r:
        print('you got the point')
        break
    elif num > r:
        print('比答案大要猜小一點')
    elif num < r:
        print('比答案小要大一點')

