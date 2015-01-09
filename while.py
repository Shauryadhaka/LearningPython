number=23
running= True
while running:
	guess=int(input('Enter an integer:'))

	if guess == number:
		print('Congratulation, you gussed it')
		running = False
	elif guess < number:
		 print('No, It is a litlle higher than that')
	else:
	  	  print('No, it a litlle lower than that')
else:
	  print('The while loop is over')  # Can have a else statement for a while loop as well which executes as the statement becomes false.
	                                   #It wouldn't run if the lop is exited with the help of a break command.
print('Done')
