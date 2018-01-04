#Uses continue to skip the print of those quick maths where the modulo
#operator (%), which produces just the remainder of the divided numbers,
#is 0 (i.e. no remainders, and completely divisible (e.g. 2/2)).

num = 0
while num < 10:
	num += 1
	if num % 2 == 0:
		continue

	print(num)
