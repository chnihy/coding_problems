	"""
		given an int, return a bool stating if int is a palindrome
	"""

	def isPalindrome(x):
		# convert to string, then to list
		x = list(str(x))
		
		# our mid point is half the length of our list 
		# rounding down with floor division
		mid = int((len(x)//2))
		
		# if length of list is odd (using modulo)
		if len(x)%2 != 0:
			# define left/right sides
			# using reverse indexing [::-1]
			left_side = x[:mid]
			right_side = x[-1:mid:-1]
			
		# if number is even
		else:
			# our right side needs to be modified for 
			# even lengthed lists to include the midway index
			# note the reverse indexing and SUBTRACTING from midpoint
			left_side = x[:mid]
			right_side = x[-1:mid-1:-1]
			#print(left_side, right_side)

		# return the result of your comparison
		return left_side == right_side


	test_cases = [1, 11, 111, 1111, 11111, 
				2, 12, 21, 221, 122, 212, 1221,
				123, 12321, 1234321, 11111211111]
	for case in test_cases:
		print("{} : {}".format(str(case), isPalindrome(case)))