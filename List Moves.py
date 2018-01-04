#imports an entire module
import query_yes_no_mod

#imports a function from a module
from derek_check_mod import derek_check

usernumb = 0

confirmed_users = []
denied_users = []
denied_dogs = []
unconfirmed_users = []


#asks for a user name and species and does a Derek check
more = True
while more:
	answer = query_yes_no_mod.query_yes_no(
		'\nDo you want to add a user? ', None)
	if answer == 'yes':
		tron = {}
		usernumb = usernumb + 1
		tron['userid'] = usernumb
		tron['name'] = derek_check()
		species = input('\nWhat is your species? ')
		tron['species'] = species
		unconfirmed_users.append(tron)
	if answer == 'no':
		more = False

# Prints the list of unconfirmed_users
if unconfirmed_users:
	print('\nUnconfirmed Users:')
	for user in unconfirmed_users:
		print('\n' + str(user))

# Allows the user to confirm or deny unconfirmed_users
p = 0
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	# denies all users of the species dog automatically
	if current_user['species'] == 'dog':
			denied_dogs.append(current_user)
			p += 1
	else: 
		answer = query_yes_no_mod.query_yes_no('\nConfirm '
			+ current_user['name'].title() + '?')
		if answer == 'yes':
			confirmed_users.append(current_user)
			print('\n' + current_user['name'].title() + ' confirmed')
		if answer == 'no':
			denied_users.append(current_user)
			print('\n' + current_user['name'].title() + ' denied')

#prints the results of the entries and their confirmation or denial
			
print('\nNo additional users to confirm. Your final list is below.')

if confirmed_users:
	print('\nConfirmed Users:')
	for user in confirmed_users:
		print('\n' + user['name'].title())
		
if denied_dogs:
	print('\n' + str(p) + ' dogs denied:')
	for user in denied_dogs:
		print('\n' + user['name'].title())
		
if denied_users:
	print('\nDenied Users:')
	for user in denied_users:
		print('\n' + user['name'].title())
