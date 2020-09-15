#create an infinite loop that takes input from user. If name is in ACCEPTED_NAMES, print name. Otherwise prompt to enter valid name. If user chooses to exit, print See Ya!
ACCEPTED_NAMES = ['bob', 'larry', 'george', 'anna']

def check_name():
	while True:
		name = input("Please enter a name or exit: ").lower()
		if name == 'exit':
			print('See Ya!')
			break
		if name not in ACCEPTED_NAMES:
			print('Enter valid name.')
			continue
		print(name)
