# constraints-verifying-solver
Given a number of specified constraints, the program either finds a solution to the problem with these constraints or ends with no solution found. The problem to be solved is provided in a text file which needs to be read in by the program. An instance of the Constraint Satisfaction Problem being examined in this project is defined using the following syntax:

3:4
1 * X0 + 0 < 2
1 * X1 + 1 == 3

The domain line, which is found in the first line, is a string sequence of integers separated by colon. It is then followed by constraint lines. Domains are read from left to right. The first integer represents the domain of variable X0, which is {0, 1 ,2}, and the second integer, domain of X1, which is {0, 1, 2, 3}. In case there are more constraint lines in addition to the ones given in the above example, then they have the domain represented by the last integer in the domain line. 
