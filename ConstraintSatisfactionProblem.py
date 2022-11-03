# This is the Constraint 
# Satisfaction Problem class.
# Instance of this class
# will represent the 
# current constraint 
# satisfaction problem.

class CSP:
    def __init__(self, forward_check=0, list_of_vars=[], domains={}, constraints={}):
        """This method is invoked when creating
           an instance of the class. Its parameters
           take on default values if not given. 
        """
        
        # attribute denoting whether
        # CSP needs to be solved
        # with forward checking
        self._forward_checking = forward_check
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
        # attribute denoting 
        # the neighbor list of
        # each variable
        self._arcs = []
        # attribute denoting
        # the solution of CSP
        self._solution = {}
    
    @property
    def list_of_vars(self):
        return self._list_of_vars
    
    @property
    def domains(self):
        return self._domains
    
    @property
    def constraints(self):
        return self._constraints

    @property
    def arcs(self):
        return self._arcs
    
    def read_file(self, filename):
        """This method helps process a text file
           containing the syntax for a constraint
           satisfaction problem. It will take
           the relevant information regarding a CSP
           and save them into the CSP class instance. 
        """
        flip_signs = {'>': '<', '<': '>',
                      '>=': '<=', '<=': '>=',
                      '!=': '!=', '==': '=='}

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

        # create a dictionary
        # where key is the variable index
        # value is the neighbor list
        neighbors = {}

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

                # tuple <scope, rel>
                scope_rel = None

                # Check if we have a right hand side variable
                if items[6].startswith('X'):
                    # index of second variable
                    var2_index = int(items[6][1])

                    # a 2nd list of elements for 
                    # the other direction (Bidirection) 
                    diff_elements = [items[6], flip_signs[items[5]], items[0], items[2], items[4]]

                    # save index of variable 2 
                    indices.append(var2_index)

                    # get constraints of which var1 and var2 are a part
                    if not constraints.get(var1_index, None): 
                        # if arc is not seen before, create a new list
                        constraints[var1_index] = []
                        # define tuple
                        scope_rel = ((var1_index, var2_index), self.get_relation(var1_index, elements, var2_index))
                        # append relation into the new list
                        constraints[var1_index].append(scope_rel)

                        self._arcs.append((var1_index, var2_index))
                    else:
                        scope_rel = ((var1_index, var2_index),self.get_relation(var1_index, elements, var2_index))
                        # add relation to existing list for arc
                        constraints[var1_index].append(scope_rel)

                        self._arcs.append((var1_index, var2_index))
                    
                    # ensure bidirection for binary constraint
                    if not constraints.get(var2_index, None):
                        constraints[var2_index] = []
                        scope_rel = ((var2_index, var1_index),self.get_relation(var2_index, diff_elements,var1_index))
                        constraints[var2_index].append(scope_rel)

                        self._arcs.append((var2_index, var1_index))
                    else:
                        scope_rel = ((var2_index, var1_index),self.get_relation(var2_index, diff_elements,var1_index))
                        constraints[var2_index].append(scope_rel)

                        self._arcs.append((var2_index, var1_index))
                    
                else: # an integer is found instead
                    # add constraint for this variable 
                    if not constraints.get(var1_index, None):
                        constraints[var1_index] = []
                        constraints[var1_index].append(((var1_index,),self.get_relation(var1_index, elements)))
                    else:
                        constraints[var1_index].append(((var1_index,),self.get_relation(var1_index, elements)))
                    
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
        if j == None:
            return self.get_unary_relation(i, constraint_info)
        else:
            return self.get_binary_relation(i, constraint_info, j)
    
    def get_binary_relation(self, i, constraint_info, j):
        """This method returns an
           anonymous function for
           a binary constraint.
        """
        comparison_ops = ['!=', '==', '<=', '>=', '<', '>'] 
        if constraint_info[3] in comparison_ops:
            if constraint_info[3] == "==":
                return lambda Xi, Xj: int(constraint_info[0]) * Xi + int(constraint_info[2]) == Xj
            elif constraint_info[3] == "!=":
                return lambda Xi, Xj: int(constraint_info[0]) * Xi + int(constraint_info[2]) != Xj
            elif constraint_info[3] == "<=":
                return lambda Xi, Xj: int(constraint_info[0]) * Xi + int(constraint_info[2]) <= Xj
            elif constraint_info[3] == ">=":
                return lambda Xi, Xj: int(constraint_info[0]) * Xi + int(constraint_info[2]) >= Xj
            elif constraint_info[3] == "<":
                return lambda Xi, Xj: int(constraint_info[0]) * Xi + int(constraint_info[2]) < Xj
            else: # constraint_info[3] == ">"
                return lambda Xi, Xj: int(constraint_info[0]) * Xi + int(constraint_info[2]) > Xj
        
        else:
            if constraint_info[1] == "==":
                return lambda Xi, Xj: Xi == int(constraint_info[2]) * Xi + int(constraint_info[4])
            elif constraint_info[1] == "!=":
                return lambda Xi, Xj: Xi != int(constraint_info[2]) * Xi + int(constraint_info[4])
            elif constraint_info[1] == "<=":
                return lambda Xi, Xj: Xi <= int(constraint_info[2]) * Xi + int(constraint_info[4])
            elif constraint_info[1] == ">=":
                return lambda Xi, Xj: Xi >= int(constraint_info[2]) * Xi + int(constraint_info[4])
            elif constraint_info[1] == "<":
                return lambda Xi, Xj: Xi < int(constraint_info[2]) * Xi + int(constraint_info[4])
            else:
                return lambda Xi, Xj: Xi > int(constraint_info[2]) * Xi + int(constraint_info[4])

        
        

    def get_unary_relation(self, i, constraint_info):
        """This method returns
           an anonymous function
           for a unary constrain
        """
        if constraint_info[3] == "==":
            return lambda Xi: int(constraint_info[0]) * Xi + int(constraint_info[2]) == int(constraint_info[4])
        elif constraint_info[3] == "!=":
            return lambda Xi: int(constraint_info[0]) * Xi + int(constraint_info[2]) != int(constraint_info[4])
        elif constraint_info[3] == "<=":
            return lambda Xi: int(constraint_info[0]) * Xi + int(constraint_info[2]) <= int(constraint_info[4])
        elif constraint_info[3] == ">=":
            return lambda Xi: int(constraint_info[0]) * Xi + int(constraint_info[2]) >= int(constraint_info[4])
        elif constraint_info[3] == "<":
            return lambda Xi: int(constraint_info[0]) * Xi + int(constraint_info[2]) < int(constraint_info[4])
        else: # constraint_info[3] == ">"
            return lambda Xi: int(constraint_info[0]) * Xi + int(constraint_info[2]) > int(constraint_info[4])

    def verify_arc_consistency(self):
        """This method helps to check
           if consistency is found between
           two variables (arc formed
           by them). Consistency is 
           preserved when constraints 
           for the two selected variables
           are satisfied. 
        """
        if self._forward_checking:
            # store all arcs specified by the constraints in queue
            queue = self._arcs[:]
        
            # loop through the queue
            while queue:
        
                # look at an item from queue
                # item is a tuple of a tuple and comparison function
                var1, var2 = queue.pop()
                
                # check if CSP needs to be revised
                if self.revise(var1, var2):
                    # is size of domain for variable 1 equal to zero
                    if len(self._domains[var1]) == 0:
                        # an inconsistency is found
                        return False

                    # otherwise
                    # for each neighbor variable in 
                    # the neighbor list of variables 1 minus variable 2
                    for tup in self._arcs:
                        if tup[1] == var1:
                            queue.append(tup)
        return True

    def revise(self, i, j):
        """This method helps the 
           AC-3 algorithm (implemented
           in verify_arc_consistency)
           to reduce the domain of
           variable at position i.
        """
        revised = False
        
        # for each value, x, in domains of X_i
        for X_i_value in self._domains[i]:
            out = False
            
            # for each value, y, in domains of X_j
            for X_j_value in self._domains[j]:
                
                for tup in self._constraints[i]:
                    
                    if tup[0] == (i, j) and tup[1](X_i_value, X_j_value):
                        # Found one value from D_j that makes
                        # (x, y) satisfy the constraint
                        out = True
                        break
                if out:
                    break
            else:
                self._domains[i].remove(X_i_value)
                revised = True


        
        return revised

    def backtracking_search(self):
        """This method helps
           find the solution 
           to the current CSP.
        """
        return self.backtrack(self._solution)
    
    def backtrack(self, assignment):
        """This method is the 
           helper method for
           backtracking_search.
           It will backtrack
           when an assignment
           is invalid.
        """
        if not assignment:
            # TODO: implement select_unassigned_variable
            # choose an unassigned variable
            var = self.select_unassigned_variable(assignment)
            
            # TODO: implement order_domain_values
            for value in self.order_domain_values(var, assignment):
                # if value is consistent with assignment
                    # add {var = value} to the assignment
                    
                    # TODO: Modify verify_arc_consistency
                    # if True (forward checking to be done)
                    if self._forward_checking:
                        inferences = self.verify_arc_consistency(var, value)

                    # if inferences is not failure
                    if not inferences:
                        # add inferences to assignment
                        result = self.backtrack(assignment)
                        # if result is not failure
                        if not result:
                            return result
                # remove {var = value} and 
                # inferences from assignment

        else:
            return assignment

    def select_unassigned_variable(self, assignment):
        """This method returns an
           unassigned variable, using
           two heuristics: (1) minimum-
           remaining-values (MRV) & 
           (2) degree heuristic. If there 
           are more than one variable with 
           the same MRV, then degree heuristic
           is used. If a tie still exists,
           choose an unassigned variable randomly.
        """
        # get a dictionary of unassigned variables and their domains
        unassigned_var_dict = { var: self._domains[var] 
            for var in self._domains if var not in assignment}
        # Get a list of variables
        unassigned_var_list = list(unassigned_var_dict.keys())
        # Pick the minimum item
        min_item = unassigned_var_list[0] # pick the first one

        # Find the variable with the least possible values
        for var in unassigned_var_list:
            # number of possible values
            num_remaining_values = len(unassigned_var_dict[var])
            min_num_values = len(unassigned_var_dict[min_item])

            # Update min item
            # use minimum remaining values heuristic
            if num_remaining_values < min_num_values:
                min_item = var
            elif num_remaining_values == min_num_values:
                # use degree heuristic
                if len(self._constraints[var]) > len(self._constraints[min_item]):
                    min_item = var
        
        return min_item

    def order_domain_values(self, variable, assignment):
        """This method determines
           the order in which the 
           values of the domain
           be tried. It uses the
           least-constraining-value
           heuristic.
        """
        # below is the a list that
        # keeps track of variable and their
        # number of inconsistent constraints,
        # represented as a tuple, e.g. (0, 2) 
        # [X0, 2 constraints]
        var_list = []

        # possible values to be selected
        var_values = self._domains[variable]

        neighbors = self._neighbors[variable]
        
        # verify if variable has neighbor(s) or not
        if len(neighbors) > 0:
            for neighbor in neighbors:
                # keep count of neighbor's inconsistent values
                count = 0

                neighbor_values = self._domains[neighbor]
                for constraint_func in self._constraints[(variable, neighbor)]:
                    for val1 in var_values:
                        for val2 in neighbor_values:
                            if constraint_func(val1, val2):
                                count += 1



                
                

