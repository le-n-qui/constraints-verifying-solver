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

                indices = []
                # Left hand side variable index
                indices.append(int(items[2][1])) # e.g. take 0 from X0

                # Check if we have right hand side variable
                if items[6].startswith('X'):
                    indices.append(int(items[6][1]))

                for ind in indices:
                    # check whether variable index 
                    # is greater than the size
                    # of nums_in_line
                    if ind < len(nums_in_line) and ind != (len(nums_in_line) - 1):
                        # create domain for variable with this index
                        domains_dict[ind] = list(range(nums_in_line[ind]))
                    else:
                        domains_dict[ind] = list(range(nums_in_line[-1]))

                constraints.append((items[0], items[2], items[4], items[5], items[6]))
        print("Domains Dictionary:")
        print(domains_dict)
        print("Constraints:")
        for c in constraints:
            print(c)


                
                

