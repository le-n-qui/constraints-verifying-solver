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

	def read_file(self):
		pass