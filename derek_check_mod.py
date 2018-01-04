def derek_check():
	'''This requests a first name and rejects the first name derek'''
	d = 0
	derek = True
	while derek:
		name = input('\nWhat is your first name? ')
		if name.lower() == 'derek':
			d += 1
			if d <= 2:
				print("\nFuck you, Derek! Buzz off.")					
			if d > 2:
				print('\nSeriously... Fuck off!')
				sys.exit()
		else:
			print("\nThank God... You're not Derek.")
			return name
			derek = False
