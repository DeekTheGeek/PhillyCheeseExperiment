filename = 'pi.txt'
new_filename = 'pi_string.txt'

# Open the file
with open(filename) as text_file:
	lines = text_file.readlines()

# Connect the lines into a string		
pi_string = ''
for line in lines:
	pi_string += line.rstrip()

# Creates or updates new txt file:
with open(new_filename, 'a') as new_file:
	new_file.write(pi_string + "/n")

# Ask for the user's birthday
birthday = input("Enter your birthday (mmddyy): ")

# Count appearances of birthday in the string
bdays = str(pi_string.count(birthday))

# Count the number of pi digits
stretch = str(len(pi_string))

# Communicate Results
if birthday in pi_string:
	confirmation_message = ("\nYour birthday appears " + bdays 
		+ " times in these " + stretch + " digits of pi!")
	print(confirmation_message)
	with open(new_filename, 'a') as new_file:
		new_file.write(confirmation_message)
else:
	print("\nYour birthday does not appear in these " 
		+ stretch + " digits of pi...")
