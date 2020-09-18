#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n) - because it goes until n^3 but it increases at a rate of n^2+1 so every time n increases, the amount of times the function runs
increases by n

b)
O(nlog(n)) - inner loop has a rate of log(n) since it doubles, and the outer loop runs n times

c)
O(n) - it runs once each recursion

## Exercise II

Use a binary search algorithm, have a top floor and bottom floor, drop an egg from the middle floor, if it breaks then your new top floor is your former middle,
otherwise your new bottom floor is your former middle. This has O(log(n)) efficiency.