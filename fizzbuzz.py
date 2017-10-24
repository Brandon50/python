for n in range (1,101):
	if n%3 == 0 and n%5 != 0:
		print("FIZZ")
	if n%5 == 0 and n%3 != 0:
		print("BUZZ")
	if n%3 == 0 and n%5 == 0:
		print ("FIZZBUZZ")
	if n%3 != 0 and n%5 != 0:
		print (n)
