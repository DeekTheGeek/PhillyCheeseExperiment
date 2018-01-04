# This is a test script for Derek LeBlond to learn Python.
from datetime import *

# using as renames a module of function with the program
from query_yes_no_mod import query_yes_no as qy

# writing cheats
carriage_return = "\n"
tab = "\t"
br = "\n\n=========================================================\n\n"

# date quick math brrrra
timedelta = (date.today() - date(2017,12,3))
delta2 = timedelta.days

# Variables
author = "sukrat"
date1 = str(timedelta.days)
date2 = "help!"

# Condition1
if delta2 > 1 and delta2 < 30:
	skill = "novice"
elif delta2 > 30:
	skill = "expert"
elif delta2 < 1:
	skill = "newb"

# Condition2		
if skill == "novice" or skill == "expert":
	skill = date1 + " days."
else:
	skill = date1 + " day."

# Condition3
if skill != date1:
	surprise = "sURPRISE!"
else:
	surprise = "YOU FAIL!"

# Input Name using a while loop to keep out Derek.
# Used break instead of setting punk as false for practice.
punk = True
nomme = "Please enter your name: "
p = 0
while punk:
	name = input(nomme)
	if name.lower() == 'derek':
		if p <= 2:
			print("Fuck you, Derek!")
			p += 1
		if p > 2:
			print('Seriously. Fuck off!')
			sys.exit()
	else:
		print("Thank God... You're not Derek.")
		break

# messaging
message = "\nHello " + name.title() + "!"
message = message + carriage_return*2 
statement = ("I am learning Python. I have been learning Python for "
    + skill + carriage_return*2)
quote =('"Python is great!"' + carriage_return + tab*2 + "-"
	+ author.title() + br)

# list fun
string_list = list(range(1,4))
origlist = list(string_list)
string_list.insert(2, statement)
string_list.insert(1, 'me 2')
string_list.append(surprise.lower())
testlist1 = list(string_list)
del string_list[4]
string_list.remove('me 2')
popped_list = string_list.pop()
finallist = list(string_list)
emptylist = []

# final message
hello_world=message.upper() + str(string_list[-1]) + quote

#prompt for list disclosure
answer = qy(name.title() + ", do you want to only see the "
	"message?")

# pc loadletter
print (hello_world)

#Input Condition
if answer == "no":
		print(str(timedelta) + br)

		# If as an error (that will always fail)
		if popped_list != "sURPRISE!":
			print("Popped List Error: " + popped_list + br)

		# Using if to different things based on a list being empty or 
		# full, as well as compare lists and change what is printed
		if emptylist:
			print("What about this list?")
			for origlistitem in origlist:
				if origlistitem < 3:
					print (origlistitem)
				else:
					print ("Trips be-otch!")
		else:
			for origlistitem in origlist:
				if origlistitem in finallist:
					if origlistitem < 3:
						print ("In final list")
					else:
						print ("Trips be-otch!")
				else:
					print (origlistitem)
		print (br)

		# Using For to Print a Line Item List
		for finallistitem in finallist:
			print (finallistitem)
		print (br)
		for testlist1item in testlist1:
			print (testlist1item)
		print (br)
		for testlist2item in reversed(testlist1):
			print (testlist2item)
		print (br)
