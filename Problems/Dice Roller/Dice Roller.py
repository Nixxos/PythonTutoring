# @author - zac_j_harris

import logging  # Not necessary - used to showcase logging functionality

from random import randint, random

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger("Main")



def main():
	# Get user input using the input() function - takes a string as inputs (usually a prompt for the user to type something in)
	user_in = input("Please input a roll in the form NdM:\t")

	# The sum of our rolls that we will print out
	roll_sum = 0

	# This will take a string like "6d4" and return a list like ["6", "4"]. It uses the "d" we typed in for 6d4 as the delimeter, which is something that is used to divide the text.
	# Another example of the str.split() function might be something like "a,b,c,d" as the string, string.split(",") as the function, and the output would be ["a", "b", "c", "d"]. It separated the string by the delimeter.
	str_n = user_in.split("d")

	# Turning our list of strings into a list of integers
	nums = [int(n) for n in str_n]

	# logging the list of numbers to the console
	logger.debug(nums)

	# Repeat N times, N being the first number in NdM, and also stored in nums[0]
	for i in range(nums[0]):

		# Add a random number from 1 to M to the sum of the rolls
		roll_sum += randint(1, nums[1])

	# Finally, print out the sum of the rolls
	print('The sum of your rolls is %s' % roll_sum)




if __name__ == "__main__":
	main()