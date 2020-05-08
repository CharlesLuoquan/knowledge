# print('luoquan111')
# name = input('what is your name? ')
# color = input('what is your favourite color? ')
# print(name + " likes " + color)
# a = 'luo'
# b = 'quan'
# msg = f'{a}'
# print(msg)

# count = 1
# target = 8
# while count <= 3:
#     guess = int(input('Guess: '))
#     count += 1
#     if guess == target:
#         print('You won!')
#         break
# else:
#     print('sorry you fail')

secret = ''
started = False
while True:
    secret = input('> ').lower()
    if secret == 'help':
        print(
'''
start - to start the car
stop - to stop the car
quit - to exit''')
    elif secret == 'start':
        if started:
            print("cat is already started!!!")
        else:
            started = True
            print('start the car')
    elif secret == 'stop':
        if not started:
            print("car is already stopped!!!")
        else:
            started = False
            print('stop the car')
    elif secret == 'quit':
        break
    else:
        print('i do not understand!')


