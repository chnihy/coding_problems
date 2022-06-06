"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""



while True:
	def romanToInt(s):
		# first make dictionaries containing your conversion tables
		# we will reference these when we create our <for> loop below
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
		# helps us with our <for> loop algorithm below 
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