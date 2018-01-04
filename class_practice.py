import class_pet
from query_yes_no_mod import query_yes_no as qyn

boo = class_pet.Dog('sheldon', 8, 'ellen', 'bichon')
boo2 = class_pet.Dog('cuddles', 9, 'jen', 'shitzu')

print(boo.owner.title() + "'s dog's name is " + boo.name.title() + ".")
print("\n" + boo.name.title() + " is " + str(boo.age) + ".")

print("\n" + boo2.owner.title() + "'s dog's name is " 
	+ boo2.name.title() + ".")
print("\n" + boo2.name.title() + " is " + str(boo2.age) + ".")

r = True
while r:
	answer = qyn('\nDo you want to play with ' + boo.name.title() + '?',
		None)
	if answer == 'yes':
		boo.ready()
		sit = qyn('\nDo you want ' + boo.name.title() + ' to sit?',
			None)
		if sit == 'yes':
				boo.sit()
		if sit == 'no':
			roll = qyn('\nDo you want ' + boo.name.title()
				+ ' to roll over?', None)
			if roll == 'yes':
				boo.roll_over()
	if answer == 'no':
		boo.sleep()
		r = False
c = True
while c:
	answer = qyn('\nDo you want to play with ' + boo2.name.title() + '?',
		None)
	if answer == 'yes':
		boo2.ready()
		sit = qyn('\nDo you want ' + boo2.name.title() + ' to sit?',
			None)
		if sit == 'yes':
				boo2.sit()
		if sit == 'no':
			roll = qyn('\nDo you want ' + boo2.name.title()
				+ ' to roll over?', None)
			if roll == 'yes':
				boo2.roll_over()
	if answer == 'no':
		boo2.sleep()
		c = False
