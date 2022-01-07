''' This function will create random color '''

import string 
import random

def genColor():
	letters = "ABCDEF"
	digits = string.digits

	color = "#"
	for i in range(0,6):
		color += random.choice(letters+digits)
	
	return color
		
