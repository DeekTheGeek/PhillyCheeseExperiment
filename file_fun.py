# opens the document and prints the content with the right white space
# removed
with open('pi.txt') as text_file:
	contents = text_file.read()
	print(contents.rstrip())

#opens the document and stores the lines in memory using a variable name
with open('pi.txt') as text_file:
	lines = text_file.readlines()

#prints the lines stored from above and removes the right white space
for line in lines:
	print(line.rstrip())

#merges all the lines into a single line
pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print (pi_string)

# truncates the string to show only the first 13 characters
print ("\n" + pi_string[:13] + '...')

#  counts the character length
print ("\n" + str(len(pi_string)))
