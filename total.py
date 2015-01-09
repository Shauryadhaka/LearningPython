def total(intial=5, *numbers, **keywords):
	count = intial
	for number in numbers:
		count += number
	for key in keywords:
	    count += keywords[key]
	return count
print(total(10,1,2,3,vegetables=50,fruits=100))	    	