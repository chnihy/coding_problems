while True:
	def romanToInt(s):
		# first make dictionaries containing your conversion tables
		# we will reference these when we create our <for> loop bellow
		romans = {
			'I':1,
			'V':5,
			'X':10,
			'L':50,
			'C':100,
			'D':500,
			'M':1000
		}
		
		# the <romans_sub> dictionary uses clever key/value assignment which 
		# helps us with our <for> loop algorithm bellow 
		romans_sub = {
			'V': 'I',
			'X': 'I',
			'L': 'X',
			'C': 'X',
			'D': 'C',
			'M': 'C'
		}
		
		# we create our variables and assign them empty starting values
		prev_c = ''
		
		# <value> is our final sum to be returned
		value = 0

		"""
		Because roman numeral subs occur on the left side of 
		their partners, it is benneficial to scan our list in reverse order.  
		This is easily done with the reversed() method
		"""
		print("reversed(s): {}".format(list(reversed(s))))
		# we are only printing this list for logging

		# iterate through the reversed list
		for c in reversed(s):
			try:
				# if the currently viewed item has a prev item [item index -1]:
				if romans_sub[prev_c] == c:
				# and that value is equal to any key in the romans_sub dict
					value -= romans[c]
					# subtract the associated value of c
				else:
					# otherwise add value of c
					value += romans[c]
			except:
				# except if the currently viewed item does not have a prev item
				# [item index -1] returns an error
				value += romans[c]
			# assign current value to prev value, continue loop with new c value
			prev_c = c
		
		return value

	rn = input("Enter RN: ")
	romanToInt(str(rn))
'''		for c in reversed(s):
			try:
				if romans_sub[prev_c] == c:
					value -= romans[c]
				else:
					value += romans[c]
			except:
				value += romans[c]

			prev_c = c
		return value
'''