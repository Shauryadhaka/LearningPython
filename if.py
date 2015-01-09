number =23
guess = int(input('Enter an integer:'))
if guess==number:
	print('Congratulations, you gussed it') #new block starts here
	print('but you do not win any prizes!') #new block ends here
elif guess<number:
    print('No, it is a little higher than that')
    # you can do whatever you want in this block....
else:
  print('No, it is a little lower that that')

print('Done')
      	