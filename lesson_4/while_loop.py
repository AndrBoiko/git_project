counter = 0

while counter <= 10:
    print(counter)
    counter += 1

while True:
    message = input('>>> ')
    if message.lower() == 'exit':
        break
    print(f'{message.upper()}')
else:
    print('Wjile loop is ended')