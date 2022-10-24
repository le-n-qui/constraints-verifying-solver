# Constraint Satisfaction Problem solver

# Import libraries
import sys


# Main method
# is invoked
# when the script 
# is executed 
# on the command
# line terminal
def main():
	# extract a list of arguments to the program
	args = sys.argv[1:] 
	# if the list is empty
	if not args:
		# display helpful information
		print("usage: file [use_forward_check_flag]")
		print("warning: need a text file containing")
		print("\t a constraint satisfaction problem")
		print("\t using the specified syntax.")
		print("optional: provide 0 or 1 for forward check flag;")
		print("\t default value is 0.")
		# exit the program
		sys.exit(1)

	# create variable for forward check
	# its value will either be 1 (Yes) or 0 (No)
	forward_check_flag = None

	# if more than 2 arguments are provided
	if len(args) > 2:
		# take the first 2 arguments
		args = args[:2]

	# if argument list size is exactly 2
	if len(args) == 2:
		# convert string literal into integer
		bool_val = int(args[1])
		# verify that user input the correct value
		if bool_val not in [0, 1]:
			print("usage: file [use_forward_check_flag]")
			print("warning: forward check flag must be 0 or 1.")
			sys.exit(1)
		# if so, assign it to forward check flag variable
		forward_check_flag = bool_val
	else: # if no value is provided for forward check flag
		# a default of zero is assigned
		forward_check_flag = 0

	print("Forward Check Flag: ", forward_check_flag)

# Run the script
if __name__ == "__main__":
	main()
