# Constraint Satisfaction Problem solver

# Import libraries
import sys

# Import class
from ConstraintSatisfactionProblem import CSP

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
    
    if forward_check_flag == 0:
        # Create a CSP problem
        problem = CSP()
    else:
    	problem = CSP(forward_check=1)

    # Let CSP take the problem context from file
    problem.read_file(args[0])

    # Test output
    # print("CSP Variables (their indices)")
    # print(problem.list_of_vars)
    # print("CSP Domains")
    # print(problem.domains)
    # print("CSP Constraints")
    # print(problem.constraints)
    # print("Check using constraints")
    # for key, val in problem.constraints.items():
    # 	# key: variable index
    # 	# value: list of tuples where 
    # 	#         a tuple contains a tuple and a function
    # 	print("Variable: ", key)
    # 	print("List: ", val)

    	
    # for var, neighbors in problem.neighbors.items():
    # 	print("Variable: {}\tNeighbors: {}".format(var, neighbors))

    # Test to see all arcs
    print("All arcs:")
    print(problem.arcs)
    print()
    
    result = problem.verify_arc_consistency()
    print("Is CSP arc consistent? ")
    print(result)
    print()

# Run the script
if __name__ == "__main__":
    main()
