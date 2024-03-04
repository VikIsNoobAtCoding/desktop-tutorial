# office assistant

print('Hello there!')

name = input('What is your name? \n')

if name == 'Simeon':
    print('Please get out')
    exit()
else:
 order = input(f'Hello {name}! Nice to meet you today.\n'
              'What kind of help do you want?\n'
              'With emails, word files or excel files. \n')

order_price = 5

client_wish = float(input(f'Oh, so you want help with {order}.\n '
                          f'And how many {order} do you want help with?\n'))

print(f'Okay that will cost you {client_wish*order_price}\n'
      f"Sounds good {name}. You will have your " + str(client_wish) + f" {order} ready to go.")

