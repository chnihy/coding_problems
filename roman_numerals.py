"""
Given a roman numeral, convert it to an integer.
"""

def romanToInt(s):
	# make dictionaries containing our conversion tables
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
	# helps us with our <for> loop 
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

	# our for loop iterates through the reversed list
	for c in reversed(s):
		# if the currently viewed item (c) has a prev item (prev_c) aka [(index of c)-1]:
		try:
			# and that value is equal to any key in the romans_sub dict
			if romans_sub[prev_c] == c:
				# we subtract the associated value of c from our final result 
				value -= romans[c]
			else:
				# otherwise we add value of c
				value += romans[c]
		except:
			# except if the currently viewed item does not have a prev item
			# aka if [c index -1] returns an error
			value += romans[c]
		
		# before we start again, we assign current value to prev value, 
		# then continue our loop with new c value
		prev_c = c
	
	return value
