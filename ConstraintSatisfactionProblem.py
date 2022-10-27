# This is the Constraint 
# Satisfaction Problem class.
# Instance of this class
# will represent the 
# current constraint 
# satisfaction problem.

class CSP:
    def __init__(self, list_of_vars=[], domains={}, constraints={}):
        """This method is invoked when creating
           an instance of the class. Its parameters
           take on default values if not given. 
        """

        # attribute denoting the number of variables in the problem
        self._list_of_vars = list_of_vars
        # attribute denoting the list of domains, each with their 
        # corresponding variable
        self._domains = domains
        # attribute denoting the list of constraints
        # with each contraint being a tuple of 
        # five items: integer, variable, integer
        # comparison operator, integer/variable
        self._constraints = constraints
    
    @property
    def list_of_vars(self):
        return self._list_of_vars
    
    @property
    def domains(self):
        return self._domains
    
    @property
    def constraints(self):
        return self._constraints
    
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
        constraints = {}

        # open filename given at the terminal
        with open(filename, 'r') as file:
            # read the first line of the file
            first_line = file.readline()
            # turn string into a list of numbers
            nums_in_line = [ int(x) for x in first_line.strip().split(':') ]
            
            # read subsequent lines of file
            for line in file:
                # Assumption: every element in the 
                # constraint line is separated
                # by one or more whitespaces
                items = line.split()
                
                # keep relevant elements in a constraint 
                elements = (items[0], items[2], items[4], items[5], items[6])

                # a list of variable indices
                indices = []

                # Left hand side variable index 
                # (first encountered variable)
                # below code takes 0 from X0 
                var1_index = int(items[2][1])

                # save index of variable 1 
                indices.append(var1_index) 

                # Check if we have a right hand side variable
                if items[6].startswith('X'):
                    var2_index = int(items[6][1])
                    # save index of variable 2 
                    indices.append(var2_index)
                    # get constraints of which var1 and var2 are a part
                    if not constraints.get((var1_index, var2_index), None): 
                        constraints[(var1_index, var2_index)] = []
                        constraints[(var1_index, var2_index)].append(self.get_relation(var1_index, elements, var2_index))
                    else:
                        constraints[(var1_index, var2_index)].append(self.get_relation(var1_index, elements, var2_index))
                else: # an integer is found instead
                    # add constraint for this variable 
                    if not constraints.get(var1_index, None):
                        constraints[var1_index] = []
                        constraints[var1_index].append(self.get_relation(var1_index, elements))
                    else:
                        constraints[var1_index].append(self.get_relation(var1_index, elements))
                    
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
                
        # Update CSP instance attributes
        self._list_of_vars = sorted(domains_dict.keys())
        self._domains = domains_dict
        self._constraints = constraints

    def get_relation(self, i, constraint_info, j=None):
        """This method returns an anonymous
           function based on the comparison
           operator found in the constraint
           for variable i and optional
           variable j. This anonymous function
           compares the two quantities using
           the appropriate relational operator.
        """
        if constraint_info[3] == "==":
            if j != None:
                return lambda Xi, Xj: int(constraint_info[0]) * Xi + int(constraint_info[2]) == Xj
            else:
                return lambda Xi: int(constraint_info[0]) * Xi + int(constraint_info[2]) == int(constraint_info[4])
        elif constraint_info[3] == "!=":
            if j != None:
                return lambda Xi, Xj: int(constraint_info[0]) * Xi + int(constraint_info[2]) != Xj
            else:
                return lambda Xi: int(constraint_info[0]) * Xi + int(constraint_info[2]) != int(constraint_info[4])
        elif constraint_info[3] == "<=":
            if j != None:
                return lambda Xi, Xj: int(constraint_info[0]) * Xi + int(constraint_info[2]) <= Xj
            else:
                return lambda Xi: int(constraint_info[0]) * Xi + int(constraint_info[2]) <= int(constraint_info[4])
        elif constraint_info[3] == ">=":
            if j != None:
                return lambda Xi, Xj: int(constraint_info[0]) * Xi + int(constraint_info[2]) >= Xj
            else:
                return lambda Xi: int(constraint_info[0]) * Xi + int(constraint_info[2]) >= int(constraint_info[4])
        elif constraint_info[3] == "<":
            if j != None:
                return lambda Xi, Xj: int(constraint_info[0]) * Xi + int(constraint_info[2]) < Xj
            else:
                return lambda Xi: int(constraint_info[0]) * Xi + int(constraint_info[2]) < int(constraint_info[4])
        else: # constraint_info[3] == ">"
            if j != None:
                return lambda Xi, Xj: int(constraint_info[0]) * Xi + int(constraint_info[2]) > Xj
            else:
                return lambda Xi: int(constraint_info[0]) * Xi + int(constraint_info[2]) > int(constraint_info[4])

                
                

