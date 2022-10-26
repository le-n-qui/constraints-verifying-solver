# This is the Constraint 
# Satisfaction Problem class.
# Instance of this class
# will represent the 
# current constraint 
# satisfaction problem.

class CSP:
    def __init__(self, list_of_vars=[], domains={}, constraints=[]):
        # attribute denoting the number of variables in the problem
        self._list_of_vars = list_of_vars
        # attribute denoting the list of domains, each with their 
        # corresponding variable
        self._domains = domains
        # attribute denoting the list of constraints
        # with each contraint being a tuple of 
        # two items: a tuple of variables and 
        # a relation that those variables take on
        self._constraints = constraints
    
    def read_file(self, filename):
        """This method helps process a text file
           containing the syntax for a constraint
           satisfaction problem. It will take
           the relevant information regarding a CSP
           and save them into the CSP class instance. 
        """

        # create a dictionary
        # where key is the variable index
        # and value is the domain (range)
        domains_dict = {}

        # create a list of constraints
        # each contraint is represented 
        # as a tuple of 5 elements 
        # (element can be variable, integer, 
        # comparison operator)
        constraints = []

        # open filename given at the terminal
        with open(filename, 'r') as file:
            # read the first line of the file
            first_line = file.readline()
            # turn string into a list of numbers
            nums_in_line = [ int(x) for x in first_line.strip().split(':') ]
            # Test output
            print("Domain Line")
            print(nums_in_line)
            # read subsequent lines of file
            for line in file:
                # Assumption: every element in the 
                # constraint line is separated
                # by one or more whitespaces
                items = line.split()
                
                # a list of variable indices
                indices = []
                # Left hand side variable index 
                # (first encountered variable)
                # below code takes 0 from X0 and add it to list
                indices.append(int(items[2][1])) 

                # Check if we have a right hand side variable
                if items[6].startswith('X'):
                    indices.append(int(items[6][1]))

                # loop through the list of indices
                for ind in indices:
                    # check whether variable index 
                    # is greater than the size
                    # of nums_in_line
                    if ind < len(nums_in_line) and ind != (len(nums_in_line) - 1):
                        # create domain for variable with this index
                        domains_dict[ind] = list(range(nums_in_line[ind]))
                    else:
                        domains_dict[ind] = list(range(nums_in_line[-1]))
                # create a tuple for a constraint and save it into the list
                constraints.append((items[0], items[2], items[4], items[5], items[6]))
        
        # Update CSP instance attributes
        self._list_of_vars = sorted(domains_dict.keys())
        self._domains = domains_dict
        self._constraints = constraints

        # Test output
        print("Variables (Taken from Domains Dictionary)")
        print(sorted(domains_dict.keys()))
        print("Domains Dictionary:")
        print(domains_dict)
        print("Constraints:")
        for c in constraints:
            print(c)


                
                

