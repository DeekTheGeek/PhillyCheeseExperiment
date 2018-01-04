from query_yes_no_mod import query_yes_no as qyn
from derek_check_mod import derek_check as dc
# importing with an asterisk imports all the classes importing 
# individual classes instead of the entire module skips the need for the
# module name in the code (e.g. class_pet.Dog vs. Dog).
from class_pet import *

dogs = []
cats = []

add = True
while add:
	answer = qyn('\nDo you want to add another pet? ', None)
	if answer == 'yes':
		pet = True
		while pet:
			species = input('\nDo you own a dog or cat? ')
			if species.lower() != 'dog' and species.lower() != 'cat':
				print('\nWe only accept dogs or cats at this time ')
			if species.lower() == 'dog':
				dog = {}
				dog['owner'] = dc()
				dog['name'] = input("\nWhat is your dog's name? ")
				dog['breed'] = input("\nWhat is your dog's breed? ")
				dog['age'] = input("\nWhat is your dog's age? ")
				dog = Dog(dog['name'], dog['age'], 
					dog['owner'], dog['breed'])
				dogs.append(dog)
				pet = False
			if species.lower() == 'cat':
				cat = {}
				cat['owner'] = dc()
				cat['name'] = input("\nWhat is your cat's name? ")
				cat['breed'] = input("\nWhat is your cat's breed? ")
				cat['age'] = input("\nWhat is your cat's age? ")
				cat = Cat(cat['name'], cat['age'], 
					cat['owner'], cat['breed'])
				cats.append(cat)
				pet = False
	if answer == 'no':
		add = False

for cat in cats:
	print(cat.__str__())
	cat.warning()

for dog in dogs:
	if dog.name.lower() == 'sheldon':
		dog.untrained()

for dog in dogs:
	print(dog.__str__())
	if dog.trained == False: 
		print(dog.warning())
	
for dog in dogs:
	r = True
	while r:
		answer = qyn('\nDo you want to play with ' + dog.name.title()
			+ '?', None)
		if answer == 'yes':
			dog.ready()
			sit = qyn('\nDo you want ' + dog.name.title() + ' to sit?',
				None)
			if sit == 'yes':
					dog.sit()
			if sit == 'no':
				roll = qyn('\nDo you want ' + dog.name.title()
					+ ' to roll over?', None)
				if roll == 'yes':
					dog.roll_over()
		if answer == 'no':
			dog.sleep()
			r = False
