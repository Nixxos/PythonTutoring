# @author - zac_j_harris

import logging  # Not necessary - used to showcase logging functionality

from random import randint, random

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger("Main")



def main():
	user_in = input("Please input a roll in the form NdM:\t")
	roll_sum = 0
	try:
		str_n = user_in.split("d")
		nums = [int(n) for n in str_n]
		logger.debug(nums)
		if len(nums) != 2:
			print("Error. Incorrect Input")
			return
		for i in range(nums[0]):
			roll_sum += randint(0, nums[1])
		print('The sum of your rolls is %s' % roll_sum)
	except Exception as e:
		logging.critical(e)
		print("Error. Incorrect Input")




if __name__ == "__main__":
	main()