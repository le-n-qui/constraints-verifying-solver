# This is the Constraint 
# Satisfaction Problem class.
# Instance of this class
# will represent the 
# current constraint 
# satisfaction problem.

class CSP:
	def __init__(self, number_of_var=0, domains=[], constraints=[]):
		# attribute denoting the number of variables in the problem
		self.num_var = number_of_var
		# attribute denoting the list of domains, each with their 
		# corresponding variable
		self.domains = domains
		# attribute denoting the list of constraints
		# with each contraint being a tuple of 
		# two items: a tuple of variables and 
		# a relation that those variables take on
		self.constraints = constraints

	def read_file(self, filename):
		# open filename given at the terminal
		with open(filename, 'r') as file:
			# read the first line of the file
			first_line = file.readline()
			# turn string into a list of numbers
			nums_in_line = [ int(x) for x in first_line.strip().split(':') ]
			print(nums_in_line)
		    # read subsequent lines of file
			for line in file:
				print(line)

