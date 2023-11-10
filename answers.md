# CMPS 2200 Assignment 4
## Answers

**Name:** Rhon Farber


Place all written answers from `assignment-04.md` here for easier grading.

1a)
The greedy algorithm for producing as few coins as possible that sum to 
N would be continuously choosing the highest denomination coin that fits without exceeding the target dollar amount. The algorithm repeats this process until the total value matches the specified dollar amount.

1b)
The greedy choice is choosing the largest denomination that does not exceed the remaining amount. The optimal substructure properties are proven as follows: given a target N, at each iteration, the greedy choice is made and since the denomations are in base 2, the coin chosen is 2^k. Then the subproblem becomes N - 2^k. This substructure continues as N - 2^k becomes the new N and 2^k is the next largest denomiation that doesn't exceed N. No combination of coins less than 2^k can sum up to 2^k without using more coins at each step, so the solution is optimal.

1c)
The work is W(n) = O(log(n)) 
The span is S(n) = O(log(n)) 
This is because the greedy algorithm does log_2(n) over and over again until n = 0, which is not a parallelizable process. 

2a)
A simple counterexample that shows that the greedy algorithm does not produce the fewest number of coins in Fortuito could be if there are denominations of 1, 3, and 4. The target N is 6. The greedy algorithm would choose 4, and then 1, and then 1 to reach 4 + 1 + 1 = 6. This is not optimal because there is a better solution of choosing 3 and then choosing 3 which is 3 + 3 = 6. This solution uses 2 coins rather than the 3 coins from the greedy solution. 

2b)
In Fortuito, the optimal substructure property is as follows. Assuming you have an optimal solution for making change for N dollars using the fewest coins. The first coin of denomination D is subtracted from the target N. Now the subproblem is N - D. If that subproblem is not optimal then you replace that part of the solution with a better solution for N - D. 

2c)
Using dynamic programming and a bottom-up approach. You can build a 2d array of denominations and their powers. The work is equal to all the nodes of DAG, or W(n) = O(n * k) where n is the length of the set of denominations and k is the highest powers. The span is the longest path in DAG, which is the table so it is S(n) = O(n * k).
